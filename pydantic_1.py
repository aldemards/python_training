import pydantic
from typing import Optional

# class User:
#     def __init__(self, username:str, password:str, age:int) -> None:
#         self.username = username
#         self.password = password
#         self.age = age

#     def __repr__(self) -> str:
#         return f'{self.username}, {self.age}'

#     def __str__(self) -> str:
#         return f'el usuario {self.username}'

# u = User('Juan', '123', 25)

#python -m virtualenv env
#pip freeze  ->  esto es para saber cuales librerias tengo

class User(pydantic.BaseModel):
    username: str
    age: int
    password: str
    score: int
    email: Optional[str]

    @pydantic.validator('email')
    @classmethod
    def email_validator(cls, value):
        if '@' not in value:
            raise ValueError('Email has to have @ in it')
        else:
            return value

    @pydantic.validator('age','score')
    @classmethod
    def age_score_validator(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError('Numbers must be possitive')



u = User(username='Juan', age=25, score=5, password='123',email='ejemplo@gmail.com')
print(u)
