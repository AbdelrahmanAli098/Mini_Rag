from fastapi import APIRouter, FastAPI
import os


# Create a router instance
router = APIRouter(
    prefix="/api/v1",
    tags=["Base"]
)

# Define a welcome endpoint
@router.get("/")
async def welcome():
    # Access environment variables
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")

    return {"message": f"Welcome to the {app_name} API!", "version": app_version}