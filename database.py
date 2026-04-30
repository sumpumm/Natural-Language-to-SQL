from langchain_community.utilities.sql_database import SQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
db_port = os.getenv("db_port")

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db= SQLDatabase.from_uri(connection_string, sample_rows_in_table_info=1)

print(db.dialect)
print(db.get_usable_table_names())
print(db.table_info) #give table schema along with row examples