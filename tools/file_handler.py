"""
File handling tools for reading inputs and saving outputs.
"""
import os
from typing import Any
from datetime import datetime
from claude_agent_sdk import tool


@tool(
    name="read_input_files",
    description="Read the topic and article prompt from input files (topic.txt and article_prompt.txt)",
    input_schema={}
)
async def read_input_files(args: dict[str, Any]) -> dict[str, Any]:
    """
    Read topic.txt and article_prompt.txt files.
    Returns the topic and article writing instructions.
    """
    try:
        # Define file paths relative to project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        topic_path = os.path.join(base_dir, 'topic.txt')
        prompt_path = os.path.join(base_dir, 'article_prompt.txt')

        # Read topic
        if not os.path.exists(topic_path):
            return {
                "content": [{
                    "type": "text",
                    "text": "Error: topic.txt not found. Please create this file with your search topic."
                }],
                "isError": True
            }

        with open(topic_path, 'r', encoding='utf-8') as f:
            topic = f.read().strip()

        if not topic or topic == "Your topic here":
            return {
                "content": [{
                    "type": "text",
                    "text": "Error: topic.txt is empty or contains placeholder text. Please add a valid topic."
                }],
                "isError": True
            }

        # Read article prompt
        if not os.path.exists(prompt_path):
            return {
                "content": [{
                    "type": "text",
                    "text": "Error: article_prompt.txt not found. Please create this file with writing instructions."
                }],
                "isError": True
            }

        with open(prompt_path, 'r', encoding='utf-8') as f:
            article_prompt = f.read().strip()

        if not article_prompt:
            return {
                "content": [{
                    "type": "text",
                    "text": "Error: article_prompt.txt is empty. Please add article writing instructions."
                }],
                "isError": True
            }

        # Success
        return {
            "content": [{
                "type": "text",
                "text": f"Successfully read input files:\n\nTopic: {topic}\n\nArticle Prompt Length: {len(article_prompt)} characters"
            }],
            "topic": topic,
            "article_prompt": article_prompt
        }

    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"Error reading input files: {str(e)}"
            }],
            "isError": True
        }


@tool(
    name="save_article",
    description="Save the article to output directory. Use is_draft=True for work-in-progress, False for final version with timestamped filename.",
    input_schema={
        "article": str,
        "video_sources": list,
        "topic": str,
        "total_cost": float,
        "total_input_tokens": int,
        "total_output_tokens": int,
        "is_draft": bool
    }
)
async def save_article(args: dict[str, Any]) -> dict[str, Any]:
    """
    Save the article with metadata footer.

    Args:
        article: The article content in markdown
        video_sources: List of video metadata dicts
        topic: The original search topic
        total_cost: Total cost of API calls
        total_input_tokens: Total input tokens used
        total_output_tokens: Total output tokens used
        is_draft: True for draft (article_draft.md), False for final (article_{topic}_{timestamp}.md)
    """
    try:
        # Validate required fields
        required_fields = ['article', 'video_sources', 'topic']
        for field in required_fields:
            if field not in args:
                return {
                    "content": [{
                        "type": "text",
                        "text": f"Error: Missing required field '{field}' in save_article call"
                    }],
                    "isError": True,
                    "success": False
                }

        article = args["article"]
        video_sources = args["video_sources"]
        topic = args["topic"]

        # Validate article is not empty
        if not article or not article.strip():
            return {
                "content": [{
                    "type": "text",
                    "text": "Error: Article content is empty"
                }],
                "isError": True,
                "success": False
            }

        # Validate video_sources is a list
        if not isinstance(video_sources, list):
            return {
                "content": [{
                    "type": "text",
                    "text": f"Error: video_sources must be a list, got {type(video_sources).__name__}"
                }],
                "isError": True,
                "success": False
            }

        # Validate video_sources is not empty
        if len(video_sources) == 0:
            return {
                "content": [{
                    "type": "text",
                    "text": "Warning: video_sources list is empty. Article will be saved without source metadata."
                }],
                "isError": False
            }

        # Optional fields with defaults
        total_cost = args.get("total_cost", 0.0)
        total_input_tokens = args.get("total_input_tokens", 0)
        total_output_tokens = args.get("total_output_tokens", 0)
        is_draft = args.get("is_draft", False)

        # Define output path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(base_dir, 'output')

        if is_draft:
            # Draft file: gets overwritten each run
            filename = 'article_draft.md'
            output_path = os.path.join(output_dir, filename)
        else:
            # Final file: includes topic name and timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            # Clean topic name for filename (remove special chars)
            clean_topic = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in topic)
            clean_topic = clean_topic.replace(' ', '_').lower()[:50]  # Limit length
            filename = f'article_{clean_topic}_{timestamp}.md'
            output_path = os.path.join(output_dir, filename)

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Build metadata footer
        metadata = "\n\n---\n\n"
        metadata += "## Article Metadata\n\n"
        metadata += f"**Topic:** {topic}\n\n"
        metadata += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        metadata += "**Sources:**\n\n"

        for i, video in enumerate(video_sources, 1):
            metadata += f"{i}. [{video.get('title', 'Unknown')}](https://www.youtube.com/watch?v={video.get('video_id', '')})\n"
            metadata += f"   - Channel: {video.get('channel', 'Unknown')}\n"
            metadata += f"   - Views: {video.get('views', 0):,}\n"
            metadata += f"   - Comments: {video.get('comments', 0):,}\n\n"

        # Add cost information
        if total_cost > 0:
            metadata += "**Cost Summary:**\n\n"
            metadata += f"- Total Input Tokens: {total_input_tokens:,}\n"
            metadata += f"- Total Output Tokens: {total_output_tokens:,}\n"
            metadata += f"- Total Tokens: {total_input_tokens + total_output_tokens:,}\n"
            metadata += f"- **Total Cost: ${total_cost:.4f}**\n"
            metadata += f"- Model: Claude Sonnet 4\n\n"

        # Combine article and metadata
        full_content = article + metadata

        # Save to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        save_type = "draft" if is_draft else "final"
        return {
            "content": [{
                "type": "text",
                "text": f"Article successfully saved ({save_type}): {output_path}\n\nTotal length: {len(article)} characters\nSources included: {len(video_sources)} videos"
            }],
            "file_path": output_path,
            "is_draft": is_draft,
            "success": True
        }

    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"Error saving article: {str(e)}"
            }],
            "isError": True,
            "success": False
        }
