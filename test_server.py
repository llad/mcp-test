import os
import importlib

# Ensure environment variable is set before importing server
os.environ["MCP_API_KEY"] = "test-key"

import server
importlib.reload(server)


def test_ping_with_api_key():
    app = server.app.test_client()
    res = app.get("/ping", headers={"X-API-Key": "test-key"})
    assert res.status_code == 200
    assert res.get_json() == {"message": "pong"}


def test_ping_without_api_key():
    app = server.app.test_client()
    res = app.get("/ping")
    assert res.status_code == 401
