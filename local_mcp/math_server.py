from fastmcp import FastMCP
from app import app

# Wrap FastAPI → MCP
mcp = FastMCP.from_fastapi(
    app=app,
    name="math server",
)

if __name__ == "__main__":
    mcp.run()