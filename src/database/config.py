import streamlit as st
from supabase import create_client, Client

supabase_url = st.secrets.get("SUPABASE_URL")
supabase_key = st.secrets.get("SUPABASE_KEY")

if not supabase_url or not supabase_key or supabase_key == "paste-your-anon-key-here":
    raise RuntimeError(
        "Missing or invalid Supabase configuration. "
        "Set SUPABASE_URL and SUPABASE_KEY in .streamlit/secrets.toml with your Supabase anon key."
    )

supabase: Client = create_client(supabase_url, supabase_key)
