from fastapi import FastAPI
from routes import base
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv(".env")
# Create the FastAPI application instance
app = FastAPI()
# Include the base router
app.include_router(base.router)

