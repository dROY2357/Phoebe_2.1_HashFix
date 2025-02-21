import os
import re

def replace_hex_values(file_path):
    replacements = {
        "3a4bf877": "8ee2fb7c",
        "a284a970": "00b2a919",
        "baea13f2": "ecac2cc5"
    }
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for old, new in replacements.items():
        content = re.sub(old, new, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated: {file_path}")

def scan_and_replace(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower() == "mod.ini":
                file_path = os.path.join(root, file)
                replace_hex_values(file_path)

if __name__ == "__main__":
    target_directory = os.getcwd()
    scan_and_replace(target_directory)
    print("Scan complete.")
