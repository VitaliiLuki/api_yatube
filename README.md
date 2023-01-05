# Yatube API
This is a API project where users can create, edit and comment on posts, subscribe to each other. Users can also watch the latest posts of all authors or watch a posts only from favorite authors.


## Local setup
> Clone repository and go to directory "yatube_api"

```git clone https://github.com/VitaliiLuki/api_yatube.git```

```cd yatube_api/```

>Create and activate virtual environment

```python3 -m venv venv```

```source venv/bin/activate```

>Install all dependencies from requirements.txt

```pip install --upgrade pip```

```pip install -r requirements.txt```

>Go to directory with a manage.py, make migrations and run server

```cd yatube```

```python3 manage.py migrate```

```python3 manage.py runserver```


>To watch API documentation you need go to redoc endpoint:

```/redoc/```

### Project endpoints description:

Getting/creating a posts.
```
/api/v1/posts/
```
Getting/refreshing/partial update/deletion a post.
```
/api/v1/posts/{id}/
```
Getting/creating a comment.
```
/api/v1/posts/{id}/comments/
```
Getting/refreshing/partial update/deletion a comment.
```
/api/v1/posts/{id}/comments/{id}/
```
To get a group list.
```
/api/v1/groups/
```
To get information about a group.
```
/api/v1/groups/{id}/
```
To subscribe/watch a subscriptions.
```
/api/v1/follow/
```
To creare a new user.
```
/api/v1/users/
```
To create/refresh/check JWT-token.
```
/api/v1/jwt/create/
/api/v1/jwt/refresh/
/api/v1/jwt/verify/
```
