import asyncio
import uvicorn
from fastmcp import FastMCP

mcp = FastMCP(name="dev server")

# ---------------------------------------------------
# 1️⃣ AI Experiment Tracking Tool
# ---------------------------------------------------
@mcp.tool
async def ai_experiment_log(model_type: str) -> str:
    """Return AI experiment tracking template"""
    await asyncio.sleep(0)  # yield control (replace with real async I/O if needed)
    return f"""
Create AI experiment tracking sheet

Model type: {model_type}

Fields:
- Experiment name
- Dataset
- Features used
- Hyperparameters
- Training time
- Metrics (accuracy, f1, BLEU, etc)
- Observations
- Challenges
- Next steps
"""

# ---------------------------------------------------
# 2️⃣ Prompt Engineering Template
# ---------------------------------------------------
@mcp.tool
async def prompt_engineering(task: str) -> str:
    """Return structured prompt template"""
    await asyncio.sleep(0)
    return f"""
Create structured prompt for task: {task}

Sections:
- Role
- Objective
- Context
- Instructions
- Examples
- Constraints
- Output format
"""

# ---------------------------------------------------
# 3️⃣ Code Review Checklist Tool
# ---------------------------------------------------
@mcp.tool
async def code_review_template(language: str) -> str:
    """Return code review template"""
    await asyncio.sleep(0)
    return f"""
Review {language} code

Checklist:
- Readability
- Modularity
- Performance
- Scalability
- Security
- Error handling
- Logging
- Testing coverage
- Optimization suggestions
- Refactored code suggestion
"""

# ---------------------------------------------------
# 4️⃣ Dummy Data Generator Tool
# ---------------------------------------------------
@mcp.tool
async def dummy_data_template(use_case: str, rows: int) -> str:
    """Return dummy data creation template"""
    await asyncio.sleep(0)
    return f"""
Create dummy data

Use case: {use_case}
Rows: {rows}

Ask user:
- Column names
- Column data types
- Structured / unstructured
- Database compatibility
- Date range (optional)
- Output format (CSV / Excel / JSON)

Include:
- Data generation logic
- Edge cases
- Null handling
"""

# ---------------------------------------------------
# 5️⃣ Open-source Model Research Tool
# ---------------------------------------------------
@mcp.tool
async def opensource_model_research(task: str) -> str:
    """Return open-source model research template"""
    await asyncio.sleep(0)
    return f"""
Research open-source models for task: {task}

Include:
- HuggingFace models
- Model size & variants
- Parameter count
- Latency & speed
- Tool calling ability
- Agent compatibility
- Code usage example
- Optimization methods
- Benchmark comparison
- Paid API alternatives
"""

# ---------------------------------------------------
# 6️⃣ LinkedIn Post Generator Tool
# ---------------------------------------------------
@mcp.tool
async def linkedin_post(topic: str) -> str:
    """Return LinkedIn post template"""
    await asyncio.sleep(0)
    return f"""
Create LinkedIn post on topic: {topic}

Include:
- Hook
- Insight
- Real-world impact
- Key learnings
- Call to action
- Hashtags
- Visual suggestion
"""

# ---------------------------------------------------
# 7️⃣ Instagram Post Generator Tool
# ---------------------------------------------------
@mcp.tool
async def instagram_post(topic: str) -> str:
    """Return Instagram post template"""
    await asyncio.sleep(0)
    return f"""
Create Instagram post on topic: {topic}

Include:
- Caption
- Carousel idea
- Visual diagram suggestion
- Short insights
- Hashtags
- CTA
"""

# ---------------------------------------------------
# 8️⃣ Research Insight Tool
# ---------------------------------------------------
@mcp.tool
async def research_insights(topic: str) -> str:
    """Return research analysis template"""
    await asyncio.sleep(0)
    return f"""
Research latest innovations on topic: {topic}

Include:
- Market trends
- Research papers
- Innovations
- Industry use cases
- Business impact
- Future opportunities
"""

# ---------------- RUN REMOTE MCP ----------------

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8002)
