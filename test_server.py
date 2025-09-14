import asyncio
import httpx
import server

def test_ping_tool():
    res = asyncio.run(server.ping.run({}))
    assert res.content[0].text == "pong"

def test_github_zen_tool():
    res = asyncio.run(server.github_zen.run({}))
    assert isinstance(res.content[0].text, str)
    assert res.content[0].text


def test_process_gics_tool(monkeypatch):
    sample_csv = "code,sector\n10,Energy\n15,Materials\n"

    def mock_get(url, timeout):
        request = httpx.Request("GET", url)
        return httpx.Response(200, text=sample_csv, request=request)

    monkeypatch.setattr(server.httpx, "get", mock_get)

    res = asyncio.run(server.process_gics.run({"url": "http://example.com/gics.csv"}))
    assert res.content[0].text == "Processed 2 GICS records"

