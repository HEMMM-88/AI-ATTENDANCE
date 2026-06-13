# Database Setup Instructions

The app requires several tables in Supabase to function. Follow these steps to initialize your database.

## Option 1: Supabase Dashboard (Easiest)

1. Open your [Supabase project dashboard](https://app.supabase.com)
2. Navigate to **SQL Editor** (left sidebar)
3. Click **"New Query"**
4. Copy and paste the contents of `db/schema.sql`
5. Click **"Run"** (or press `Ctrl+Enter`)
6. Close the query editor and restart your app

## Option 2: Using psql CLI

If you have PostgreSQL client tools installed:

```powershell
# Get your Supabase connection string from Settings > Database > Connection Info
$SUPABASE_CONNECTION_STRING = "postgresql://postgres:[password]@[host]/postgres"

psql $SUPABASE_CONNECTION_STRING < db\schema.sql
```

## Option 3: Using Python Script

Run the initialization script (after the tables are created manually via Option 1 or 2):

```powershell
streamlit run init_db.py
```

## Verify Tables Were Created

After running the SQL, verify in Supabase dashboard:

1. Go to **Table Editor** (left sidebar)
2. You should see:
   - `teachers`
   - `students`
   - `subjects`
   - `subject_students`
   - `attendance_logs`

If you see these tables, your app should work. If not, check for SQL errors in the query output.

## Troubleshooting

- **"table already exists" error**: Safe to ignore; the schema uses `CREATE TABLE IF NOT EXISTS`
- **Permission denied**: Ensure your Supabase API key has appropriate permissions
- **Still getting "table not found" error after creating tables**: Try clearing Streamlit cache and restarting the app

```powershell
# Clear Streamlit cache
rm ~\.streamlit\cache -Recurse

# Restart the app
streamlit run app.py
```
