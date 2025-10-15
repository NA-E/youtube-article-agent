"""
YouTube transcript extraction tool using RapidAPI YouTube Transcript3 service.
"""
import os
import re
import json
from typing import Any
import httpx
from claude_agent_sdk import tool
from .transcript_cleaner import process_transcript


def _validate_video_id(video_id: str) -> bool:
    """
    Validate YouTube video ID format.

    YouTube video IDs are exactly 11 characters containing only:
    - Alphanumeric characters (a-z, A-Z, 0-9)
    - Dashes (-)
    - Underscores (_)

    Args:
        video_id: The video ID to validate

    Returns:
        True if valid YouTube video ID format, False otherwise
    """
    if not isinstance(video_id, str):
        return False
    if len(video_id) != 11:
        return False
    return bool(re.match(r'^[a-zA-Z0-9_-]{11}$', video_id))


@tool(
    name="get_transcript",
    description="Extract English transcript from a YouTube video by video ID using RapidAPI",
    input_schema={
        "video_id": str,
        "video_title": str  # For better error messages
    }
)
async def get_transcript(args: dict[str, Any]) -> dict[str, Any]:
    """
    Extract English transcript from a YouTube video using RapidAPI.

    Args:
        video_id: The YouTube video ID
        video_title: Title of the video (for logging)

    Returns:
        Dictionary with:
        - transcript: Full cleaned transcript text
        - video_id: The video ID
        - success: Boolean indicating success
        - error: Error message if failed
    """
    video_id = args["video_id"]
    video_title = args.get("video_title", "Unknown")

    print('\n========================================')
    print('[YouTube Extractor] STARTING TRANSCRIPT EXTRACTION')
    print(f'[YouTube Extractor] Video: {video_title}')
    print(f'[YouTube Extractor] Video ID: {video_id}')
    print('========================================\n')

    # Validate video ID format (security: prevent injection attacks)
    if not _validate_video_id(video_id):
        error_msg = f'Invalid video ID format: {video_id}'
        print(f'[YouTube Extractor] ❌ ERROR: {error_msg}')
        print('[YouTube Extractor] YouTube video IDs must be exactly 11 characters (alphanumeric, dash, underscore)')
        return {
            "content": [{
                "type": "text",
                "text": f"Error: {error_msg}\n\nYouTube video IDs must be 11 characters (alphanumeric, dash, underscore).\nSkipping this video..."
            }],
            "video_id": video_id,
            "success": False,
            "error": "Invalid video ID format"
        }

    # Check for RapidAPI key
    rapidapi_key = os.getenv('RAPIDAPI_KEY')

    print('[YouTube Extractor] Checking RapidAPI key...')
    if not rapidapi_key:
        error_msg = 'RAPIDAPI_KEY environment variable not set'
        print(f'[YouTube Extractor] ❌ ERROR: {error_msg}')
        return {
            "content": [{
                "type": "text",
                "text": f"Error: {error_msg}\n\nPlease set RAPIDAPI_KEY in your .env file.\nSkipping this video..."
            }],
            "video_id": video_id,
            "success": False,
            "error": error_msg
        }

    print('[YouTube Extractor] ✓ RapidAPI key found')

    # Construct YouTube URL from video ID
    youtube_url = f'https://www.youtube.com/watch?v={video_id}'

    # RapidAPI endpoint
    api_url = 'https://youtube-transcript3.p.rapidapi.com/api/transcript-with-url'

    print('[YouTube Extractor] Preparing API request...')
    print(f'[YouTube Extractor] Endpoint: {api_url}')
    print(f'[YouTube Extractor] YouTube URL: {youtube_url}')

    headers = {
        'x-rapidapi-host': 'youtube-transcript3.p.rapidapi.com',
        'x-rapidapi-key': rapidapi_key,
        'Content-Type': 'application/json'
    }

    params = {
        'url': youtube_url,
        'flat_text': 'true'
    }

    print('[YouTube Extractor] Headers configured (API key hidden)')
    print('[YouTube Extractor] Making HTTP GET request...')

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                api_url,
                headers=headers,
                params=params
            )

        print('[YouTube Extractor] Response received')
        print(f'[YouTube Extractor] Status: {response.status_code}')

        if response.status_code != 200:
            error_text = response.text
            print('[YouTube Extractor] ❌ API request failed')
            print(f'[YouTube Extractor] Status: {response.status_code}')
            print(f'[YouTube Extractor] Response: {error_text}')

            return {
                "content": [{
                    "type": "text",
                    "text": f"RapidAPI request failed for {video_title}\nStatus: {response.status_code}\nResponse: {error_text}\n\nSkipping this video..."
                }],
                "video_id": video_id,
                "success": False,
                "error": f"API request failed with status {response.status_code}"
            }

        print('[YouTube Extractor] Parsing JSON response...')

        try:
            data = response.json()
        except json.JSONDecodeError as e:
            error_preview = response.text[:500]  # First 500 chars
            print('[YouTube Extractor] ❌ Invalid JSON response from RapidAPI')
            print(f'[YouTube Extractor] Parse error: {str(e)}')
            print(f'[YouTube Extractor] Response preview: {error_preview}')

            return {
                "content": [{
                    "type": "text",
                    "text": f"Invalid response from RapidAPI for {video_title}\n\nExpected JSON but received:\n{error_preview}\n\nSkipping this video..."
                }],
                "video_id": video_id,
                "success": False,
                "error": f"Invalid JSON response: {str(e)}"
            }

        print('[YouTube Extractor] Response parsed successfully')
        print(f'[YouTube Extractor] Success: {data.get("success", False)}')

        if not data.get('transcript'):
            error_msg = data.get('message', 'Unknown error')
            print('[YouTube Extractor] ❌ No transcript available')
            print(f'[YouTube Extractor] Message: {error_msg}')

            return {
                "content": [{
                    "type": "text",
                    "text": f"No transcript available for {video_title}\nMessage: {error_msg}\n\nSkipping this video..."
                }],
                "video_id": video_id,
                "success": False,
                "error": "No transcript available"
            }

        raw_transcript = data['transcript']
        transcript_length = len(raw_transcript)

        print('[YouTube Extractor] ✓ Transcript extracted successfully')
        print(f'[YouTube Extractor] Raw transcript length: {transcript_length} characters')
        print(f'[YouTube Extractor] Preview: {raw_transcript[:100]}...')
        print('\n========================================')
        print('[YouTube Extractor] TRANSCRIPT EXTRACTION COMPLETED')
        print('========================================\n')

        # Clean and process the transcript
        try:
            processed_transcript = process_transcript(raw_transcript)
            word_count = len(processed_transcript.split())

            return {
                "content": [{
                    "type": "text",
                    "text": f"Successfully extracted and cleaned transcript for: {video_title}\n\nVideo ID: {video_id}\nRaw length: {transcript_length} characters\nProcessed length: {len(processed_transcript)} characters\nWord count: ~{word_count} words"
                }],
                "video_id": video_id,
                "transcript": processed_transcript,
                "word_count": word_count,
                "success": True
            }

        except ValueError as e:
            # Cleaning failed, but we have the raw transcript
            print(f'[YouTube Extractor] ⚠️ Cleaning failed: {str(e)}')
            print('[YouTube Extractor] Returning raw transcript')

            word_count = len(raw_transcript.split())
            return {
                "content": [{
                    "type": "text",
                    "text": f"Extracted transcript for: {video_title} (cleaning failed, using raw)\n\nVideo ID: {video_id}\nTranscript length: {transcript_length} characters\nWord count: ~{word_count} words"
                }],
                "video_id": video_id,
                "transcript": raw_transcript,
                "word_count": word_count,
                "success": True
            }

    except httpx.TimeoutException:
        error_msg = 'Request timeout (30 seconds)'
        print(f'[YouTube Extractor] ❌ {error_msg}')
        return {
            "content": [{
                "type": "text",
                "text": f"Timeout extracting transcript for {video_title}\n\nThe request took too long. Skipping this video..."
            }],
            "video_id": video_id,
            "success": False,
            "error": error_msg
        }

    except Exception as e:
        error_msg = str(e)
        print('[YouTube Extractor] ❌ Unexpected error during extraction')
        print(f'[YouTube Extractor] Error: {error_msg}')

        return {
            "content": [{
                "type": "text",
                "text": f"Error extracting transcript for {video_title}: {error_msg}\n\nSkipping this video..."
            }],
            "video_id": video_id,
            "success": False,
            "error": error_msg
        }
