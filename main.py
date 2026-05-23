# main.py

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from routes import employee_routes, auth_routes
from auth import auth_middleware

app = FastAPI()


# Set up templates
templates = Jinja2Templates(directory="./templates")


# Include routers
app.include_router(employee_routes.router)
app.include_router(auth_routes.router)

app.middleware("http")(auth_middleware)