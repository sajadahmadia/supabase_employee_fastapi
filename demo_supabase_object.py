from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# setting up the environment
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

response = supabase.storage.from_(
    "demo_bucket").get_public_url("IMG_7662.HEIC")

print(response)
