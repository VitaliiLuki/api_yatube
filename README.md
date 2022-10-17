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


