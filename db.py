import sqlite3

def run_query(sql_query):
    conn = sqlite3.connect("study.db")
    cursor = conn.cursor()

    cursor.execute(sql_query)
    rows = cursor.fetchall()

    conn.close()
    return rows
