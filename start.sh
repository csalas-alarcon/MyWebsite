#!/bin/bash

# 1. Ensure dependencies are in sync with your lockfile
echo "🚀 Syncing dependencies..."
uv sync

# 2. Start the server
echo "🌐 Starting FastAPI server..."
uv run uvicorn src.main:app --reload