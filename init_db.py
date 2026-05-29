import os
import pymysql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_DATABASE = os.getenv("DB_DATABASE", "hospital_db")

def run_sql_file(cursor, filepath):
    print(f"[*] Executing SQL file: {filepath}")
    with open(filepath, 'r') as f:
        sql_content = f.read()
    
    # Split by semicolon, but ignore semicolons inside comments/strings
    # Simple split works for our schema and seed files
    statements = sql_content.split(';')
    for statement in statements:
        stmt_clean = statement.strip()
        if stmt_clean and not stmt_clean.startswith('--'):
            cursor.execute(stmt_clean)

def main():
    print("[*] Connecting to MySQL server...")
    try:
        # Connect without specifying database to create it if it doesn't exist
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("[+] Connected to MySQL server successfully.")
    except Exception as e:
        print(f"[-] Failed to connect to MySQL server: {e}")
        print("[-] Please ensure that a local MySQL Server is running and credentials in .env are correct.")
        print("[-] App will run in Mock Database Mode for now.")
        return

    try:
        with conn.cursor() as cursor:
            # 1. Run schema.sql
            run_sql_file(cursor, 'schema.sql')
            conn.commit()
            print("[+] Schema imported successfully.")
            
            # 2. Run seed.sql
            run_sql_file(cursor, 'seed.sql')
            conn.commit()
            print("[+] Seed data imported successfully.")
            print("[+] Database initialization complete!")
    except Exception as e:
        print(f"[-] Database initialization failed: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    main()
