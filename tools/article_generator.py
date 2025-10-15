"""
Article generation and refinement tools using Claude API.
"""
import os
from typing import Any
from anthropic import AsyncAnthropic
from claude_agent_sdk import tool


# Initialize Anthropic async client (prevents blocking event loop)
client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


@tool(
    name="generate_initial_article",
    description="Generate the first draft of an article from a YouTube video transcript",
    input_schema={
        "transcript": str,
        "article_prompt": str,
        "video_title": str,
        "channel_name": str,
        "topic": str
    }
)
async def generate_initial_article(args: dict[str, Any]) -> dict[str, Any]:
    """
    Create initial article draft from first video's transcript.

    Args:
        transcript: The video transcript text
        article_prompt: User's article writing instructions
        video_title: Title of the video
        channel_name: Name of the channel
        topic: Original search topic

    Returns:
        Dictionary with the generated article draft
    """
    try:
        transcript = args["transcript"]
        article_prompt = args["article_prompt"]
        video_title = args["video_title"]
        channel_name = args["channel_name"]
        topic = args.get("topic", "")

        # Construct the prompt for Claude
        system_prompt = """You are a professional content writer who specializes in transforming video transcripts into engaging, well-structured articles. Your goal is to capture the speaker's voice, insights, and key points while creating polished, readable content."""

        user_prompt = f"""Using the transcript below from a YouTube video, write a comprehensive article that captures the speaker's insights and maintains their authentic voice.

**Original Topic:** {topic}

**Video Information:**
- Title: {video_title}
- Channel: {channel_name}

**Article Writing Instructions:**
{article_prompt}

**Video Transcript:**
{transcript}

**Your Task:**
Create a well-structured article that:
1. Captures the speaker's main insights and key points
2. Maintains the speaker's authentic voice and style
3. Follows the article writing instructions provided above
4. Is engaging, clear, and well-organized
5. Uses proper markdown formatting (headings, lists, etc.)
6. Flows naturally from introduction to conclusion

**IMPORTANT:** Output ONLY the article content in markdown format. Do not include any preamble, introduction about what you're doing, or closing remarks. Start directly with the article title/content and end with the conclusion."""

        # Call Claude API (using async to avoid blocking event loop)
        message = await client.messages.create(
            model="claude-sonnet-4-20250514",  # Claude Sonnet 4
            max_tokens=8000,
            temperature=0.7,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        # Extract article text
        article_draft = message.content[0].text

        word_count = len(article_draft.split())

        # Calculate cost (Claude Sonnet 4 pricing)
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        input_cost = (input_tokens / 1_000_000) * 3.0  # $3 per million input tokens
        output_cost = (output_tokens / 1_000_000) * 15.0  # $15 per million output tokens
        total_cost = input_cost + output_cost

        return {
            "content": [{
                "type": "text",
                "text": f"Successfully generated initial article draft!\n\nSource: {video_title}\nArticle length: {len(article_draft)} characters\nWord count: ~{word_count} words\n\n💰 Cost: ${total_cost:.4f} (Input: {input_tokens:,} tokens, Output: {output_tokens:,} tokens)"
            }],
            "article": article_draft,
            "word_count": word_count,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": total_cost,
            "success": True
        }

    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"Error generating article: {str(e)}"
            }],
            "isError": True,
            "success": False
        }


@tool(
    name="refine_article",
    description="Refine and improve the article by incorporating insights from additional video transcripts",
    input_schema={
        "current_article": str,
        "new_transcript": str,
        "article_prompt": str,
        "video_title": str,
        "channel_name": str,
        "iteration": int
    }
)
async def refine_article(args: dict[str, Any]) -> dict[str, Any]:
    """
    Improve article by integrating insights from additional videos.

    Args:
        current_article: The current article draft
        new_transcript: Transcript from the new video
        article_prompt: User's article writing instructions
        video_title: Title of the new video
        channel_name: Channel of the new video
        iteration: Which iteration (2 or 3)

    Returns:
        Dictionary with the refined article
    """
    try:
        current_article = args["current_article"]
        new_transcript = args["new_transcript"]
        article_prompt = args["article_prompt"]
        video_title = args["video_title"]
        channel_name = args["channel_name"]
        iteration = args.get("iteration", 2)

        # Construct refinement prompt
        system_prompt = """You are an expert content editor who excels at synthesizing information from multiple sources into cohesive, comprehensive articles. Think of yourself as an A+ student compiling comprehensive notes from multiple lectures on the same topic."""

        user_prompt = f"""You are refining an article by incorporating valuable insights from an additional video source.

**Current Article Draft:**
{current_article}

**New Source - Video {iteration}:**
- Title: {video_title}
- Channel: {channel_name}

**New Video Transcript:**
{new_transcript}

**Article Writing Guidelines:**
{article_prompt}

**Your Refinement Task:**
Carefully review the current article and analyze the new transcript. Then:

1. **Identify New Insights:** Find valuable information, perspectives, or examples in the new transcript that aren't fully covered in the current article
2. **Integrate Seamlessly:** Weave new insights into the existing article structure naturally
3. **Enhance Depth:** Add depth, nuance, and additional context where the new source provides value
4. **Maintain Voice:** Keep the original speaker's authentic voice and tone throughout
5. **Improve Flow:** Ensure smooth transitions and logical progression
6. **Add Sections if Needed:** Create new sections if the new source introduces important topics
7. **Remove Redundancy:** Eliminate repetitive information
8. **Strengthen Examples:** Add concrete examples or use cases from the new source
9. **Preserve Quality:** Maintain or improve the article's overall quality and readability

Think like an A+ student who attends multiple lectures on the same topic and creates comprehensive, well-organized notes that capture all the valuable insights.

**IMPORTANT:** Output ONLY the refined article content in markdown format. Do not include any preamble like "I'll help refine..." or "Here's the enhanced version". Do not include any closing remarks. Start directly with the article content and end with the conclusion."""

        # Call Claude API (using async to avoid blocking event loop)
        message = await client.messages.create(
            model="claude-sonnet-4-20250514",  # Claude Sonnet 4
            max_tokens=8000,
            temperature=0.7,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        # Extract refined article
        refined_article = message.content[0].text

        word_count = len(refined_article.split())

        # Calculate cost (Claude Sonnet 4 pricing)
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        input_cost = (input_tokens / 1_000_000) * 3.0  # $3 per million input tokens
        output_cost = (output_tokens / 1_000_000) * 15.0  # $15 per million output tokens
        total_cost = input_cost + output_cost

        return {
            "content": [{
                "type": "text",
                "text": f"Successfully refined article with insights from Video {iteration}!\n\nNew source: {video_title}\nRefined article length: {len(refined_article)} characters\nWord count: ~{word_count} words\n\n💰 Cost: ${total_cost:.4f} (Input: {input_tokens:,} tokens, Output: {output_tokens:,} tokens)"
            }],
            "article": refined_article,
            "word_count": word_count,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": total_cost,
            "success": True
        }

    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"Error refining article: {str(e)}"
            }],
            "isError": True,
            "success": False
        }
