import oracledb
def probar(dsn, user, pwd):
    try:
        print("Probar:", dsn, user)
        con = oracledb.connect(user=user, password=pwd, dsn=dsn)
        con.close()
        print("OK")
    except Exception as e:
        print("ERROR:", e)

probar("127.0.0.1:1521/XEPDB1", "DJANGO_GRUPO7", "Grupo72025progra")
probar("127.0.0.1:1521/XE",     "DJANGO_GRUPO7", "Grupo72025progra")