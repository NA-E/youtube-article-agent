"""
Cost tracking utility for Claude API usage.
"""
import os
from typing import Any
from claude_agent_sdk import tool


# Global cost tracker
cost_data = {
    "total_input_tokens": 0,
    "total_output_tokens": 0,
    "total_cost": 0.0,
    "api_calls": 0
}


@tool(
    name="track_cost",
    description="Track cumulative cost of Claude API calls",
    input_schema={
        "input_tokens": int,
        "output_tokens": int,
        "cost": float,
        "operation": str
    }
)
async def track_cost(args: dict[str, Any]) -> dict[str, Any]:
    """
    Track and accumulate costs from Claude API calls.

    Args:
        input_tokens: Number of input tokens used
        output_tokens: Number of output tokens used
        cost: Cost of this API call
        operation: Description of the operation
    """
    global cost_data

    cost_data["total_input_tokens"] += args["input_tokens"]
    cost_data["total_output_tokens"] += args["output_tokens"]
    cost_data["total_cost"] += args["cost"]
    cost_data["api_calls"] += 1

    return {
        "content": [{
            "type": "text",
            "text": f"Cost tracked for {args['operation']}: ${args['cost']:.4f}\n\nRunning total: ${cost_data['total_cost']:.4f} ({cost_data['api_calls']} API calls)"
        }],
        "success": True
    }


@tool(
    name="get_total_cost",
    description="Get the total accumulated cost of all Claude API calls",
    input_schema={}
)
async def get_total_cost(args: dict[str, Any]) -> dict[str, Any]:
    """
    Return the total cost summary.
    """
    global cost_data

    summary = f"""
╔════════════════════════════════════════════╗
║         COST SUMMARY - FINAL REPORT        ║
╚════════════════════════════════════════════╝

📊 API Usage Statistics:
   • Total API Calls: {cost_data['api_calls']}
   • Input Tokens: {cost_data['total_input_tokens']:,}
   • Output Tokens: {cost_data['total_output_tokens']:,}
   • Total Tokens: {cost_data['total_input_tokens'] + cost_data['total_output_tokens']:,}

💰 Cost Breakdown:
   • Input Cost:  ${(cost_data['total_input_tokens'] / 1_000_000) * 3.0:.4f} (@$3/M tokens)
   • Output Cost: ${(cost_data['total_output_tokens'] / 1_000_000) * 15.0:.4f} (@$15/M tokens)

💵 TOTAL COST: ${cost_data['total_cost']:.4f}

Model: Claude Sonnet 4 (claude-sonnet-4-20250514)
"""

    return {
        "content": [{
            "type": "text",
            "text": summary
        }],
        "total_cost": cost_data["total_cost"],
        "total_input_tokens": cost_data["total_input_tokens"],
        "total_output_tokens": cost_data["total_output_tokens"],
        "api_calls": cost_data["api_calls"],
        "success": True
    }


def reset_cost_tracking():
    """Reset cost tracking for a new run."""
    global cost_data
    cost_data = {
        "total_input_tokens": 0,
        "total_output_tokens": 0,
        "total_cost": 0.0,
        "api_calls": 0
    }
