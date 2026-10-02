import os
from datetime import datetime

def saludar():
    print("¡Hola! Este script se ejecutó automáticamente en la nube con GitHub Actions.")

def listar_archivos():
    print("\n=== Archivos en el servidor ===")
    for carpeta_actual, subcarpetas, archivos in os.walk("."):
        if ".git" in carpeta_actual:
            continue
        print(f"📁 Carpeta: {carpeta_actual}")
        for archivo in archivos:
            print(f"  └── 📄 Archivo: {archivo}")

def generar_reporte():
    print("\n=== Generando archivo para Auto-Commit ===")
    # Crea o actualiza el archivo 'resultado.txt' sumando una nueva línea
    with open("resultado.txt", "a", encoding="utf-8") as f:
        f.write(f"Ejecución registrada el: {datetime.now()}\n")
    print("📄 Archivo 'resultado.txt' generado con éxito.")

if __name__ == "__main__":
    saludar()
    listar_archivos()
    generar_reporte()