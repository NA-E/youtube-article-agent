"""
YouTube search tool using YouTube Data API v3.
"""
import os
from typing import Any
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from claude_agent_sdk import tool

# Load environment variables
load_dotenv()


@tool(
    name="search_youtube",
    description="Search YouTube for videos on a given topic and return top 3 videos sorted by engagement (comments, then views)",
    input_schema={
        "topic": str
    }
)
async def search_youtube(args: dict[str, Any]) -> dict[str, Any]:
    """
    Search YouTube and return top 3 videos with most engagement.

    Args:
        topic: The search query/topic

    Returns:
        Dictionary with list of video metadata including:
        - video_id
        - title
        - channel
        - views
        - comments
        - duration
        - description
    """
    try:
        topic = args["topic"]
        api_key = os.getenv("YOUTUBE_API_KEY")

        if not api_key or api_key == "your_youtube_api_key_here":
            return {
                "content": [{
                    "type": "text",
                    "text": "Error: YOUTUBE_API_KEY not set in .env file. Please add your YouTube Data API v3 key."
                }],
                "isError": True
            }

        # Build YouTube API client
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Search for videos with captions (English)
        search_request = youtube.search().list(
            part="id,snippet",
            q=topic,
            type="video",
            videoCaption="closedCaption",  # Only videos with captions
            relevanceLanguage="en",
            maxResults=20,  # Get more results to filter and sort
            order="relevance"
        )

        search_response = search_request.execute()

        if not search_response.get('items'):
            return {
                "content": [{
                    "type": "text",
                    "text": f"No videos found for topic: {topic}"
                }],
                "isError": True
            }

        # Extract video IDs
        video_ids = [item['id']['videoId'] for item in search_response['items']]

        # Get detailed video statistics
        videos_request = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=','.join(video_ids)
        )

        videos_response = videos_request.execute()

        # Process and sort videos
        videos = []
        for item in videos_response['items']:
            snippet = item['snippet']
            statistics = item.get('statistics', {})
            content_details = item.get('contentDetails', {})

            # Parse statistics (some may be disabled)
            view_count = int(statistics.get('viewCount', 0))
            comment_count = int(statistics.get('commentCount', 0))
            like_count = int(statistics.get('likeCount', 0))

            video_data = {
                'video_id': item['id'],
                'title': snippet['title'],
                'channel': snippet['channelTitle'],
                'description': snippet.get('description', ''),
                'published_at': snippet['publishedAt'],
                'views': view_count,
                'comments': comment_count,
                'likes': like_count,
                'duration': content_details.get('duration', 'Unknown')
            }

            videos.append(video_data)

        # Sort by comments (descending), then views (descending)
        videos.sort(key=lambda x: (x['comments'], x['views']), reverse=True)

        # Get top 3
        top_videos = videos[:3]

        # Format response text
        response_text = f"Found {len(videos)} videos with captions for topic: '{topic}'\n\n"
        response_text += "Top 3 videos by engagement:\n\n"

        for i, video in enumerate(top_videos, 1):
            response_text += f"{i}. {video['title']}\n"
            response_text += f"   - Channel: {video['channel']}\n"
            response_text += f"   - Views: {video['views']:,}\n"
            response_text += f"   - Comments: {video['comments']:,}\n"
            response_text += f"   - Video ID: {video['video_id']}\n"
            response_text += f"   - URL: https://www.youtube.com/watch?v={video['video_id']}\n\n"

        return {
            "content": [{
                "type": "text",
                "text": response_text
            }],
            "videos": top_videos,
            "success": True
        }

    except HttpError as e:
        error_reason = e.error_details[0].get('reason', 'Unknown') if e.error_details else 'Unknown'
        error_message = f"YouTube API Error: {error_reason}"

        if 'quotaExceeded' in error_reason:
            error_message += "\n\nYour YouTube API quota has been exceeded. Quota resets daily. Please try again in 24 hours."
        elif 'keyInvalid' in error_reason:
            error_message += "\n\nYour YouTube API key is invalid. Please check your .env file."

        return {
            "content": [{
                "type": "text",
                "text": error_message
            }],
            "isError": True
        }

    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"Error searching YouTube: {str(e)}"
            }],
            "isError": True
        }
