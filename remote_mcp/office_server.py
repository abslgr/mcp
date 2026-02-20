from fastmcp import FastMCP
import asyncio
import json

mcp = FastMCP(name="Office Productivity Server")

# ---------------- MEETING TOOLS ----------------

@mcp.tool
async def generate_meeting_agenda(topic: str, participants: str) -> str:
    """Generate a structured meeting agenda"""
    await asyncio.sleep(0)  # ✅ yields control to event loop
    return f"""
Create a meeting agenda
Topic: {topic}
Participants: {participants}
Sections:
1. Meeting objective
2. Key discussion points
3. Decisions to be made
4. Risks / blockers
5. Action items
""".strip()


@mcp.tool
async def generate_meeting_minutes(summary: str) -> str:
    """Generate meeting minutes from a summary"""
    await asyncio.sleep(0)
    return f"""
Create meeting minutes from summary
Summary:
{summary}
Sections:
1. Attendees
2. Discussion summary
3. Decisions taken
4. Action items
5. Next steps
""".strip()


@mcp.tool
async def extract_action_items(transcript: str) -> str:
    """Extract action items from a meeting transcript"""
    await asyncio.sleep(0)
    return f"""
Extract action items from transcript:
Transcript:
{transcript}
Return:
- Task
- Owner
- Deadline
""".strip()


# ---------------- PRODUCT / AI PROJECT TOOLS ----------------

@mcp.tool
async def generate_prd(product_name: str, description: str) -> str:
    """Generate a Product Requirement Document"""
    await asyncio.sleep(0)
    return f"""
Create a Product Requirement Document
Product: {product_name}
Description: {description}
Sections:
1. Overview
2. Problem statement
3. Goals & success metrics
4. Target users
5. Features
6. User stories
7. Architecture overview
8. Risks
9. Timeline
""".strip()


@mcp.tool
async def generate_user_stories(feature: str) -> str:
    """Generate user stories for a feature"""
    await asyncio.sleep(0)
    return f"""
Create user stories for feature: {feature}
Format:
As a [user]
I want [goal]
So that [benefit]
Also include acceptance criteria.
""".strip()


@mcp.tool
async def generate_test_cases(feature: str) -> str:
    """Generate test cases for a feature"""
    await asyncio.sleep(0)
    return f"""
Create test cases for feature: {feature}
Columns:
- Test case ID
- Scenario
- Steps
- Expected result
- Status
""".strip()


# ---------------- ARCHITECTURE TOOLS ----------------

@mcp.tool
async def architecture_design(system_name: str, requirements: str) -> str:
    """Design system architecture"""
    await asyncio.sleep(0)
    return f"""
Design system architecture
System: {system_name}
Requirements: {requirements}
Include:
1. Components
2. Data flow
3. Tech stack
4. Scalability strategy
5. Security considerations
""".strip()


@mcp.tool
async def diagram_description(system_name: str) -> str:
    """Generate architecture diagram description"""
    await asyncio.sleep(0)
    return f"""
Create architecture diagram description for {system_name}
Return:
- Components
- Connections
- Data flow
- Suggested diagram (Mermaid / Draw.io)
""".strip()


# ---------------- PPT TOOLS ----------------

@mcp.tool
async def ppt_outline(topic: str, audience: str) -> str:
    """Generate a PowerPoint presentation outline"""
    await asyncio.sleep(0)
    return f"""
Create PPT outline
Topic: {topic}
Audience: {audience}
Slides:
1. Title
2. Problem
3. Solution
4. Features
5. Architecture
6. Demo
7. Roadmap
8. Q&A
""".strip()


# ---------------- DOCUMENTATION TOOLS ----------------

@mcp.tool
async def readme_generator(project: str) -> str:
    """Generate a README file for a project"""
    await asyncio.sleep(0)
    return f"""
Create README for project: {project}
Sections:
1. Overview
2. Features
3. Tech stack
4. Installation
5. Usage
6. API
7. Contributing
""".strip()


@mcp.tool
async def proposal_generator(idea: str) -> str:
    """Generate a project proposal"""
    await asyncio.sleep(0)
    return f"""
Create proposal for idea: {idea}
Sections:
1. Background
2. Problem
3. Proposed solution
4. Benefits
5. Timeline
6. Cost estimate
""".strip()


# ---------------- RESOURCE ----------------

@mcp.resource("info://server")
async def server_info() -> str:
    """Return server metadata"""
    await asyncio.sleep(0)
    return json.dumps({
        "name": "Office Productivity MCP",
        "version": "1.0",
        "description": "Templates for meetings, PRD, architecture, PPT, and documentation",
        "tools": 11
    }, indent=2)


# ---------------- RUN REMOTE MCP ----------------

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8001)