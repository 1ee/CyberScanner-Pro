import json
import os

def save_report(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Report saved to {path}")