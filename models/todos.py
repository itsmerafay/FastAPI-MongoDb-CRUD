# Pydantic - Data validation and serilization library
# Pydantic is used for : data validation, automatic parsing, serialization, type checking                             
from pydantic import BaseModel

class Todo(BaseModel):
    name : str
    description : str
    complete : bool