# 排名查询小服务
## 使用
按照csv目录下的testest.csv的格式，编辑好数据，命名为考试的名字，如“大一下期末考试”，放在csv目录下，若有多个成绩文件同理。

提示：文件请以UTF-8格式保存，如果你想用别的格式，请自行修改server.py文件读取相关代码。

运行server.py，脚本会自动读取csv目录下的文件，并在前端体现。

## 命令行参数
-p --port 指定端口 默认80

-f --csv 指定成绩文件目录 默认csv目录

-d --debug 开启debug模式 默认False

## 依赖项
python3及标准库

bottle

paste