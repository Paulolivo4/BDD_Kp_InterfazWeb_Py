import pyodbc

# Datos de conexión
server = 'localhost'  # o la IP/instancia del servidor SQL Server
database = 'CATEQUESIS PARROQUIAL'
username = 'catequesis_user'
password = 'Software@2025'

# Cadena de conexión
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ Conexión exitosa")
except Exception as e:
    print("❌ Error al conectar:", e)
