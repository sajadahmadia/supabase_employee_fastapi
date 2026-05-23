# Employee Repository

A full-stack employee management app built with FastAPI and Supabase.

## Features

- **Employee CRUD** - Add, edit, deactivate employees with image uploads
- **Authentication** - Signup, login, logout via Supabase Auth with JWT stored in httponly cookies
- **Storage** - Employee images uploaded to Supabase Storage
- **Server-rendered UI** - Jinja2 templates, no frontend framework required

## Tech Stack

- **FastAPI** - Python web framework
- **Supabase** - Database, Auth, and Storage
- **Jinja2** - HTML templating
- **PyJWT** - JWT verification via Supabase JWKS
- **uv** - Python package management

## Setup

1. Clone the repo and install dependencies:
   ```bash
   uv sync
   ```

2. Create a `.env` file:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   SUPABASE_BUCKET=your_bucket_name
   SUPABASE_JWT_SECRET=your_jwt_secret
   DEBUG=true
   ```

3. Create the `employees` table in Supabase:
   ```sql
   create table employees (
       id serial primary key,
       first_name text not null,
       last_name text not null,
       email text unique not null,
       salary numeric not null,
       image_url text,
       is_active boolean default true
   );
   ```

4. Run the dev server:
   ```bash
   uv run uvicorn main:app --reload
   ```

## Deploy

```bash
uv run fastapi cloud deploy
```

Set environment variables via CLI before deploying:
```bash
uv run fastapi cloud env set SUPABASE_URL 'your_url'
uv run fastapi cloud env set SUPABASE_KEY 'your_key' --secret
uv run fastapi cloud env set SUPABASE_BUCKET 'your_bucket'
uv run fastapi cloud env set SUPABASE_JWT_SECRET 'your_secret' --secret
uv run fastapi cloud env set DEBUG 'false'
```

## Project Structure

```
main.py                  # App entry point, middleware, router registration
database.py              # Supabase client initialization
auth.py                  # JWT verification, auth middleware
models.py                # Pydantic models (EmployeeCreate, EmployeeUpdate)
forms.py                 # as_form decorator for HTML form support
routes/
  employee_routes.py     # Employee CRUD endpoints
  auth_routes.py         # Signup, login, logout endpoints
templates/
  index.html             # Employee list page
  add_employee.html      # Add employee form
  edit_employee.html     # Edit employee form
  login.html             # Login page
  signup.html            # Signup page
  error.html             # Error page
```
