# Python3脚本，不适用于Python2
# !/usr/bin/envpython
# coding=utf-8
from bottle import route, run, request
import csv

# 此处可扩充为完整HTML
queryPage = '''
	<form action="/" method="POST" enctype="multipart/form-data">
		<h1>排名查询</h1><br>
		请输入姓名：<input type="text" name="name" /><br>
		请输入学号：<input type="text" name="xduid" /><br>
		请输入身份证号：<input type="text" name="id" /><br>
    	<input type="submit" value="查询" />
	</form>
'''


@route('/')
def showPage():
    return queryPage


@route('/', method='POST')
def do_query():
    name = request.forms.get('name')
    xduid = request.forms.get('xduid')
    id = request.forms.get('id')
    # 读取csv至字典
    csvFile = open("instance.csv", "r")
    dict_reader = csv.DictReader(csvFile)

    for row in dict_reader:
        if row['name'] == name and row['xduid'] == xduid and row['id'] == id:
            rank = int(row['rank'])
            average = float(row['average'])
            returnString = f'{name}同学，你的平均成绩为{average}，你的年级排名为{rank}，位于年级的前{rank / 245 * 100:.2f}%'
            break
        else:
            returnString = '输入有误，请返回重新输入'

    csvFile.close()
    return returnString


run(host='0.0.0.0', port=12345, debug=True)
