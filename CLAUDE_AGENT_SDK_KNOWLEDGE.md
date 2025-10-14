# Claude Agent SDK - Complete Knowledge Base

## Overview

The Claude Agent SDK enables developers to create autonomous agents by giving Claude access to a computer where it can write files, run commands, and iterate on work.

**Key Resources:**
- Blog: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- Docs: https://docs.claude.com/en/api/agent-sdk/overview
- Python SDK: https://docs.claude.com/en/api/agent-sdk/python
- GitHub: https://github.com/anthropics/claude-agent-sdk-python

---

## Installation

### Prerequisites
- Python 3.10+
- Node.js
- Claude Code 2.0.0+

### Install Command
```bash
pip install claude-agent-sdk
```

### Verify Installation
```bash
pip show claude-agent-sdk
```

**Expected Output:**
- Name: claude-agent-sdk
- Version: 0.1.0
- Requires: anyio, mcp, typing-extensions

---

## The Agent Loop Framework

Every agent follows this cycle:

1. **Gather Context** - Understand what needs to be done
2. **Take Action** - Execute the task
3. **Verify Work** - Check if the output is correct
4. **Repeat** - Continue until the task is complete

---

## Context Gathering Strategies

### 1. Agentic Search (Primary Method)
- Use file system exploration and bash commands
- Let the agent navigate and discover relevant information
- Most effective for broad searches

### 2. Semantic Search (Secondary Method)
- Vector-based concept retrieval
- Good as supplementary method
- Helps find conceptually similar content

### 3. Subagents
- Run parallel tasks with isolated context windows
- Useful for complex, multi-faceted problems
- Each subagent focuses on a specific subtask

### 4. Compaction
- Automatically summarize conversation history
- Manages context window limits
- Keeps the agent efficient over long sessions

---

## Action Taking Methods

### 1. Tools (Primary Building Blocks)
- Design custom tools for your agent's specific needs
- Define clear interfaces and parameters
- Most structured way to enable capabilities

### 2. Bash & Scripts
- Flexible execution of computer-based tasks
- Run system commands directly
- Good for ad-hoc operations

### 3. Code Generation
- Create precise, reusable scripts
- Better for repeatable workflows
- More maintainable than ad-hoc commands

### 4. Model Context Protocol (MCP)
- Standardized way to integrate external services
- Connect to APIs, databases, and tools
- Reusable across different agents

---

## Work Verification Approaches

### 1. Defining Rules
- Establish clear output criteria upfront
- Set expectations for what "done" looks like
- Easiest to implement

### 2. Visual Feedback
- Take screenshots of generated content
- Analyze visual output programmatically
- Essential for UI/UX tasks

### 3. LLM Judging
- Use another language model to evaluate output
- Good for subjective quality assessment
- Can catch nuanced issues

---

## Python SDK API Reference

### 1. Simple Query (Stateless)

Use for single interactions without conversation history.

```python
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="What is 2 + 2?"):
        print(message)

anyio.run(main)
```

### 2. ClaudeSDKClient (Stateful Sessions)

Use for maintaining conversation context across multiple exchanges.

```python
import anyio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a helpful coding assistant"
    )

    async with ClaudeSDKClient(options) as client:
        # First query
        await client.query("Analyze this code")
        async for message in client.receive_response():
            print(message)

        # Follow-up query (maintains context)
        await client.query("Now optimize it")
        async for message in client.receive_response():
            print(message)

anyio.run(main)
```

### 3. Custom Tools

Define custom capabilities for your agent using the `@tool` decorator.

```python
from claude_agent_sdk import tool
from typing import Any

@tool(
    name="greet",
    description="Greet a user by name",
    input_schema={"name": str}
)
async def greet(args: dict[str, Any]) -> dict[str, Any]:
    return {
        "content": [{
            "type": "text",
            "text": f"Hello, {args['name']}!"
        }]
    }

# Use with query
async for message in query(
    prompt="Greet John",
    options=ClaudeAgentOptions(tools=[greet])
):
    print(message)
```

### 4. Configuration Options

```python
from claude_agent_sdk import ClaudeAgentOptions

options = ClaudeAgentOptions(
    # Control which tools the agent can use
    allowed_tools=["read", "write", "bash"],

    # Customize agent behavior
    system_prompt="You are a helpful assistant",

    # Set maximum conversation turns
    max_turns=10,

    # Define tool execution permissions
    permission_mode="auto",  # or "manual"

    # Add custom tools
    tools=[greet, another_tool],

    # Intercept and modify behavior
    hooks={
        "pre_tool": my_pre_tool_hook,
        "post_tool": my_post_tool_hook
    }
)
```

### 5. Error Handling

```python
from claude_agent_sdk import CLINotFoundError, ProcessError

try:
    async for message in query(prompt="Hello"):
        print(message)
except CLINotFoundError:
    print("Claude Code CLI not installed")
except ProcessError as e:
    print(f"Process failed with exit code: {e.exit_code}")
```

### 6. MCP Server Creation

Create an in-process MCP server with custom tools.

```python
from claude_agent_sdk import create_sdk_mcp_server

# Create server with your tools
server = create_sdk_mcp_server(tools=[greet, calculate, search])

# Use the server in your agent configuration
options = ClaudeAgentOptions(mcp_server=server)
```

### 7. Hooks

Intercept and modify agent behavior at different stages.

```python
async def pre_tool_logger(input_data, tool_use_id, context):
    tool_name = input_data.get("name")
    print(f"About to execute tool: {tool_name}")
    return input_data  # Must return input_data

async def post_tool_validator(output_data, tool_use_id, context):
    print(f"Tool completed: {output_data}")
    return output_data  # Must return output_data

options = ClaudeAgentOptions(
    hooks={
        "pre_tool": pre_tool_logger,
        "post_tool": post_tool_validator
    }
)
```

---

## Complete Example: File Analyzer Agent

```python
import anyio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, tool
from typing import Any
import os

@tool(
    name="count_files",
    description="Count files in a directory",
    input_schema={"directory": str}
)
async def count_files(args: dict[str, Any]) -> dict[str, Any]:
    directory = args["directory"]
    try:
        file_count = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
        return {
            "content": [{
                "type": "text",
                "text": f"Found {file_count} files in {directory}"
            }]
        }
    except Exception as e:
        return {
            "content": [{
                "type": "text",
                "text": f"Error: {str(e)}"
            }]
        }

async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a file system analyzer",
        tools=[count_files],
        permission_mode="auto"
    )

    async with ClaudeSDKClient(options) as client:
        await client.query("How many files are in the current directory?")
        async for message in client.receive_response():
            print(message)

if __name__ == "__main__":
    anyio.run(main)
```

---

## Best Practices

### Context Gathering
✓ Start with agentic search as your primary strategy
✓ Use semantic search as a supplementary method
✓ Implement subagents for parallel processing of complex tasks
✓ Enable compaction for long-running conversations

### Tool Design
✓ Keep tool interfaces simple and clear
✓ Provide detailed descriptions for each tool
✓ Use strict input schemas with type hints
✓ Return consistent output formats
✓ Handle errors gracefully within tools

### Agent Configuration
✓ Set appropriate `max_turns` to prevent infinite loops
✓ Use `permission_mode="manual"` for sensitive operations
✓ Implement pre/post hooks for logging and validation
✓ Test with representative evaluation sets

### Verification
✓ Define clear success criteria upfront
✓ Implement automated checks where possible
✓ Use LLM judging for subjective quality assessment
✓ Create feedback loops for iterative improvement

---

## Agent Types You Can Build

### 1. Finance Agents
- Analyze financial data
- Generate reports
- Perform calculations
- Track budgets

### 2. Personal Assistant Agents
- Manage tasks and schedules
- Send notifications
- Organize files
- Automate workflows

### 3. Customer Support Agents
- Answer common questions
- Route inquiries
- Provide troubleshooting
- Escalate issues

### 4. Deep Research Agents
- Gather information from multiple sources
- Synthesize findings
- Generate summaries
- Create reports

### 5. Coding Agents
- SRE automation bots
- Security review tools
- Code analysis
- Deployment automation

### 6. Business Agents
- Legal document assistants
- Contract review
- Data processing
- Report generation

---

## Implementation Workflow

### Step 1: Define Purpose
- What problem will the agent solve?
- What are the success criteria?
- What tools/resources does it need?

### Step 2: Design Context Strategy
- How will the agent gather information?
- Does it need semantic search?
- Will it use subagents?

### Step 3: Create Tools
- What custom capabilities are needed?
- What external services to integrate?
- How to handle errors?

### Step 4: Implement Verification
- How will the agent check its work?
- What are the quality criteria?
- Who validates the output?

### Step 5: Test and Iterate
- Create test cases
- Run on real-world scenarios
- Measure performance
- Refine based on results

---

## Common Patterns

### Pattern 1: Simple Query Agent
```python
async for message in query(prompt="Analyze this log file"):
    print(message)
```

### Pattern 2: Stateful Conversation Agent
```python
async with ClaudeSDKClient(options) as client:
    await client.query("First question")
    async for msg in client.receive_response():
        print(msg)
    await client.query("Follow-up")
    async for msg in client.receive_response():
        print(msg)
```

### Pattern 3: Tool-Based Agent
```python
@tool("my_tool", "description", {"param": str})
async def my_tool(args):
    return {"content": [{"type": "text", "text": "result"}]}

async for message in query(
    prompt="Use my tool",
    options=ClaudeAgentOptions(tools=[my_tool])
):
    print(message)
```

### Pattern 4: Supervised Agent
```python
options = ClaudeAgentOptions(
    permission_mode="manual",
    hooks={"pre_tool": approval_hook}
)
```

---

## Troubleshooting

### Issue: CLINotFoundError
**Solution:** Install Claude Code 2.0.0+ and ensure it's in your PATH

### Issue: Tool not being called
**Solution:**
- Check tool description is clear
- Verify input_schema matches expectations
- Ensure tool is included in `options.tools`

### Issue: Context limit exceeded
**Solution:**
- Enable compaction in options
- Reduce `max_turns`
- Use subagents to isolate context

### Issue: Permission denied
**Solution:**
- Check `permission_mode` setting
- Implement custom permission hooks
- Review `allowed_tools` configuration

---

## Quick Start Checklist

- [ ] Install Python 3.10+
- [ ] Install Node.js
- [ ] Install Claude Code CLI
- [ ] Run `pip install claude-agent-sdk`
- [ ] Verify installation with `pip show claude-agent-sdk`
- [ ] Create a simple test agent
- [ ] Test with basic query
- [ ] Add custom tools
- [ ] Implement error handling
- [ ] Test with real use case

---

## Additional Resources

- **Anthropic API Docs:** https://docs.anthropic.com
- **Claude Agent SDK Overview:** https://docs.claude.com/en/api/agent-sdk/overview
- **Python SDK Reference:** https://docs.claude.com/en/api/agent-sdk/python
- **GitHub Repository:** https://github.com/anthropics/claude-agent-sdk-python
- **MCP Specification:** https://modelcontextprotocol.io

---

## Environment Notes

**Current Setup:**
- Location: `C:\Claude Agent SDK\`
- Python Version: 3.10
- SDK Version: 0.1.0
- Dependencies: anyio, mcp, typing-extensions

**Existing API Keys:**
- ANTHROPIC_API_KEY (set as environment variable)

---

Last Updated: October 13, 2025
