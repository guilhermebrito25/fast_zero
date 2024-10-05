from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get('/users', status_code=HTTPStatus.OK)
def read_users():
    return {'user': database}