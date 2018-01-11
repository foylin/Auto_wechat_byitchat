import pymysql
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# keywords = input()
keywords = '舞蹈'
# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='root', db='videocms', charset='utf8')

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
print("%d" % results)
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
