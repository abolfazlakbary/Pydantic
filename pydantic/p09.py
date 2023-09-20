from __future__ import annotations
from pprint import pprint
from pydantic import BaseModel, constr, model_validator

class User(BaseModel):
    username : constr(min_length=2, strict=True)
    pass1 : constr(min_length=5, strict=True)
    pass2 : constr(min_length=5, strict=True)

    @model_validator(mode="after") #after means the programm first runs the class, then checks the function
    def check_passwords_match(self) -> User:
        if self.pass1 != self.pass2:
            raise ValueError("Passwords do not match")
        return self

u1 = User(username="alireza", pass1="asdfg", pass2="asdfg")
pprint(u1)