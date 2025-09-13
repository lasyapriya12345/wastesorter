import subprocess
import sys

def main():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "waste_sorter.py"])

if __name__ == "__main__":
    main()