#coding=utf8
import requests
import itchat
import pymysql
import io
import sys
import time
# import urllib
from urllib.parse import quote

TULINGKEY = 'a553ec404b0a4ffba3349e5b2e6ed319'
HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWD = 'root'
DB = 'videocms'
CHARSET = 'utf8'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': TULINGKEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

# 获取视频数据
def get_video(name):
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                         passwd='root', db='videocms', charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT count(*) FROM baiyug_vod WHERE d_name like '%%%s%%'" % (name)
    # try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    # print(results[0])
    if results[0] > 0:
        # print(results[0])
        video_link = 'http://videocms.net/index.php?m=vod-search-wd-%s' % quote(name)
    else:
        return
    # print
    db.close()
    return video_link



@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])

    video_reply = get_video(msg['Text'])
    time.sleep(2)
    return video_reply or reply

itchat.auto_login(hotReload=True)
itchat.run()

