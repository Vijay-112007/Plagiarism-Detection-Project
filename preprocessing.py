import os
import re
import json
from collections import Counter

# Try to import mysql.connector (for database work)
try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except Exception:
    MYSQL_AVAILABLE = False

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "PASSWORD",      
    "database": "PlagiarismStudents"       
}

SOURCE_TABLE = "studentsAssignments"       # table where student file names are stored
ID_COL = "student_id"                      # column with student IDs
FILENAME_COL = "student_filename"          # column with file names

# Folder where student files will be stored
SUBMISSIONS_FOLDER = os.path.join(os.getcwd(), "submissions")

# Table to store processed results
PREP_TABLE = "preprocessed_submissions"
# ------------------------------------------------


# ---------- TEXT CLEANING FUNCTIONS ----------
def clean_text(text: str) -> str:
    #Convert text to lowercase, remove punctuation/numbers, keep only words.
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)  # keep only letters and spaces
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text

def tokenize(text: str):
    #Split text into words (tokens).
    return text.split()

def word_freq(tokens):
    #Count how many times each word appears.
    return Counter(tokens)

def freq_to_json(counter: Counter) -> str:
    #Convert word frequencies to JSON string for storage in DB.
    return json.dumps(dict(counter), ensure_ascii=False)
# ---------------------------------------------

# ---------- DATABASE HELPERS ----------
def ensure_prep_table(cursor):
    #Make sure the preprocessed_submissions table exists in DB.
    create_stmt = f"""
    CREATE TABLE IF NOT EXISTS {PREP_TABLE} (
        {ID_COL} INT PRIMARY KEY,
        clean_text TEXT,
        word_freq_json LONGTEXT
    );
    """
    cursor.execute(create_stmt)

def fetch_rows_from_db(cursor):
    #Fetch student IDs and filenames from database table.
    q = f"SELECT {ID_COL}, {FILENAME_COL} FROM {SOURCE_TABLE};"
    cursor.execute(q)
    return cursor.fetchall()
# --------------------------------------


def preprocess_and_store_db():
    #Main function for DB mode: fetch files, preprocess, store results in DB.
    if not MYSQL_AVAILABLE:
        print("mysql.connector not installed. Run: pip install mysql-connector-python")
        return False

    # Connect to MySQL
    try:
        cnx = mysql.connector.connect(**DB_CONFIG)
    except Exception as e:
        print("DB connection failed:", e)
        return False

    cursor = cnx.cursor(dictionary=True)
    ensure_prep_table(cursor)
    cnx.commit()

    rows = fetch_rows_from_db(cursor)
    if not rows:
        print("No student files found in DB.")
        return True

    processed = 0
    for r in rows:
        sid = r.get(ID_COL)
        fname = r.get(FILENAME_COL)
        if not fname:
            continue

        path = os.path.join(SUBMISSIONS_FOLDER, fname)
        if not os.path.exists(path):
            print(f"[missing] File for ID={sid} not found: {path}")
            continue

        # Read file content
        with open(path, "r", encoding="utf-8") as fh:
            raw = fh.read()

        # Clean + tokenize + count
        cleaned = clean_text(raw)
        tokens = tokenize(cleaned)
        freq = word_freq(tokens)
        freq_json = freq_to_json(freq)

        # Insert or update DB
        upsert = f"""
        INSERT INTO {PREP_TABLE} ({ID_COL}, clean_text, word_freq_json)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
          clean_text = VALUES(clean_text),
          word_freq_json = VALUES(word_freq_json)
        """
        cursor.execute(upsert, (sid, cleaned, freq_json))
        cnx.commit()
        processed += 1
        print(f"[ok] ID={sid} processed | tokens={len(tokens)} | unique={len(freq)}")

    cursor.close()
    cnx.close()
    print(f"DB mode done — processed {processed} files.")
    return True


def preprocess_local_and_save():
    #Local-only mode: process all .txt files in submissions/ and save as JSON.
    out_dir = "preprocessed_results"
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(SUBMISSIONS_FOLDER):
        print("Submissions folder not found:", SUBMISSIONS_FOLDER)
        return

    files = [f for f in os.listdir(SUBMISSIONS_FOLDER) if f.endswith(".txt")]
    if not files:
        print("No .txt files in", SUBMISSIONS_FOLDER)
        return

    for fname in files:
        path = os.path.join(SUBMISSIONS_FOLDER, fname)
        with open(path, "r", encoding="utf-8") as fh:
            raw = fh.read()

        # Clean + tokenize + count
        cleaned = clean_text(raw)
        tokens = tokenize(cleaned)
        freq = word_freq(tokens)

        # Save result in JSON file
        out = {
            "filename": fname,
            "clean_text": cleaned,
            "word_freq": dict(freq)
        }
        out_path = os.path.join(out_dir, fname + ".json")
        with open(out_path, "w", encoding="utf-8") as of:
            json.dump(out, of, ensure_ascii=False, indent=2)

        print(f"[saved] {out_path} | tokens={len(tokens)} | unique={len(freq)}")

    print("Local mode done — results in", out_dir)


# ---------- MAIN ----------
if __name__ == "__main__":
    print("Starting preprocessing...")
    db_ok = preprocess_and_store_db()
    if not db_ok:
        print("Database not available. Falling back to local-only mode.")
        preprocess_local_and_save()
