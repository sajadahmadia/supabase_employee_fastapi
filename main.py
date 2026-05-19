# main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import employee_routes


app = FastAPI()


# Mount the static files directory
app.mount("/static", StaticFiles(directory="./static"), name="static")


# Set up templates
templates = Jinja2Templates(directory="./templates")


# Include routers
app.include_router(employee_routes.router)
