import os

from flask import jsonify, render_template, request
import json
import pandas as pd

from . import app, db
from .models import File


@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    '''
    Загрузка файла типа CSV в бд и в локальное хранилище
    '''
    if request.method == 'POST':
        f = request.files['file']
        if f.filename != '':
            filepath = os.path.join('uploads', f.filename)
            if not os.path.exists('uploads'):
                os.makedirs('uploads')
            f.save(filepath)
        data = pd.read_csv(filepath)
        column = ",".join(data.columns.tolist())
        file_record = File(file=f.filename, column=column)
        db.session.add(file_record)
        db.session.commit()

        return render_template('index2.html')
    return render_template("index.html")

@app.route('/show_data', methods=['GET'])
def showData():
    '''
    Получение всех таблиц со сводкой: id, наименование файла, Наименование столбцов
    ''' 
    data = File.query.all()
    files_list = [[ver.id, ver.file, ver.column] for ver in data]
    return render_template('show_csv_data.html',
                           data_var=files_list)

@app.route('/show_data/<int:file_id>', methods=['GET', 'DELETE'])
def get_data(file_id):
    '''
    Получение таблицы со сводкой: "Название стобца":"Строки столбца"
    Фильтрация по запросу: .../show_data/id?sort_columns=Название_столбца
    Удаление таблицы из локального хранилища и бд
    '''
    data = File.query.get_or_404(file_id)
    filepath = os.path.join('uploads', data.file)
    if request.method == 'GET':
        dat = pd.read_csv(filepath)
        sort_columns = request.args.getlist('sort_columns')
        if sort_columns:
            dat = dat.sort_values(by=sort_columns)
        return dat.to_json()
    elif request.method == 'DELETE':
        db.session.delete(data)
        db.session.commit()
        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            return({'Info':'File in system already deleted'})
        return ({'Info':'Done. Id {} deleted'.format(file_id)})