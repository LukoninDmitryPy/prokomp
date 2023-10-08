# prokomp
# R4C
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat-square&logo=Flask)](https://flask-docs.readthedocs.io/)
[![openpyxl](https://img.shields.io/badge/-openpyxl-464646?style=flat-square&logo=openpyxl)](https://openpyxl.readthedocs.io/en/stable/)
HTTP сервис для работы с импортируемыми данными
## Использование
Склонируйте репозиторий  
```
git clone https://github.com/LukoninDmitryPy/prokomp.git
```
# Если используете Docker: 
```
docker-compose up -d --build
```
Сервис будет доступен по адресу: http://127.0.0.1:5000

# Локальный запуск:
Создайте виртуальное окружение:
```
python -m venv venv
```
Активируйте виртуальное окружение
* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установите зависимости 
```
pip install -r requirements.txt
```
Запустите проект
```
flask run
```

Сервис будет доступен по адресу: http://127.0.0.1:5000

Данный сервис имеет Endpoints:
```
POST/GET .../

Загрузка файла типа CSV в бд и в локальное хранилище
```
```
GET .../show_data

Получение всех таблиц со сводкой: id, наименование файла, Наименование столбцов
```
```
GET/DELETE .../show_data/<int:file_id>

Получение таблицы со сводкой: "Название стобца":"Строки столбца"
Фильтрация по запросу: .../show_data/id?sort_columns=Название_столбца
Удаление таблицы из локального хранилища и бд
```

## Над проектом работали
- [Дмитрий Луконин](https://wa.me/79153612056)