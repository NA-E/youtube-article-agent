# YouTube to Article Writer Agent

An autonomous agent built with Claude Agent SDK that searches YouTube for videos on any topic, extracts transcripts, and generates comprehensive articles by synthesizing insights from multiple sources.

## Implementation Status

**Status:** Fully implemented and ready to use!

All core components have been implemented:
- 6 custom tools for autonomous workflow
- Main agent with stateful conversation loop
- Error handling and retry logic
- Logging system
- Complete project structure

## Quick Start

### 1. Install Dependencies

Dependencies are already installed! If you need to reinstall:

```bash
cd "C:\Claude Agent SDK\youtube-article-agent"
pip install -r requirements.txt
```

### 2. Configure API Keys

**YouTube API Key (Required):**
1. Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Create a project (if you don't have one)
3. Enable "YouTube Data API v3"
4. Create an API key (Credentials → Create Credentials → API Key)
5. Add the key to `.env` file:

```bash
YOUTUBE_API_KEY=your_actual_api_key_here
```

**Anthropic API Key:**
- Already set in your system environment variables

### 3. Populate Input Files

**topic.txt** - Add your search topic:
```
How to build scalable microservices architecture
```

**article_prompt.txt** - Define your article style:
```
Target Audience: Software engineers and technical leads

Writing Style:
- Conversational but professional tone
- Use technical terminology when appropriate
- Include practical examples and use cases
- Break down complex concepts into digestible sections

Structure:
- Introduction (hook + overview)
- Main content (3-5 key sections)
- Practical takeaways
- Conclusion with call-to-action

Length: 1500-2000 words

Voice: Third person, authoritative but approachable

Additional Requirements:
- Use headings and subheadings
- Include bullet points for lists
- Add code snippets if relevant
- Emphasize actionable insights
```

### 4. Run the Agent

```bash
cd "C:\Claude Agent SDK\youtube-article-agent"
python agent.py
```

The agent will:
1. Read your topic and article writing instructions
2. Search YouTube for the top 3 most engaging videos (sorted by comments, then views)
3. Extract English transcripts from each video
4. Generate an initial article draft from the first video
5. Refine the article by incorporating insights from videos 2 and 3
6. Save the final article to `output/article.md`

## Project Structure

```
youtube-article-agent/
├── agent.py                         # Main agent implementation
├── tools/                           # Custom tools directory
│   ├── __init__.py                 # Tools package
│   ├── file_handler.py             # Read inputs & save outputs
│   ├── youtube_search.py           # YouTube search via API
│   ├── transcript_fetcher.py       # Extract transcripts
│   └── article_generator.py        # Generate & refine articles
├── topic.txt                        # INPUT: Your search topic
├── article_prompt.txt               # INPUT: Writing style instructions
├── .env                             # API keys configuration
├── output/
│   └── article.md                   # OUTPUT: Final article
├── logs/
│   └── agent_log.txt                # Execution logs
├── requirements.txt                 # Python dependencies
├── plan.md                          # Implementation plan
├── CLAUDE_AGENT_SDK_KNOWLEDGE.md    # SDK reference guide
└── README.md                        # This file
```

## How It Works

### Autonomous Workflow

The agent operates autonomously through these steps:

1. **Context Gathering**
   - Reads topic from `topic.txt`
   - Reads article writing instructions from `article_prompt.txt`

2. **Video Discovery**
   - Searches YouTube for videos with captions
   - Filters by relevance language (English)
   - Retrieves video metadata (views, comments, likes)
   - Sorts by engagement: comments first, then views
   - Returns top 3 videos

3. **Transcript Extraction**
   - Attempts to extract English transcript for each video
   - Handles multiple English variants (en, en-US, en-GB)
   - Falls back to auto-generated transcripts if needed
   - Gracefully skips videos without transcripts

4. **Article Generation**
   - **Video 1:** Generates initial article draft using Claude 3.5 Haiku
   - **Video 2:** Refines article by integrating new insights
   - **Video 3:** Final refinement pass for comprehensive coverage

5. **Output & Metadata**
   - Saves polished article to `output/article.md`
   - Adds metadata footer with video sources, timestamps, and statistics
   - Logs execution details to `logs/agent_log.txt`

### Key Features

- **Autonomous Operation:** Runs end-to-end without human intervention
- **Robust Error Handling:** Skips videos without transcripts, continues with available ones
- **Multi-Source Synthesis:** Combines insights from multiple videos like an A+ student compiling lecture notes
- **Voice Preservation:** Maintains the speaker's authentic voice throughout
- **Customizable Style:** Follows your specific article writing instructions
- **Comprehensive Logging:** Tracks all operations with timestamps

## Tools Implementation

### 1. read_input_files
- **Purpose:** Read topic and article prompt from input files
- **Validation:** Checks for empty files and placeholder text
- **Error Handling:** Returns clear error messages if files missing or invalid

### 2. search_youtube
- **Purpose:** Search YouTube and return top 3 videos by engagement
- **Sorting:** Comments (descending) → Views (descending)
- **Filters:** Only videos with captions, English language
- **Error Handling:** Handles quota exceeded, invalid API key, network errors

### 3. get_transcript
- **Purpose:** Extract English transcript from YouTube video
- **Library:** Uses `youtube-transcript-api` (free, no API key needed)
- **Languages:** Supports en, en-US, en-GB variants
- **Error Handling:** Gracefully handles disabled transcripts, unavailable videos, rate limits

### 4. generate_initial_article
- **Purpose:** Create first draft from Video 1 transcript
- **Model:** Claude 3.5 Haiku (fast and cost-effective)
- **Approach:** Captures speaker's voice and key insights
- **Output:** Markdown-formatted article

### 5. refine_article
- **Purpose:** Improve article by integrating additional video insights
- **Strategy:** A+ student approach - compiles comprehensive notes from multiple lectures
- **Iterations:** Used for Video 2 and Video 3
- **Focus:** Adds depth, maintains voice, removes redundancy

### 6. save_article
- **Purpose:** Save final article with metadata
- **Metadata:** Video sources, generation date, statistics
- **Format:** Markdown with clickable YouTube links
- **Location:** `output/article.md`

## Cost Breakdown

**Per Article Execution:**
- YouTube API: $0 (within free tier, 10,000 units/day)
- Transcript Extraction: $0 (free library)
- Claude API (3 calls): ~$0.03
- **Total: ~$0.03 per article**

**Claude 3.5 Haiku Pricing:**
- Input: $0.25 per million tokens
- Output: $1.25 per million tokens

## Troubleshooting

### YouTube API Issues

**Error: "YOUTUBE_API_KEY not set"**
- Solution: Add your API key to `.env` file

**Error: "quotaExceeded"**
- Cause: Daily quota of 10,000 units exceeded
- Solution: Wait 24 hours for quota reset (resets at midnight Pacific Time)

**Error: "keyInvalid"**
- Solution: Check that your API key is correct and YouTube Data API v3 is enabled

### Transcript Extraction Issues

**"No English transcript found"**
- This is normal - some videos don't have captions
- The agent will automatically skip to the next video

**"Transcripts are disabled"**
- Creator disabled captions on the video
- Agent skips to next video automatically

### Article Generation Issues

**"Error generating article"**
- Check that ANTHROPIC_API_KEY is set in environment
- Verify you have sufficient API credits
- Check logs for detailed error message

### General Issues

**No output file created**
- Check `logs/agent_log.txt` for errors
- Ensure at least one video had a transcript
- Verify all input files are properly populated

**Article quality is poor**
- Refine your `article_prompt.txt` instructions
- Try a different topic with more established content
- Ensure videos have good transcript quality

## Advanced Usage

### Custom Model Selection

Edit `tools/article_generator.py` to change the Claude model:

```python
# Current: Claude 3.5 Haiku (fast, cheap)
model="claude-3-5-haiku-20241022"

# Alternative: Claude 3.5 Sonnet (higher quality)
model="claude-3-5-sonnet-20241022"
```

### Adjusting Video Count

Edit `tools/youtube_search.py` to change search results:

```python
# Line 66: Increase for more options
maxResults=20  # Get more candidates before sorting

# Line 129: Change top videos count
top_videos = videos[:3]  # Change to [:5] for top 5
```

### Custom Logging

Edit `agent.py` to customize logging behavior:

```python
# Line 30: Change log level
def log(message: str, level: str = "INFO"):

# Add more detailed logging as needed
```

## Example Output

After running the agent, you'll find an article like this in `output/article.md`:

```markdown
# How to Build Scalable Microservices Architecture

## Introduction
[Article content synthesized from multiple videos...]

## Key Principles
[Main insights...]

## Practical Implementation
[Examples and use cases...]

---

## Article Metadata

**Topic:** How to build scalable microservices architecture

**Generated:** 2025-10-13 14:30:00

**Sources:**

1. [Microservices Architecture Explained](https://www.youtube.com/watch?v=...)
   - Channel: Tech Channel
   - Views: 1,250,000
   - Comments: 3,450

2. [Building Microservices at Scale](https://www.youtube.com/watch?v=...)
   - Channel: Cloud Expert
   - Views: 850,000
   - Comments: 2,100

3. [Microservices Best Practices](https://www.youtube.com/watch?v=...)
   - Channel: DevOps Pro
   - Views: 600,000
   - Comments: 1,800
```

## Next Steps

1. **Get your YouTube API key** (see Quick Start section)
2. **Add your topic** to `topic.txt`
3. **Customize** `article_prompt.txt` with your style preferences
4. **Run the agent:** `python agent.py`
5. **Review the output** in `output/article.md`

## Future Enhancements

Potential improvements to consider:
- Multi-language support
- HTML/PDF export formats
- Batch processing (multiple topics)
- SEO optimization
- Fact-checking against transcripts
- Image/screenshot generation
- Medium/Substack formatting
- Email newsletter format

## Support

For issues or questions:
- Check `logs/agent_log.txt` for detailed execution logs
- Review Claude Agent SDK docs: https://docs.claude.com/en/api/agent-sdk/overview
- Refer to `CLAUDE_AGENT_SDK_KNOWLEDGE.md` for SDK patterns

---

Built with Claude Agent SDK | Last updated: 2025-10-13
