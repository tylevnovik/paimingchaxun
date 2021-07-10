# -*- coding: utf-8 -*-
import argparse
import datetime
import os
import socket

from bottle import route, run, request, get, static_file, error, template

import csv


@get('/dump')
def dumpfunc():
    try:
        predownloaddumpfiles = [x for x in os.listdir('./dump') if not x.find('.dat') == -1]
    except FileNotFoundError:
        return 'No dump files found.'
    if predownloaddumpfiles == []:
        return 'No dump files found.'
    files = ''
    for asinglefile in predownloaddumpfiles:
        file = f'<a href="./dump/{asinglefile}">{asinglefile}</a>'
        files += file
    return files


@get('/dump/<filename>')
def getdumpfile(filename=None):
    if filename == '':
        return template('erroralertpage', content='别试了，啥都没有。')
    elif not filename.find('.dat') == -1:
        return static_file(filename, root='./dump', download=True)
    else:
        return template('erroralertpage', content='别试了，啥都没有。')


@error(404)
def error404(error):
    return template('erroralertpage', content='别试了，啥都没有。')


@error(500)
def error500(error):
    import pickle
    dumpfilename = './dump/dump' + datetime.datetime.today().strftime('%y%m%d') + '.dat'
    with open(dumpfilename, 'wb') as dumpfile:
        pickle.dump(datadict, dumpfile)
    return template('erroralertpage', content='服务器出错了，请联系系统管理员。</ br>QQ:1226159010')


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


def IsOpen(port, ip='127.0.0.1'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("-c", "--csvpath", type=str, default="./csv", help="the path of csv files")
    parse.add_argument("-p", "--port", type=int, default=80, help="the port number the service serving at")
    parse.add_argument("-d", "--debug", type=bool, default=False, help="whether to enable debug mode")
    args = parse.parse_args()
    csvfilepath = [x.replace('.csv', '') for x in os.listdir(args.csvpath) if not x.find('.csv') == -1]
    print('载入的csv文件列表：', csvfilepath)
    datadict = {'date': datetime.datetime.today(), 'data': {}}
    csvdictlist = []
    for filename in csvfilepath:
        path = args.csvpath + '/' + filename + '.csv'
        if os.path.exists(path):
            with open(path, 'r', encoding='UTF-8') as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    csvdictlist.append(row)
            datadict['data'][filename] = csvdictlist
            csvdictlist = []
    if args.debug:
        print(datadict)
    print('开始检查端口是否被占用')
    if not IsOpen(args.port):
        print(f'{args.port}端口未被占用，启动服务器')
        run(host='0.0.0.0', port=args.port, debug=False, server='paste')
    else:
        print(f'{args.port}端口已被占用，请更换端口')
