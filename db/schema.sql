-- Schema for ai-attendance-project-app

CREATE TABLE IF NOT EXISTS teachers (
  teacher_id SERIAL PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS students (
  student_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  face_embedding JSONB,
  voice_embedding JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS subjects (
  subject_id SERIAL PRIMARY KEY,
  subject_code TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  section TEXT,
  teacher_id INTEGER REFERENCES teachers(teacher_id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS subject_students (
  id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
  subject_id INTEGER REFERENCES subjects(subject_id) ON DELETE CASCADE,
  UNIQUE (student_id, subject_id)
);

CREATE TABLE IF NOT EXISTS attendance_logs (
  id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES students(student_id) ON DELETE CASCADE,
  subject_id INTEGER REFERENCES subjects(subject_id) ON DELETE CASCADE,
  timestamp TIMESTAMPTZ,
  is_present BOOLEAN DEFAULT false
);
