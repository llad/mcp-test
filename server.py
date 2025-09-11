from __future__ import annotations

import httpx
from fastmcp import FastMCP

server = FastMCP()


@server.tool()
def ping() -> str:
    """Return a simple pong response."""
    return "pong"


@server.tool()
def github_zen() -> str:
    """Fetch a random message from the GitHub Zen API."""
    response = httpx.get("https://api.github.com/zen", timeout=10)
    response.raise_for_status()
    return response.text.strip()


if __name__ == "__main__":
    server.run()
