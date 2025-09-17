import cx_Oracle

try:
    dsn = cx_Oracle.makedsn("localhost", 1521, service_name="xe")
    conn = cx_Oracle.connect(
        user="django_grupo7",
        password="Grupo72025progra",
        dsn=dsn
    )
    print("✅ Conexión exitosa a Oracle XE con django_grupo7")
    conn.close()
except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("❌ Error de conexión:", error.message)

