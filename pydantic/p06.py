from pprint import pprint
from pydantic import BaseModel, Field, ConfigDict

def to_lower_camel(string: str) -> str: #This function will turn the snake case to camel case
    first_word, *rest = string.split("_")
    capitalize_rest = "".join(word.capitalize() for word in rest if word)
    lower_camel = f"{first_word}{capitalize_rest}"
    return lower_camel

class Student(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid", alias_generator=to_lower_camel) #(populate_by_name) is for using both real names and aliases in new versions of pydantic
    first_name : str = Field
    last_name : str = Field
    stno : int = Field(alias="studentNumber")

data_dict = {
    "first_name" : "Alireza",
    "last_name" : "Mohammadi",
    "stno" : 97301797,
}

data_json = """
{
    "firstName": "Alireza",
    "lastName": "Mohammadi",
    "studentNumber": 97301797
}
"""

s1 = Student.model_validate(data_dict)
pprint(s1)
pprint(s1.first_name)

s2 = Student.model_validate_json(data_json)
pprint(s2)
pprint(s2.stno)