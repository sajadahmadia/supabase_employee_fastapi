# the main CRUD operations with supabase
from supabase import create_client, Client

from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# setting up the environment
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


results = supabase.table("demo_table").select("*").execute()
print(results)

# insert a new row
new_row = [{"first_name": "jack"}, {"first_name": "jane"}]
result2 = supabase.table("demo_table").insert(new_row).execute()

print(result2)

update_name = {"first_name": "JOHN"}
# update row
results3 = supabase.table("demo_table").update(
    update_name).eq("id", 2).execute()
print(results3)


# delete record in a table
results4 = supabase.table("demo_table").delete().eq("id", 2).execute()
print(results4)
