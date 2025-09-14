from __future__ import annotations

import csv
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


@server.tool()
def process_gics(url: str) -> str:
    """Fetch a GICS CSV file from the provided URL and report the number of records."""
    response = httpx.get(url, timeout=10)
    response.raise_for_status()

    reader = csv.reader(response.text.splitlines())
    rows = list(reader)
    num_records = len(rows) - 1 if rows else 0

    return f"Processed {num_records} GICS records"


if __name__ == "__main__":
    server.run(transport="streamable-http")
