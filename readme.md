# YouTube Video Top Search MCP

## This project implements a **Model Control Protocol (MCP)** server that allows clients to query for the top YouTube videos based on a search term (e.g., product or ingredient name). It fetches the most viewed videos from YouTube and provides details such as video title, URL, and view count.

## Features

- Search YouTube for top videos based on a keyword.
- Retrieve video details including title, URL, and view count.
- Runs as an MCP server with SSE (Server-Sent Events) transport.
- Supports proxy configuration for YouTube Transcript API (optional).

---

## Requirements

- Python 3.9+
- Dependencies:
  - `google-api-python-client`
  - `pydantic`
  - `python-dotenv`
  - `mcp`
    Install dependencies:

```bash
pip install google-api-python-client pydantic python-dotenv mcp
```
