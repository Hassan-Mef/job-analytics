import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_Name = os.getenv('DB_NAME')
DB_User = os.getenv('DB_USER')
DB_Password = os.getenv('DB_PASSWORD')
DB_Host = os.getenv('DB_HOST', 'localhost')
DB_Port = os.getenv('DB_PORT', '5432')

try:
    # Connect
    conn = psycopg2.connect(
        dbname=DB_Name,
        user=DB_User,
        password=DB_Password,
        host=DB_Host,
        port=DB_Port
    )
    cur = conn.cursor()

    # Run query
    cur.execute("SELECT * FROM jobs;")
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
