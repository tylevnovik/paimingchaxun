# -*- coding: utf-8 -*-
from bottle import route, run, request, get, static_file, error, template
import csv
import os


@error(404)
def error404(error):
    return template('erroralertpage', content='啥都没有')


@error(500)
def error500(error):
    return template('erroralertpage', content='服务器出错了')


@get('/')
def showPage():
    return template('querypage')


@get('/favicon.ico')
def pushIcon():
    return static_file("favicon.ico", root='./')


@get('/guanji')
def guanji():
    if request.query.pwd == "123456":
        os.system('shutdown -s -t 10')
    else:
        return template('erroralertpage', content='密码错误，访问已记录')


@get('/shutdown')
def shutdown():
    if request.query.pwd == "123456":
        os._exit(10086)
    else:
        return template('erroralertpage', content='密码错误，访问已记录')


@route('/', method='POST')
def do_query():
    name = request.forms.get('name')
    xduid = request.forms.get('xduid')
    id = request.forms.get('id')
    item = request.forms.get('item')
    filepath = item + ".csv"
    # 读取csv至字典
    if os.path.exists(filepath):
        itemcsv = open(filepath, "r")
    else:
        return template('erroralertpage', content='您选择的项目暂未开放查询，请返回重新选择')

    data = csv.DictReader(itemcsv)

    for row in data:
        if row['name'] == name and row['xduid'] == xduid and row['id'] == id:
            rank = int(row['rank'])
            average = float(row['average'])
            returnstring = template('result', name=name, average=average, rank=rank, percent=f'{rank / 245 * 100:.2f}',
                                    ratings=f'{10 - (rank / 245 * 10):.2f}')
            break
        else:
            returnstring = template('erroralertpage', content='输入有误，请返回重新查询')

    itemcsv.close()
    return returnstring


run(host='0.0.0.0', port=12345, debug=False, server='paste')
