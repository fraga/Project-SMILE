# ./backend/src/api/main.py

# Import FastAPI class from fastapi module
from fastapi import FastAPI

# Import CORSMiddleware to handle Cross-Origin Resource Sharing
from fastapi.middleware.cors import CORSMiddleware

# Import the router from the app.api.routers module
from app.api.routers import router

import uvicorn
import asyncio
import logging
import sys
from app.configs.settings import settings
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = settings.app_config["langchain_config"]["tracing_v2"]
os.environ["LANGCHAIN_ENDPOINT"] = settings.app_config["langchain_config"]["endpoint"]
os.environ["LANGCHAIN_PROJECT"] = settings.app_config["langchain_config"]["project"]


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create an instance of the FastAPI class
app = FastAPI()

# Include the router in the FastAPI app
app.include_router(router)

# Add middleware to handle CORS
# This allows all origins, credentials, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow credentials (cookies, authorization headers, etc.)
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

def run_app():
    """Run the FastAPI application synchronously."""
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )

if __name__ == "__main__":
    run_app()

