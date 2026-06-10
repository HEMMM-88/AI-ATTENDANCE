# ai-attendance-project-app
PresentSir@1231

## Supabase setup

Create `.streamlit/secrets.toml` with your Supabase project values:

```toml
SUPABASE_URL = "https://<your-project-ref>.supabase.co"
SUPABASE_KEY = "<your-anon-key>"
```

Use the Supabase `anon` or `service_role` key from your project settings. The app will fail if the key is missing or still the placeholder value.