"""
YouTube to Article Writer Agent - Direct Execution Version
Calls tools directly without Claude Agent SDK
"""
import asyncio
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
# Import the actual async functions (unwrap from @tool decorator)
from tools.file_handler import read_input_files as read_input_files_tool, save_article as save_article_tool
from tools.youtube_search import search_youtube as search_youtube_tool
from tools.transcript_fetcher import get_transcript as get_transcript_tool
from tools.article_generator import generate_initial_article as generate_initial_article_tool, refine_article as refine_article_tool
from tools.cost_tracker import track_cost as track_cost_tool, get_total_cost as get_total_cost_tool, reset_cost_tracking

# Extract the actual async functions from the @tool decorated objects
read_input_files = read_input_files_tool.handler
search_youtube = search_youtube_tool.handler
get_transcript = get_transcript_tool.handler
generate_initial_article = generate_initial_article_tool.handler
refine_article = refine_article_tool.handler
save_article = save_article_tool.handler
track_cost = track_cost_tool.handler
get_total_cost = get_total_cost_tool.handler

# Load environment variables
load_dotenv()


# Logging utility
def log(message: str, level: str = "INFO"):
    """Log messages to console and log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{level}] {message}"
    print(log_message)

    # Append to log file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, 'agent_log.txt')

    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_message + '\n')


async def main():
    """
    Main agent workflow - direct tool execution.
    """
    log("=" * 60)
    log("YouTube to Article Writer Agent - Direct Execution")
    log("=" * 60)

    # Reset cost tracking for this run
    reset_cost_tracking()

    try:
        # STEP 1: Read input files
        log("STEP 1: Reading input files...")
        inputs_result = await read_input_files({})

        if inputs_result.get("isError"):
            log(f"Error reading inputs: {inputs_result['content'][0]['text']}", level="ERROR")
            return

        # Defensive KeyError handling: ensure expected fields exist
        try:
            topic = inputs_result["topic"]
            article_prompt = inputs_result["article_prompt"]
        except KeyError as e:
            log(f"Error: Input result missing expected field: {e}", level="ERROR")
            log(f"Available fields: {list(inputs_result.keys())}", level="ERROR")
            return

        log(f"[OK] Topic: {topic}")
        log(f"[OK] Article prompt loaded ({len(article_prompt)} chars)")

        # STEP 2: Search YouTube
        log(f"\nSTEP 2: Searching YouTube for '{topic}'...")
        search_result = await search_youtube({"topic": topic})

        if search_result.get("isError"):
            log(f"Error searching YouTube: {search_result['content'][0]['text']}", level="ERROR")
            return

        # Defensive KeyError handling: ensure videos field exists
        try:
            videos = search_result["videos"]
        except KeyError as e:
            log(f"Error: Search result missing 'videos' field: {e}", level="ERROR")
            log(f"Available fields: {list(search_result.keys())}", level="ERROR")
            return

        log(f"[OK] Found {len(videos)} videos")
        for i, video in enumerate(videos, 1):
            log(f"  {i}. {video['title']} ({video['comments']:,} comments, {video['views']:,} views)")

        # STEP 3: Extract transcripts from top 3 videos
        log(f"\nSTEP 3: Extracting transcripts...")
        successful_transcripts = []

        for i, video in enumerate(videos[:3], 1):
            log(f"  Attempting video {i}: {video['title']}")
            transcript_result = await get_transcript({
                "video_id": video["video_id"],
                "video_title": video["title"]
            })

            if transcript_result.get("success"):
                # Defensive KeyError handling: ensure transcript fields exist
                try:
                    successful_transcripts.append({
                        "video": video,
                        "transcript": transcript_result["transcript"],
                        "word_count": transcript_result["word_count"]
                    })
                    log(f"  [OK] Video {i}: Success! ({transcript_result['word_count']} words)")
                except KeyError as e:
                    log(f"  [WARNING] Transcript result missing field: {e}", level="WARNING")
                    log(f"  Available fields: {list(transcript_result.keys())}", level="WARNING")
                    # Don't add to successful_transcripts, continue to next video
            else:
                log(f"  [FAIL] Video {i}: {transcript_result.get('error', 'Failed')}")

        if len(successful_transcripts) == 0:
            log("ERROR: No videos with transcripts found!", level="ERROR")
            return

        log(f"\n[OK] Successfully extracted {len(successful_transcripts)} transcript(s)")

        # STEP 4: Generate initial article from first video
        log(f"\nSTEP 4: Generating initial article...")
        first_video_data = successful_transcripts[0]

        gen_result = await generate_initial_article({
            "transcript": first_video_data["transcript"],
            "article_prompt": article_prompt,
            "video_title": first_video_data["video"]["title"],
            "channel_name": first_video_data["video"]["channel"],
            "topic": topic
        })

        if not gen_result.get("success"):
            log(f"Error generating article: {gen_result['content'][0]['text']}", level="ERROR")
            return

        # Defensive KeyError handling: ensure article generation fields exist
        try:
            current_article = gen_result["article"]
            word_count = gen_result["word_count"]
            cost = gen_result["cost"]
        except KeyError as e:
            log(f"Error: Article generation result missing field: {e}", level="ERROR")
            log(f"Available fields: {list(gen_result.keys())}", level="ERROR")
            return

        log(f"[OK] Initial article generated ({word_count} words)")
        log(f"  Cost: ${cost:.4f}")

        # Save draft after initial generation
        video_sources_draft = [{
            "video_id": successful_transcripts[0]["video"]["video_id"],
            "title": successful_transcripts[0]["video"]["title"],
            "channel": successful_transcripts[0]["video"]["channel"],
            "views": successful_transcripts[0]["video"]["views"],
            "comments": successful_transcripts[0]["video"]["comments"]
        }]

        await save_article({
            "article": current_article,
            "video_sources": video_sources_draft,
            "topic": topic,
            "total_cost": 0.0,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
            "is_draft": True
        })
        log(f"[OK] Draft saved: article_draft.md")

        # STEP 5: Track cost for initial generation
        await track_cost({
            "input_tokens": gen_result["input_tokens"],
            "output_tokens": gen_result["output_tokens"],
            "cost": gen_result["cost"],
            "operation": "Initial article generation"
        })

        # STEP 6: Refine with second video (if available)
        if len(successful_transcripts) >= 2:
            log(f"\nSTEP 6: Refining article with video 2...")
            second_video_data = successful_transcripts[1]

            refine_result = await refine_article({
                "current_article": current_article,
                "new_transcript": second_video_data["transcript"],
                "article_prompt": article_prompt,
                "video_title": second_video_data["video"]["title"],
                "channel_name": second_video_data["video"]["channel"],
                "iteration": 2
            })

            if refine_result.get("success"):
                # Defensive KeyError handling: ensure refinement fields exist
                try:
                    current_article = refine_result["article"]
                    word_count = refine_result["word_count"]
                    cost = refine_result["cost"]
                except KeyError as e:
                    log(f"Warning: Refinement result missing field: {e}", level="WARNING")
                    log(f"Available fields: {list(refine_result.keys())}", level="WARNING")
                    log(f"Continuing with current article version...", level="WARNING")
                else:
                    log(f"[OK] Article refined with video 2 ({word_count} words)")
                    log(f"  Cost: ${cost:.4f}")

                # Update draft with 2 videos
                video_sources_draft = []
                for i in range(min(2, len(successful_transcripts))):
                    video_sources_draft.append({
                        "video_id": successful_transcripts[i]["video"]["video_id"],
                        "title": successful_transcripts[i]["video"]["title"],
                        "channel": successful_transcripts[i]["video"]["channel"],
                        "views": successful_transcripts[i]["video"]["views"],
                        "comments": successful_transcripts[i]["video"]["comments"]
                    })

                await save_article({
                    "article": current_article,
                    "video_sources": video_sources_draft,
                    "topic": topic,
                    "total_cost": 0.0,
                    "total_input_tokens": 0,
                    "total_output_tokens": 0,
                    "is_draft": True
                })
                log(f"[OK] Draft updated with video 2")

                # Only track cost if we successfully extracted the fields
                await track_cost({
                    "input_tokens": refine_result["input_tokens"],
                    "output_tokens": refine_result["output_tokens"],
                    "cost": cost,
                    "operation": "Refinement with video 2"
                })
            else:
                log(f"Warning: Refinement with video 2 failed", level="WARNING")
        else:
            log(f"\nSTEP 6: Skipped (only 1 video available)")

        # STEP 7: Refine with third video (if available)
        if len(successful_transcripts) >= 3:
            log(f"\nSTEP 7: Refining article with video 3...")
            third_video_data = successful_transcripts[2]

            refine_result = await refine_article({
                "current_article": current_article,
                "new_transcript": third_video_data["transcript"],
                "article_prompt": article_prompt,
                "video_title": third_video_data["video"]["title"],
                "channel_name": third_video_data["video"]["channel"],
                "iteration": 3
            })

            if refine_result.get("success"):
                # Defensive KeyError handling: ensure refinement fields exist
                try:
                    current_article = refine_result["article"]
                    word_count = refine_result["word_count"]
                    cost = refine_result["cost"]
                except KeyError as e:
                    log(f"Warning: Refinement result missing field: {e}", level="WARNING")
                    log(f"Available fields: {list(refine_result.keys())}", level="WARNING")
                    log(f"Continuing with current article version...", level="WARNING")
                else:
                    log(f"[OK] Article refined with video 3 ({word_count} words)")
                    log(f"  Cost: ${cost:.4f}")

                # Update draft with 3 videos
                video_sources_draft = []
                for i in range(min(3, len(successful_transcripts))):
                    video_sources_draft.append({
                        "video_id": successful_transcripts[i]["video"]["video_id"],
                        "title": successful_transcripts[i]["video"]["title"],
                        "channel": successful_transcripts[i]["video"]["channel"],
                        "views": successful_transcripts[i]["video"]["views"],
                        "comments": successful_transcripts[i]["video"]["comments"]
                    })

                await save_article({
                    "article": current_article,
                    "video_sources": video_sources_draft,
                    "topic": topic,
                    "total_cost": 0.0,
                    "total_input_tokens": 0,
                    "total_output_tokens": 0,
                    "is_draft": True
                })
                log(f"[OK] Draft updated with video 3")

                # Only track cost if we successfully extracted the fields
                await track_cost({
                    "input_tokens": refine_result["input_tokens"],
                    "output_tokens": refine_result["output_tokens"],
                    "cost": cost,
                    "operation": "Refinement with video 3"
                })
            else:
                log(f"Warning: Refinement with video 3 failed", level="WARNING")
        else:
            log(f"\nSTEP 7: Skipped (only {len(successful_transcripts)} video(s) available)")

        # STEP 8: Get total cost summary
        log(f"\nSTEP 8: Generating cost summary...")
        cost_result = await get_total_cost({})

        total_cost = cost_result["total_cost"]
        total_input_tokens = cost_result["total_input_tokens"]
        total_output_tokens = cost_result["total_output_tokens"]

        # Skip fancy Unicode display due to Windows encoding issues
        log(f"Total Cost: ${total_cost:.4f}")
        log(f"Total Input Tokens: {total_input_tokens:,}")
        log(f"Total Output Tokens: {total_output_tokens:,}")

        # STEP 9: Save the final article
        log(f"\nSTEP 9: Saving final article...")

        # Build video_sources list
        video_sources = []
        for item in successful_transcripts:
            video_sources.append({
                "video_id": item["video"]["video_id"],
                "title": item["video"]["title"],
                "channel": item["video"]["channel"],
                "views": item["video"]["views"],
                "comments": item["video"]["comments"]
            })

        save_result = await save_article({
            "article": current_article,
            "video_sources": video_sources,
            "topic": topic,
            "total_cost": total_cost,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "is_draft": False  # Final version with topic + timestamp
        })

        if save_result.get("success"):
            log(f"[OK] Article saved to: {save_result['file_path']}")
        else:
            log(f"Error saving article: {save_result['content'][0]['text']}", level="ERROR")
            return

        # Final summary
        log("\n" + "=" * 60)
        log("[OK] WORKFLOW COMPLETED SUCCESSFULLY!")
        log("=" * 60)
        log(f"Videos processed: {len(successful_transcripts)}")
        log(f"Final article length: {len(current_article)} characters")
        log(f"Total cost: ${total_cost:.4f}")
        log(f"Output: {save_result['file_path']}")
        log("=" * 60)

    except KeyboardInterrupt:
        log("\nAgent execution interrupted by user", level="WARNING")
        sys.exit(1)

    except Exception as e:
        log(f"\nFatal error: {str(e)}", level="ERROR")
        log("Full error details:", level="ERROR")
        import traceback
        log(traceback.format_exc(), level="ERROR")
        sys.exit(1)


if __name__ == "__main__":
    log("Python version: " + sys.version)
    log("Working directory: " + os.getcwd())

    # Verify environment
    if not os.getenv("ANTHROPIC_API_KEY"):
        log("ERROR: ANTHROPIC_API_KEY not found in environment", level="ERROR")
        log("Please set ANTHROPIC_API_KEY in your .env file or system environment", level="ERROR")
        sys.exit(1)

    if not os.getenv("YOUTUBE_API_KEY"):
        log("ERROR: YOUTUBE_API_KEY not found in environment", level="ERROR")
        log("Please set YOUTUBE_API_KEY in your .env file", level="ERROR")
        sys.exit(1)

    if not os.getenv("RAPIDAPI_KEY"):
        log("ERROR: RAPIDAPI_KEY not found in environment", level="ERROR")
        log("Please set RAPIDAPI_KEY in your .env file", level="ERROR")
        log("Sign up at: https://rapidapi.com/", level="ERROR")
        log("Subscribe to: https://rapidapi.com/mivano94/api/youtube-transcript3", level="ERROR")
        sys.exit(1)

    # Run the agent
    asyncio.run(main())
