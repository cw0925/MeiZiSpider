# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
# 连接数据库
def dbHandle():
    conn = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="1225",
        charset="utf8",
        db="MeiZi"
    )
    print('连接成功***********')
    return conn


class MeiziPipeline(object):

    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE MeiZi")
        sql = "INSERT INTO home_meizi(title,imgurl,url) VALUES(%s,%s,%s)"
        try:
            cursor.execute(sql, (item["title"], item["img"],item["nexturl"]))
            cursor.connection.commit()
            # dbObject.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item

