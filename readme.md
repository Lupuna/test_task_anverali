### Привет, проект состоит нескольких приложений:
 * В приложении registration находятся механизмы регистрации и аунтотефикации пользователя 
 * В приложении account находится личный кабинет пользователя

### Запуск проекта необходимо осуществлять через docker-compose.yml для этого нужно:
* Запустить Docker
* Собрать контейнер. Для этого нужно прописать команду docker-compose build
* После сборки необходимо запустить контейнер. Это можно сделать командой docker-compose up

### Для запуска unit тестов нужно:
* Запустить контейнер
* Прописать команду docker-compose run --rm web-app sh -c "python manage.py test ."
