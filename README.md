# Yatube API
This is a API project where users can create, edit and comment on posts, subscribe to each other. View the latest posts of all users on the main page, or go to the subscriptions page and see posts only by the authors you like. Individual author profile pages and a detailed view of a particular post are also available.


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


>To watch API documentation go to redoc endpoint:

```/redoc/```

### Project endpoints description:

Getting a list of/creating a posts.
```
root/api/v1/posts/
```
Получение/обновление/частичное обновление/удаление публикации.
```
root/api/v1/posts/{id}/
```
Получение/добавление комментариев.
```
root/api/v1/posts/{id}/comments/
```
Получение/обновление/частичное обновление/удаление комментариев.
```
root/api/v1/posts/{id}/comments/{id}/
```
Cписок сообществ.
```
root/api/v1/groups/
```
Информация о сообществе.
```
root/api/v1/groups/{id}/
```
Подписаться/посмотреть подписки.
```
root/api/v1/follow/
```
Создать пользователя.
```
root/api/v1/users/
```
Получить/обновить/проверить JWT token.
```
root/api/v1/jwt/create/
root/api/v1/jwt/refresh/
root/api/v1/jwt/verify/
```
