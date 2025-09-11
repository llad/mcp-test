import asyncio
import server

def test_ping_tool():
    res = asyncio.run(server.ping.run({}))
    assert res.content[0].text == "pong"

def test_github_zen_tool():
    res = asyncio.run(server.github_zen.run({}))
    assert isinstance(res.content[0].text, str)
    assert res.content[0].text

