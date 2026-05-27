import sys
import os
import site

def virtual_environment():
    python_path = sys.executable  # guarda en la variable el ejecutable exacto de Python que corre el script actual. ¿Qué programa está procesando mi código?
        # prefix ruta del entorno donde se buscan os paquetes y liberias actuales. Fuera del VEnv, los dos valen exactamente lo mismo. En Venv, prefix cambia para apuntar a la carpeta del entorno local. ¿Dónde están instaladas las librerias/config. que estoy usando?
    if sys.prefix != sys.base_prefix:  # base_prefix es la ruta de instalaión global principal de Python en mi ordenador. Nunca cambia mientras use esta versión de Pythonn.
        
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_path}")

        name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {name}")

        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.\n")

        package_path = site.getsitepackages()[0]
        print(f"Package installation path:\n {package_path}")

    else:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python:{python_path}")
        print(f"Virtual Environment: None detectected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")

virtual_environment()
        
