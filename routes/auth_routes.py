from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from database import supabase_auth, DEBUG
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="./templates")


@router.get('/signup', response_class=HTMLResponse)
async def signup_form(request: Request):
    """Render the signup form."""
    return templates.TemplateResponse(request, 'signup.html')


@router.post('/signup')
async def signup(
    email: str = Form(...),
    password: str = Form(...)
):
    """Create a new user via Supabase Auth and redirect to login."""
    try:
        auth_response = supabase_auth.auth.sign_up({
            'email': email,
            'password': password
        })

        if auth_response.user is None:
            raise HTTPException(
                status_code=400,
                detail='Signup failed'
            )

        return RedirectResponse('/login', status_code=303)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get('/login', response_class=HTMLResponse)
async def login_form(request: Request):
    """Render the login form."""
    return templates.TemplateResponse(request, 'login.html')


@router.post('/login')
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    """Authenticate user and store JWT in an httponly cookie. we store the jwt token in the user's browser cookies"""
    try:
        auth_response = supabase_auth.auth.sign_in_with_password({
            'email': email,
            'password': password
        })

        if auth_response.user is None:
            return templates.TemplateResponse(
                request, 'login.html',
                {'error': 'Login failed', 'email': email}
            )

        access_token = auth_response.session.access_token

        response = RedirectResponse('/', status_code=303)

        response.set_cookie(
            key='access_token',
            value=f"Bearer {access_token}",
            httponly=True,
            secure=not DEBUG,
            samesite='lax'
        )

        return response

    except Exception as e:
        return templates.TemplateResponse(
            request, 'login.html',
            {'error': 'Invalid login credentials', 'email': email}
        )


@router.get('/logout')
async def logout():
    """Delete the access_token cookie and redirect to login."""
    response = RedirectResponse('/login', status_code=303)

    response.delete_cookie(key='access_token')

    return response
