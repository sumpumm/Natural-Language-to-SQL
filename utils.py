import re

def extract_sql_query(text: str) -> str:
    match = re.search(r"SQLQuery:\s*(.*)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None