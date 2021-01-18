# -*- coding: utf-8 -*-
from bottle import route, run, request, get, static_file, error, template
import csv
import os


@get('/')
def showPage():
    return template('querypage')


@get('/favicon.ico')
def pushIcon():
    return static_file("favicon.ico", root='./')


@get('/guanji')
@get('/shutdown')
def shutdown():
    if request.query.pwd == "123456":
        os._exit(10086)
    else:
        return template('erroralertpage',content='密码错误，访问已记录')


@error(404)
def error404(error):
    return template('erroralertpage',content='啥都没有')


@route('/', method='POST')
def do_query():
    name = request.forms.get('name')
    xduid = request.forms.get('xduid')
    id = request.forms.get('id')
    item = request.forms.get('item')
    filepath = item + ".csv"
    # 读取csv至字典
    if os.path.exists(filepath):
        csvFile = open(filepath, "r")
    else:
        return template('erroralertpage',content='您选择的项目暂未开放查询，请返回重新选择')

    dict_reader = csv.DictReader(csvFile)

    for row in dict_reader:
        if row['name'] == name and row['xduid'] == xduid and row['id'] == id:
            rank = int(row['rank'])
            average = float(row['average'])
            returnstring = f'<title>查询成功</title><h1>{name}同学</h1><h1>你的平均成绩为{average}</h1><h1>你的年级排名为{rank}</h1><h1>位于年级的前{rank / 245 * 100:.2f}%</h1>'
            break
        else:
            returnstring = template('erroralertpage',content='输入有误，请返回重新查询')

    csvFile.close()
    return returnstring


run(host='0.0.0.0', port=12345, debug=False)
