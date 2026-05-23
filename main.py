# main.py

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from routes import employee_routes, auth_routes
from auth import auth_middleware

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def auth_redirect(request: Request, exc: StarletteHTTPException):
    if exc.status_code in (401, 403):
        return RedirectResponse('/login')
    raise exc


# Set up templates
templates = Jinja2Templates(directory="./templates")


# Include routers
app.include_router(employee_routes.router)
app.include_router(auth_routes.router)

app.middleware("http")(auth_middleware)