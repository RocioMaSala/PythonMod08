import importlib.metadata
import sys

def check_dependencies() -> None:
    packages = ['pandas', 'numpy', 'matplotlib']
    missing_packages = False

    print("Checking dependencies:")
    for pkg in packages:
        try:
            version = importlib.metadata.version(pkg)

            if pkg == "pandas":
                msg = "Data manipulation ready"
            elif pkg == "numpy":
                msg = "Numerical computation ready"
            elif pkg == "matplotlib":
                msg = "Visualization ready"
            else:
                msg = "Ready to load"
            print(f"[OK] {pkg} ({version}) - {msg}")
        except importlib.metadata.PackageNotFoundError:
            print (f"[ERROR] {pkg} - Not detected")
            missing_packages = True

    if missing_packages:
        print("\nError: Missing dependencies.")
        print("To install with pip: pip install -r requirements.txt")
        print("To install with Poetry: poetry install")
        sys.exit(1)

def check_matrix_data() -> None:
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
        
    data = np.random.randn(500, 2)
    frame = pd.DataFrame(data, columns=['X', 'Y'])
    print(f"Processing {len(frame)} data points...")
    print("Generating visualization...")

    plt.scatter(frame['X'], frame['Y'], alpha=0.3, color='pink')
    plt.title("Matrix Data Analysis")

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    check_dependencies()
    print("\n")
    check_matrix_data()

