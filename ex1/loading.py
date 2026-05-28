import importlib.metadata
import sys

def check_imports() -> None:
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(e)
        sys.exit(1) # Detiene la ejecución del script inmediatamente con un código de salida de error (1), impidiendo que el resto del programa intente correr sin las librerías necesaria

def check_installed_packages():
    packages = ['pandas', 'numpy', 'matplotlib']
    versions = {}
    for pkg in packages:
        try:
            versions[pkg] = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({versions[pkg]}) - Ready to load")
        except importlib.metadata.PackageNotFoundError:
            versions[pkg] = "Not detected"

if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    check_imports()
    print("Checking dependencies:")
    check_installed_packages()

