from pydantic import BaseModel, EmailStr



class User(BaseModel):
    name : str = None
    Age:int=None
    email:EmailStr= None




user_obj :User =  User(name="Bapu",Age=12,email="Niraj@elcom.digital")
print(dict(user_obj))
