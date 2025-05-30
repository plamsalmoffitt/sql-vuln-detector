import os

def extract_sql(file_path):
    snippets = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if any(keyword in line.upper() for keyword in ["SELECT", "DELETE", "EXECUTE"]):
                snippets.append({
                    "file": os.path.basename(file_path),
                    "line": i + 1,
                    "code": line.strip()
                })
    return snippets
