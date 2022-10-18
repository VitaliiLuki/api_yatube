### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/VitaliiLuki/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


Примеры запросов к api:

```
примеры запросов смотри по адресу "root/redoc/"
```

### Описание эндпоинтов проекта:

Получение списка/создание публикаций.
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
