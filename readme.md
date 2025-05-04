# 📺 YouTube MCP Server

A FastMCP-powered API server that fetches the top YouTube videos for any given search query, sorted by view count. This server uses the YouTube Data API v3 and is built to plug into any AI or automation pipeline requiring popular video content insights.

## 🚀 Features

- Search YouTube for videos using a keyword
- Returns `videoId`, `title`, and `viewCount` for each result
- Fetches up to 100 videos per query (adjustable)
- Built with [FastMCP](https://github.com/ai-compound/fastmcp) for LLM/agent-friendly usage

---

## 🔧 Requirements

- Python 3.8+
- YouTube Data API Key
- `fastmcp`, `google-api-python-client`

### 📦 Install dependencies

```bash
pip install fastmcp google-api-python-client
```
