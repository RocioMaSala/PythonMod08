import sys
import os
import site


def virtual_environment() -> None:
    python_path = sys.executable
    if sys.prefix != sys.base_prefix:
        print(f"Current Python: {python_path}")

        name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {name}")

        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\n")

        package_path = site.getsitepackages()[0]
        print(f"Package installation path:\n {package_path}")

    else:
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python:{python_path}")
        print("Virtual Environment: None detectected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    virtual_environment()
