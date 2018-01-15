#!/usr/bin/python
#coding:utf-8

import io
import sys
# from urllib.parse import quote
import urllib
import requests
import itchat
import io
import time
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

# 换取短视频地址
def get_sort_url(url):
    apiurl = "http://suo.im/api.php?url=%s" % url
    url_sort = requests.get(apiurl)
    return url_sort.text

# 获取视频数据
def get_video(name):
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    db = MySQLdb.connect(host=HOST, port=PORT, user=USER,
                         passwd=PASSWD, db=DB, charset = CHARSET)
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
        video_link = 'http://wyingrobot.com/index.php?m=vod-search-wd-%s' % urllib.quote(name)
        return_mas = "已为您搜索到 %d 条信息 \n\n以下为视频链接地址 %s " % (results[0], get_sort_url(video_link))
    else:
        return
    # print
    db.close()
    return return_mas



@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # defaultReply = 'I received: ' + msg['Text']
    # reply = get_response(msg['Text'])
    # $domin = get_sort_url('www.wyingrobot.com');
    reply_none = "暂无该视频资源，请检查您输入的片名是否正确!!\n\n如需查找其他影视资源请可进入站点搜索\n【www.wyingrobot.com】"

    video_reply = get_video(msg['Text'])
    time.sleep(2)
    return video_reply or reply_none

itchat.auto_login(hotReload=True)
itchat.run()

