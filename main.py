import os

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

if __name__ == "__main__":
    saludar()
    listar_archivos()