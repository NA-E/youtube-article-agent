"""
YouTube transcript extraction tool using youtube-transcript-api.
"""
from typing import Any
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)
from claude_agent_sdk import tool


@tool(
    name="get_transcript",
    description="Extract English transcript from a YouTube video by video ID",
    input_schema={
        "video_id": str,
        "video_title": str  # For better error messages
    }
)
async def get_transcript(args: dict[str, Any]) -> dict[str, Any]:
    """
    Extract English transcript from a YouTube video.

    Args:
        video_id: The YouTube video ID
        video_title: Title of the video (for logging)

    Returns:
        Dictionary with:
        - transcript: Full transcript text
        - video_id: The video ID
        - success: Boolean indicating success
        - error: Error message if failed
    """
    try:
        video_id = args["video_id"]
        video_title = args.get("video_title", "Unknown")

        # Try to get English transcript using fetch() method (v1.2.2+ API)
        try:
            transcript = YouTubeTranscriptApi().fetch(
                video_id,
                languages=['en', 'en-US', 'en-GB']
            )
        except NoTranscriptFound:
            # Try to get auto-generated English transcript
            transcript = YouTubeTranscriptApi().fetch(
                video_id,
                languages=['en']
            )

        # Combine all transcript snippets into continuous text
        # transcript.snippets is a list of FetchedTranscriptSnippet objects with .text attribute
        transcript_text = ' '.join([snippet.text for snippet in transcript.snippets])

        # Clean up transcript
        transcript_text = transcript_text.replace('\n', ' ')
        transcript_text = ' '.join(transcript_text.split())  # Remove extra whitespace

        word_count = len(transcript_text.split())

        return {
            "content": [{
                "type": "text",
                "text": f"Successfully extracted transcript for: {video_title}\n\nVideo ID: {video_id}\nTranscript length: {len(transcript_text)} characters\nWord count: ~{word_count} words"
            }],
            "video_id": video_id,
            "transcript": transcript_text,
            "word_count": word_count,
            "success": True
        }

    except TranscriptsDisabled:
        return {
            "content": [{
                "type": "text",
                "text": f"Transcripts are disabled for video: {video_title} (ID: {video_id})\n\nSkipping this video..."
            }],
            "video_id": video_id,
            "success": False,
            "error": "Transcripts disabled"
        }

    except NoTranscriptFound:
        return {
            "content": [{
                "type": "text",
                "text": f"No English transcript found for video: {video_title} (ID: {video_id})\n\nThis video may not have captions available. Skipping..."
            }],
            "video_id": video_id,
            "success": False,
            "error": "No transcript found"
        }

    except VideoUnavailable:
        return {
            "content": [{
                "type": "text",
                "text": f"Video unavailable: {video_title} (ID: {video_id})\n\nThe video may have been deleted or is private. Skipping..."
            }],
            "video_id": video_id,
            "success": False,
            "error": "Video unavailable"
        }

    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"Error extracting transcript for {video_title}: {str(e)}\n\nSkipping this video..."
            }],
            "video_id": video_id,
            "success": False,
            "error": str(e)
        }
