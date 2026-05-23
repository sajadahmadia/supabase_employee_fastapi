# database.py

import os
from supabase import create_client, Client
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


SUPABASE_URL = os.environ['SUPABASE_URL']
SUPABASE_KEY = os.environ['SUPABASE_KEY']
SUPABASE_BUCKET = os.environ['SUPABASE_BUCKET']
SUPABASE_JWT_SECRET = os.environ['SUPABASE_JWT_SECRET']
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
if not all([SUPABASE_URL, SUPABASE_KEY, SUPABASE_BUCKET, SUPABASE_JWT_SECRET]):
    raise EnvironmentError(
        "one or more supabase environment variables are missing")

# Main client for table/storage operations (stays unauthenticated)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Separate client for auth (sign_in/sign_up mutate client state)
supabase_auth: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
