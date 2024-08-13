# WIth nosql database it is hard for python to use json as object so we need to serializer/deserialzier things to nosql info
# In here we will create an individual serializer for all our tables

def individual_serializer(todo) -> dict :
    return {
        "id": str(todo["_id"]) ,  # mongo specific for finding id is using _
        "name": todo["name"] ,
        "description": todo["description"],
        "complete": todo["complete"] ,
    }

def list_serializer(todos) -> list:
    return [individual_serializer(todo) for todo in todos]