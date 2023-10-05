# 🧑‍💻 Приложение `Mailer` для отправки писем клиентам.

### Содержание:
1. [Старт работы (как запустить приложение)](#start)
2. [Работа с пприложением)](#work)
3. [Тестирование приложения с помощью Pytest:](#testing)


<a id='start'></a>
## 1. 📝 Старт работы (как запустить приложение)

Чтобы запустить `проект` локально, необходимо произвести `клонирование` на локальное устройство следующей командой

```
git clone https://github.com/ValentinKim531/Mailer.git
```

После успешного клонирования проекта, создаем и активируем `виртуальное окружение` 
```
python3 -m virtualenv venv
```
```
source venv/bin/activate 
```
и загружаем все зависимости проекта:

```
pip3 install -r requirements.txt
```

Запустите SMTP сервер для разработки (`smtp4dev`):

```
docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev 
```

Создайте образ `приложения` на Docker:

```
docker build -t mailer-service .
```

Запустите контейнер:

```
docker run -e SMTP_HOST=host.docker.internal -e SMTP_PORT=2525 -p 8000:8000 -v $(pwd):/app mailer-service 
```
---
<a id='work'></a>
## 2. 📫 Для отправки Email перейдите по ссылке:

```
http://localhost:8000/docs
```
---
<a id='testing></a>
## 3. 🌍 Для тестирования приложения с помощью Pytest, наберите 
## в командной строке, где вы запустили приложение:  

```
pytest test.py
```
