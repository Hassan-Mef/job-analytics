from db_utils import get_connection

try:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM jobs;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
