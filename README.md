# Космический Телеграм

Телеграм бот, отправляющий фотки космической тематики

### Как установить

- Скачайте код и поместите в виртуальное окружение
```
python3 -m venv <название окружения>
```
```
<название окружения>\Scripts\activate.bat
```
```
git clone https://github.com/mihakurd2003/space.git
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как пользоваться файлом send_photos.py
- Для начала создайте файл .env в директории проекта, в этом файле создайте переменные:
```
TOKEN_NASA=<ваш токен с сайта https://api.nasa.gov/>
```
```
ID_SPACEX=<id с сайта https://github.com/r-spacex/SpaceX-API>
```
```
TELEGRAM_BOT_TOKEN=<ваш токен телеграм бота>
```
```
PUBLICATION_FREQUENCY=<кол-во времени по умолчанию(в часах)>
```
- В терминале набирайте команду:
```
python3 send_photos.py --timeout <кол-во часов>
```
- --timeout позволяет изменить частоту отправки фотографий. По умолчанию --timeout равен значению publication_frequency в файле .env

### Как пользоваться файлом send_photo.py
```
python3 send_photo --path <Фотография из images/>
```
- Если не указан --path, публикуется случайное фото из директории images/
#### Чтобы пользоваться следующими скриптами, убедитесь, что файл .env заполнен
### Как пользоваться файлом fetch_APOD_images.py
```
python3 fetch_APOD_images.py --key <ваш токен с сайта https://api.nasa.gov/>
```
- Если --key не заполнен, то по умолчанию используется значение из файла .env
### Как пользоваться файлом fetch_nasa_images.py
```
python3 fetch_nasa_images.py --key <ваш токен с сайта https://api.nasa.gov/>
```
- Если --key не заполнен, то по умолчанию используется значение из файла .env
### Как пользоваться файлом fetch_spacex_images.py
```
python3 fetch_spacex_images.py --id <id с сайта https://github.com/r-spacex/SpaceX-API>
```
- Если --id не заполнен, то по умолчанию используется значение из файла .env

