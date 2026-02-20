from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "http://127.0.0.1:8001/mcp", # provide your deployed cloud server url
    name="office server proxy"
)

if __name__=="__main__":
    mcp.run()