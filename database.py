# database.py

import os
from supabase import create_client, Client
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

try:
    SUPABASE_URL = os.environ['SUPABASE_URL']
    SUPABASE_KEY = os.environ['SUPABASE_KEY']
    SUPABASE_BUCKET = os.environ['SUPABASE_BUCKET']
except KeyError as e:
    raise EnvironmentError(
        f"Missing Supabase environment variable: {e.args[0]}") from e


# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
