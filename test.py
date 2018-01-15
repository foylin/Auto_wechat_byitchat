#!/usr/bin/python
#coding:utf-8
# import pymysql
import io
import sys
# from urllib.parse import quote
import urllib
import requests
# imp.reload(sys)
# sys.setdefaultencoding('utf-8')
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')

TULINGKEY = 'a553ec404b0a4ffba3349e5b2e6ed319'
HOST = 'www.wyingrobot.com'
PORT = 3306
USER = 'wyingrob_01'
PASSWD = 'wying2018'
DB = 'wyingrob_videocms'
CHARSET = 'utf8'


def get_sort_url(url):
    apiurl = "http://suo.im/api.php?url=%s" % url
    url_sort = requests.get(apiurl)
    return url_sort.text


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# keywords = input()
keywords = '人民的名义'


# apiUrl = 'http://suo.im/api.php?url=http://www.baidu.com'
# data = {
#         'url'  : 'http://videocms.net/index.php?m=vod-search-wd-%E4%BA%BA%E6%B0%91%E7%9A%84%E5%90%8D%E4%B9%89',
#     }
# r = requests.get(apiUrl)

# print(r.text)

# 打开数据库连接
db = MySQLdb.connect(host=HOST, port=PORT, user=USER,
                         passwd=PASSWD, db=DB, charset=CHARSET)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT count(*) FROM baiyug_vod WHERE d_name like '%%%s%%'" % (keywords)

# print(sql)
# try:
    # 执行SQL语句
cursor.execute(sql)
    # 获取所有记录列表
results = cursor.fetchone()
# print results[0]
# print sql
if  results[0] > 0:
    # print(results[0])
     video_link = 'http://videocms.net/index.php?m=vod-search-wd-%s' % urllib.quote(keywords)
     video_link_sort = get_sort_url(video_link)
     return_mas = "已为您搜索到 %d 条信息 \n以下为视频链接地址 %s " % (results[0], video_link_sort)
     print return_mas

# for row in results:
#         # print(row[0])
#     fname = row[0]
#     lname = row[1]
#     age = row[2]
#     sex = row[3]
#     income = row[4]
#     # 打印结果
#     print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" %
#                 (fname, lname, age, sex, income))
# except:
#     print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
