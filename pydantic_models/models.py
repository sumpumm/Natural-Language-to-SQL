from pydantic import BaseModel, Field
from typing import List

class Query(BaseModel):
    sql: str = Field(description="The generated sql query")
 
class Table(BaseModel):
    """Table in SQL database."""
    name: List[str] = Field(description="Name of table in SQL database.")