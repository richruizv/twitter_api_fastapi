#models
from models import User,Tweet

#python
from typing import List

#fastapi
from fastapi import FastAPI
from fastapi import status
from fastapi import Path



app = FastAPI()

# path operations
@app.get(path="/")
def home():
    return {"Twitter API" : "Working!"}

## Auth
@app.post('/auth/signup',
        response_model=User,
        response_model_exclude={"password"},
        status_code=status.HTTP_201_CREATED,
        summary='Sign up',
        tags=['Auth', 'Users'])
def signup(user: User) -> User:
    pass


@app.post('/auth/login',
          response_model=User,
          response_model_exclude={"password"},
          status_code=status.HTTP_200_OK,
          summary='Login',
          tags=['Auth', 'Users'])
def login(user: User) -> User:
    pass


## Users


@app.get('/users/',
         response_model=List[User],
         status_code=status.HTTP_200_OK,
         summary='Get all users',
         tags=['Users'])
def list_users() -> List[User]:
    pass


@app.get('/users/{id}',
         response_model=User,
         status_code=status.HTTP_200_OK,
         summary='Get a user',
         tags=['Users'])
def retrieve_user(
    id: int = Path(...,
                   gt=0,
                   title='User ID',
                   description='The ID of the user to retrieve',
                   example=1,),
) -> User:
    pass


@app.put('/users/{id}',
         response_model=User,
         status_code=status.HTTP_200_OK,
         summary='Update user',
         tags=['Users'])
def update_user(
    id: int = Path(...,
                   gt=0,
                   title='User ID',
                   description='The ID of the user to update',
                   example=1,),
) -> User:
    pass


@app.delete('/users/{id}',
            status_code=status.HTTP_204_NO_CONTENT,
            summary='Delete user',
            tags=['Users'])
def delete_user(
    id: int = Path(...,
                   gt=0,
                   title='User ID',
                   description='The ID of the user to update',
                   example=1,),
) -> User:
    pass


## Tweets


@app.get('/tweets/',
         response_model=List[Tweet],
         status_code=status.HTTP_200_OK,
         summary='Get all tweets',
         tags=['Tweets'])
def list_tweets() -> List[Tweet]:
    pass


@app.get('/tweets/{id}',
         response_model=Tweet,
         status_code=status.HTTP_200_OK,
         summary='Get a tweet',
         tags=['Tweets'])
def retrieve_tweet(
    id: int = Path(...,
                   gt=0,
                   title='Tweet ID',
                   description='The ID of the tweet to retrieve',
                   example=1,),
) -> Tweet:
    pass

@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet',
    tags=['Tweets']
)
def post():
    pass


@app.put('/tweets/{id}',
         response_model=Tweet,
         status_code=status.HTTP_200_OK,
         summary='Update tweet',
         tags=['Tweets'])
def update_tweet(
    id: int = Path(...,
                   gt=0,
                   title='Tweet ID',
                   description='The ID of the tweet to update',
                   example=1,),
) -> Tweet:
    pass


@app.delete('/tweets/{id}',
            status_code=status.HTTP_204_NO_CONTENT,
            summary='Delete tweet',
            tags=['Tweets'])
def delete_tweet(
    id: int = Path(...,
                   gt=0,
                   title='Tweet ID',
                   description='The ID of the tweet to update',
                   example=1,),
) -> Tweet:
    pass
