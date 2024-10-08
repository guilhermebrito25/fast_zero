from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):  # Schema de criação do usuario
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):  # Schema para adicionar no BD
    id: int


class UserPublic(BaseModel):  # Schema de resposta publica do usuario
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):  # Schema de resposta publica do usuario
    users: list[UserPublic]
