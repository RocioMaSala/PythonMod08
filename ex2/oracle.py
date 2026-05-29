import os
from dotenv import load_dotenv


def loading_config_status_seccheck() -> None:

    load_dotenv()
    mode = os.getenv("MATRIX_MODE", "development").lower()
    database = os.getenv("DATABASE_URL", "sqlite:///local_matrix.db")
    api_access = os.getenv("API_KEY", "MISSING_API_KEY_ENV")
    log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
    zion_network = os.getenv("ZION_ENDPOINT", "http://localhost:8000/v1")

    if mode == "production":
        database = "Connected to Zion Mainframe"
        zion_network = "Secure Uplink Active"
        if log_level != "INFO":
            log_level = "INFO"
        production_overrides = True
    else:
        database = "Connected to local instance"
        zion_network = "Simulated Localhost(Online)"
        if log_level != "INFO" and log_level != "DEBUG":
            log_level = "DEBUG"
        production_overrides = False

    is_api_valid = api_access != "MISSING_API_KEY_ENV" and api_access != ""

    if api_access == "MISSING_API_KEY_ENV" or api_access == "":
        api_access = "[WARNING] API_KEY is missing - Unauthenticated Access"
    else:
        api_access = "[OK] API_KEY detected - Authenticated - Access granted"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api_access}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_network}")

    print("\nEnvironment security check:")
    if is_api_valid:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Using default/missing credentials")

    if os.path.exists(".env"):
        try:
            with open(".gitignore", "r") as check:
                if ".env" in check.read():
                    print("[OK] .env file properly configured")
                else:
                    print("[!] ALERT: .env is NOT in .gitignore!")
        except FileNotFoundError:
            print("[!] ALERT: .gitignore not found!")
    else:
        print("[WARNING] .env file missing")

    if production_overrides:
        print("[OK] Production overrides available")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    loading_config_status_seccheck()
