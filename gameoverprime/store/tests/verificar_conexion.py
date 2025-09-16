import cx_Oracle

try:
    conn = cx_Oracle.connect("django_grupo7", "Grupo72025progra", "localhost:1521/XEPDB1")
    print("✅ Conexión exitosa a Oracle con django_grupo7")
    conn.close()
except cx_Oracle.DatabaseError as e:
    print("❌ Error de conexión:", e)