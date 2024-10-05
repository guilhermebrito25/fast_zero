from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get('/users', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database[user_id - 1] = user_with_id
    return user_with_id
