import cx_Oracle

def diagnosticar_conexion():
    print("🔍 Iniciando diagnóstico de conexión...")
    
    # 1. Verificar si Oracle Client está instalado
    try:
        print(f"Versión de cx_Oracle: {cx_Oracle.version}")
        print(f"Versión de Oracle Client: {cx_Oracle.clientversion()}")
    except Exception as e:
        print("❌ Oracle Client no está configurado correctamente")
        print(f"Error: {e}")
        return
    
    # 2. Probar diferentes combinaciones de usuario/contraseña
    test_cases = [
        {"user": "django_grupo2025", "password": "Grupo72025progra123", "dsn": "XEPDB1"},
        {"user": "DJANGO_GRUPO2025", "password": "Grupo72025progra123", "dsn": "XEPDB1"},
        {"user": "django_grupo2025", "password": "GRUPO72025PROGRA123", "dsn": "XEPDB1"},
        {"user": "system", "password": "tu_password_system", "dsn": "XEPDB1"}  # Cambia esta línea
    ]
    
    for i, test in enumerate(test_cases, 1):
        try:
            conn = cx_Oracle.connect(
                user=test["user"],
                password=test["password"],
                dsn=test["dsn"]
            )
            print(f"✅ Test {i}: Conexión exitosa con {test['user']}")
            conn.close()
            return True
        except cx_Oracle.DatabaseError as e:
            print(f"❌ Test {i} falló con {test['user']}: {e}")
    
    return False

if __name__ == "__main__":
    diagnosticar_conexion()