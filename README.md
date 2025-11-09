# Проект интернет-магазина
В проекте добавлено HTML-шаблона: 

home.html для домашней страницы и 

contacts.html для страницы с контактной информацией.

Для стилизации страниц используется Bootstrap.


- Создан контроллер для отображения домашней страницы.
- Создан контроллер для отображения страницы с контактной информацией.
- Настроена маршрутизация для этих контроллеров.
- Реализована форма обратной связи на странице контактов.
- Настроена обработка данных формы в контроллере, чтобы отображать сообщение об успешной отправке данных.

## Настройка виртуального окружения

### Создание

```commandline
python -m venv venv 
```

### Активация (Windows)

```commandline
venv\Scripts\activate
```

### Активация (Linux/macOS)

```commandline
source venv/bin/activate
```
### Установка зависимостей
```commandline
pip install -r requirements.txt
```

Установка Django
```commandline
pip install django
```

Два основных способа инициализации проекта с помощью утилиты
django-admin :

```commandline
django-admin startproject config .
```

```commandline
django-admin startproject myproject
```
## Запуск сервера

```commandline
python manage.py runserver
```
### Остановка приложения

```commandline
Ctrl + C
```


Автор: Казанцев Андрей