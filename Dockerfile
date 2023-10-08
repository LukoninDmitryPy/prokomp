# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.9
# Устанавливаем рабочую директорию для проекта в контейнере
WORKDIR /prokomp
# Скачиваем/обновляем необходимые библиотеки для проекта 
COPY requirements.txt /prokomp
RUN pip3 install --upgrade pip -r requirements.txt
# |ВАЖНЫЙ МОМЕНТ| копируем содержимое папки, где находится Dockerfile, 
# в рабочую директорию контейнера
COPY . /prokomp

CMD [ "flask", "run", "--host=0.0.0.0"]