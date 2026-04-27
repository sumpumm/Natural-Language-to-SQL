from pydantic import BaseModel, Field

class Query(BaseModel):
    sql: str = Field(description="The generated sql query")