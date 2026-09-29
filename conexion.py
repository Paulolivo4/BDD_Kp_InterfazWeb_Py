import os

import pyodbc

# Connection settings come from environment variables (see .env.example).
server = os.environ.get('DB_SERVER', 'localhost')
database = os.environ.get('DB_NAME', 'CATEQUESIS PARROQUIAL')
username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

conn = None

if not (username and password):
    print("Missing DB_USER / DB_PASSWORD environment variables")
else:
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("Connection successful")
    except Exception as e:
        print("Connection error:", e)