import os
import sys
from dotenv import load_dotenv

def main() -> None:
    load_dotenv()

    resultado = os.getenv("PROBANDO")
    print(resultado)

if __name__ == "__main__":
    main()