"""
Database initialization script for ai-attendance-project-app.
Run this once to create all required tables in Supabase.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import streamlit as st

# Configure minimal Streamlit app just to access secrets
if not st.session_state.get('_streamlit_initialized'):
    st.set_page_config(page_title='DB Init', layout='centered')
    st.session_state._streamlit_initialized = True

from src.database.config import supabase

def init_database():
    """Create all required tables in Supabase."""
    
    schema_sql = """
    -- Teachers table
    CREATE TABLE IF NOT EXISTS teachers (
      teacher_id BIGSERIAL PRIMARY KEY,
      username TEXT UNIQUE NOT NULL,
      password TEXT NOT NULL,
      name TEXT,
      created_at TIMESTAMPTZ DEFAULT now()
    );

    -- Students table
    CREATE TABLE IF NOT EXISTS students (
      student_id BIGSERIAL PRIMARY KEY,
      name TEXT NOT NULL,
      face_embedding JSONB,
      voice_embedding JSONB,
      created_at TIMESTAMPTZ DEFAULT now()
    );

    -- Subjects table
    CREATE TABLE IF NOT EXISTS subjects (
      subject_id BIGSERIAL PRIMARY KEY,
      subject_code TEXT UNIQUE NOT NULL,
      name TEXT NOT NULL,
      section TEXT,
      teacher_id BIGINT REFERENCES teachers(teacher_id) ON DELETE CASCADE,
      created_at TIMESTAMPTZ DEFAULT now()
    );

    -- Subject-Student enrollment junction table
    CREATE TABLE IF NOT EXISTS subject_students (
      id BIGSERIAL PRIMARY KEY,
      student_id BIGINT REFERENCES students(student_id) ON DELETE CASCADE,
      subject_id BIGINT REFERENCES subjects(subject_id) ON DELETE CASCADE,
      UNIQUE (student_id, subject_id)
    );

    -- Attendance logs table
    CREATE TABLE IF NOT EXISTS attendance_logs (
      id BIGSERIAL PRIMARY KEY,
      student_id BIGINT REFERENCES students(student_id) ON DELETE CASCADE,
      subject_id BIGINT REFERENCES subjects(subject_id) ON DELETE CASCADE,
      timestamp TIMESTAMPTZ,
      is_present BOOLEAN DEFAULT false
    );
    """
    
    try:
        # Execute the schema SQL
        result = supabase.postgrest.client.rpc("exec_sql", {"sql": schema_sql}).execute()
        print("✅ Database tables created successfully!")
        return True
    except Exception as e:
        # If RPC method doesn't exist, try alternative approach
        print(f"⚠️ RPC method not available, trying alternative approach...")
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    st.title("Database Initialization")
    st.write("Click the button below to create all required tables.")
    
    if st.button("Initialize Database", type="primary"):
        with st.spinner("Creating tables..."):
            success = init_database()
            if success:
                st.success("✅ All tables created successfully! You can now run the app.")
            else:
                st.error("""
                ❌ Could not initialize via script. Please manually run the SQL:
                
                1. Go to your Supabase project dashboard
                2. Navigate to SQL Editor
                3. Click "New Query"
                4. Paste the SQL from `db/schema.sql`
                5. Click "Run"
                """)
