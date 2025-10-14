"""
YouTube to Article Writer Agent - Simplified Version
Uses query() instead of ClaudeSDKClient to avoid initialization timeout
"""
import anyio
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions, create_sdk_mcp_server
from tools import (
    read_input_files,
    search_youtube,
    get_transcript,
    generate_initial_article,
    refine_article,
    save_article,
    track_cost,
    get_total_cost,
    reset_cost_tracking
)

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
    Main agent workflow using simple query API.
    """
    log("=" * 60)
    log("YouTube to Article Writer Agent - Starting (Simple Mode)")
    log("=" * 60)

    # Reset cost tracking for this run
    reset_cost_tracking()

    # System prompt for the autonomous agent
    system_prompt = """You are an autonomous agent that creates comprehensive articles from YouTube videos.

Your workflow:
1. Read the topic and article writing instructions from input files
2. Search YouTube for the top 3 most engaging videos on the topic (sorted by comments, then views)
3. Extract English transcripts from each video (skip if unavailable)
4. Generate an initial article draft from the first video's transcript
5. Refine the article by incorporating insights from the second video
6. Further refine the article with insights from the third video
7. Save the final polished article to output/article.md

Key principles:
- Be autonomous and complete all steps without human intervention
- Handle errors gracefully (skip videos without transcripts, continue with available ones)
- Maintain the speaker's authentic voice throughout the article
- Think like an A+ student compiling comprehensive notes from multiple lectures
- Synthesize information from all sources into a cohesive, engaging article
- Follow the user's article writing instructions carefully

If a video doesn't have a transcript, skip it and move to the next one. Always try to use at least one video to generate an article."""

    # Create MCP server with all tools
    mcp_server = create_sdk_mcp_server(
        name="youtube-article-agent",
        tools=[
            read_input_files,
            search_youtube,
            get_transcript,
            generate_initial_article,
            refine_article,
            save_article,
            track_cost,
            get_total_cost
        ]
    )

    # Configure agent options
    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        mcp_servers={"youtube-article-agent": mcp_server},
        max_turns=20
    )

    try:
        log("Starting autonomous workflow with simple query API...")

        query_text = """Execute the complete article generation workflow with explicit data handling:

STEP 1: Read input files
   - Call read_input_files (no parameters required)
   - This returns: {topic: str, article_prompt: str}
   - EXTRACT and STORE: topic_value, article_prompt_value

STEP 2: Search YouTube for videos
   - Call search_youtube with parameter: topic = topic_value (from step 1)
   - This returns: {videos: list, success: bool}
   - EXTRACT the 'videos' field - this is a list of dictionaries
   - Each video dict contains: {video_id, title, channel, views, comments, description}
   - STORE this videos list for later use

STEP 3: Extract transcripts from top 3 videos
   - Loop through the first 3 videos in the videos list from step 2
   - For EACH video:
     a. Call get_transcript with parameters:
        - video_id: video['video_id'] (from videos list)
        - video_title: video['title'] (from videos list)
     b. Check the 'success' field in the return value
     c. If success is True: store the transcript and video metadata
     d. If success is False: skip to next video
   - Keep track of which videos have successful transcripts

STEP 4: Generate initial article
   - Use the FIRST video that has a successful transcript
   - Call generate_initial_article with parameters:
     * transcript: (the transcript text from step 3)
     * article_prompt: article_prompt_value (from step 1)
     * video_title: video['title'] (from the video with successful transcript)
     * channel_name: video['channel'] (from the video with successful transcript)
     * topic: topic_value (from step 1)
   - This returns: {article: str, input_tokens: int, output_tokens: int, cost: float, success: bool}
   - EXTRACT and STORE:
     * current_article = return['article']
     * gen_input_tokens = return['input_tokens']
     * gen_output_tokens = return['output_tokens']
     * gen_cost = return['cost']

STEP 5: Track cost for initial generation
   - Call track_cost with parameters:
     * input_tokens: gen_input_tokens (from step 4)
     * output_tokens: gen_output_tokens (from step 4)
     * cost: gen_cost (from step 4)
     * operation: "Initial article generation"

STEP 6: Refine with second video (if available)
   - If a SECOND video has a successful transcript:
     a. Call refine_article with parameters:
        * current_article: current_article (from step 4)
        * new_transcript: (transcript from second video)
        * article_prompt: article_prompt_value (from step 1)
        * video_title: (second video's title)
        * channel_name: (second video's channel)
        * iteration: 2
     b. This returns: {article: str, input_tokens: int, output_tokens: int, cost: float}
     c. EXTRACT and UPDATE:
        * current_article = return['article'] (overwrite previous)
        * ref2_input_tokens = return['input_tokens']
        * ref2_output_tokens = return['output_tokens']
        * ref2_cost = return['cost']
     d. Call track_cost with:
        * input_tokens: ref2_input_tokens
        * output_tokens: ref2_output_tokens
        * cost: ref2_cost
        * operation: "Refinement with video 2"

STEP 7: Refine with third video (if available)
   - If a THIRD video has a successful transcript:
     a. Call refine_article with parameters:
        * current_article: current_article (from step 6, or step 4 if step 6 was skipped)
        * new_transcript: (transcript from third video)
        * article_prompt: article_prompt_value (from step 1)
        * video_title: (third video's title)
        * channel_name: (third video's channel)
        * iteration: 3
     b. EXTRACT and UPDATE:
        * current_article = return['article'] (this is now the final article)
        * ref3_input_tokens = return['input_tokens']
        * ref3_output_tokens = return['output_tokens']
        * ref3_cost = return['cost']
     c. Call track_cost with:
        * input_tokens: ref3_input_tokens
        * output_tokens: ref3_output_tokens
        * cost: ref3_cost
        * operation: "Refinement with video 3"

STEP 8: Get total cost summary
   - Call get_total_cost (no parameters required)
   - This returns: {total_cost: float, total_input_tokens: int, total_output_tokens: int}
   - EXTRACT and STORE:
     * final_total_cost = return['total_cost']
     * final_total_input_tokens = return['total_input_tokens']
     * final_total_output_tokens = return['total_output_tokens']

STEP 9: Save the final article
   - Build a video_sources list containing the metadata for ALL videos that were used
   - For each video that had a successful transcript and was used for generation/refinement:
     * Include the full video dict: {video_id, title, channel, views, comments}
   - Call save_article with parameters:
     * article: current_article (the final refined article from step 7, or step 6, or step 4)
     * video_sources: (the list of video metadata dicts you just built)
     * topic: topic_value (from step 1)
     * total_cost: final_total_cost (from step 8)
     * total_input_tokens: final_total_input_tokens (from step 8)
     * total_output_tokens: final_total_output_tokens (from step 8)

ERROR HANDLING:
- If a transcript extraction fails, skip that video and continue to the next
- If ALL videos fail to provide transcripts, report an error clearly
- Ensure at least one video is successfully used to generate an article

DATA EXTRACTION IS CRITICAL:
- Always extract specific fields from tool return values
- Store extracted values in named variables
- Pass the correct stored values to subsequent tool calls
- Build proper data structures (like the video_sources list)

Begin execution now."""

        log("Sending query to agent...")

        # Use simple query API
        async for message in query(prompt=query_text, options=options):
            # Print agent messages in real-time
            print(message, end='', flush=True)

        log("\n" + "=" * 60)
        log("Agent workflow completed successfully!")
        log("=" * 60)

        # Check if output was created
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(base_dir, 'output', 'article.md')

        if os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            log(f"Article saved to: {output_path}")
            log(f"File size: {file_size} bytes")
        else:
            log("Warning: Output file not found. Check logs for errors.", level="WARNING")

    except KeyboardInterrupt:
        log("Agent execution interrupted by user", level="WARNING")
        sys.exit(1)

    except Exception as e:
        log(f"Fatal error: {str(e)}", level="ERROR")
        log("Full error details:", level="ERROR")
        import traceback
        log(traceback.format_exc(), level="ERROR")
        sys.exit(1)


if __name__ == "__main__":
    log("Python version: " + sys.version)
    log("Working directory: " + os.getcwd())

    # Verify environment
    if not os.getenv("ANTHROPIC_API_KEY"):
        log("Warning: ANTHROPIC_API_KEY not found in environment", level="WARNING")

    # Run the agent
    anyio.run(main)
