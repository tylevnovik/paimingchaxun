# -*- coding: utf-8 -*-
import csv
import datetime
import os

from bottle import route, run, request, get, static_file, error, template


@error(404)
def error404(error):
    return template('erroralertpage', content='啥都没有')


@error(500)
def error500(error):
    return template('erroralertpage', content='服务器出错了')


@get('/')
def showPage():
    options = ''
    for item in csvfilepath:
        option = f'<option value="{item}" selected="" class="gwd-grp-xuj0">{item}</option>'
        options += option
    return template('querypage', options=options)


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
    try:
        data = datadict['data'][item]
    except KeyError:
        return template('erroralertpage', content='您选择的项目暂未开放查询，请返回重新选择')
    for row in data:
        if row['name'] == name and row['xduid'] == xduid and row['id'] == id:
            rank = int(row['rank'])
            average = float(row['average'])
            returnstring = template('result', name=name, average=average, rank=rank,
                                    percent=f'{rank / 245 * 100:.2f}',
                                    ratings=f'{10 - (rank / 245 * 10):.2f}')
            break
        else:
            returnstring = template('erroralertpage', content='输入有误，请返回重新查询')

    return returnstring


if __name__ == '__main__':
    csvfilepath = os.listdir('.\\')
    csvfilepath = [x.replace('.csv', '') for x in csvfilepath if not x.find('.csv') == -1]
    print('载入的csv文件列表：', csvfilepath)
    datadict = {'date': datetime.datetime.today(), 'data': {}}
    csvdictlist = []
    for filename in csvfilepath:
        path = filename + '.csv'
        if os.path.exists(path):
            with open(path) as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    csvdictlist.append(row)
            datadict['data'][filename] = csvdictlist
            csvdictlist = []
    print(datadict)
    run(host='0.0.0.0', port=12345, debug=False, server='paste')
