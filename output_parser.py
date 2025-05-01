from typing import TypedDict


class User(TypedDict):
    id :int= None
    name : str = None
    Age:int = None
    email:str=None


user_info : User={
    "id":1,
    "name":"Raj",
    "Age":12,
    "email":"niraj@elcom.digital"
}


print(user_info.get("name"))