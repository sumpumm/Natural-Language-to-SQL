import re
import pandas as pd

def extract_sql_query(text: str) -> str:
    match = re.search(r"SQLQuery:\s*(.*)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def get_table_details():
    table_description = pd.read_csv("table_descriptions.csv",engine="python")

    table_details=""
    for index, row in table_description.iterrows():
        table_details = table_details + "Table Name:" + row['table'] + "\n" + "Table Description:" + row['description'] + "\n\n"
    return table_details