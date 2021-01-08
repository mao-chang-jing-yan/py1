import time

from requ.book import Book
import pymysql

keys = {
    'name',
    'content',
    'url',
    '原书定价',
    '主题词',
    '出版项',
    'groupid',
    '丛书名',
    'ISBN号',
    '形态项',
    'adid',
    '参考文献格式',
    'img_url',
    '作者',
    '中图法分类号'
}


#
# {"name": i["name"],
#  "content": i["content"],
#  "url": i["url"],
#  "price": i["原书定价"],
#  "main_word": i["主题词"],
#  "public_library": i["出版项"],
#  "group_id": i["groupid"],
#  "books_name": i["丛书名"],
#  "isbn_card": i["ISBN号"],
#  "state_card": i["形态项"],
#  "adid": i["adid"],
#  "base_content_type": i["参考文献格式"],
#  "img_url": i["img_url"],
#  "maker": i["作者"],
#  "type_card": i["中图法分类号"]
#  }


def book_list_insert(jn):
    db = pymysql.connect("182.61.144.236", "mao", "123456", "school", charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("SELECT * from my")

    sql = "replace into book_list(" \
          "name, content,url," \
          "price,main_word,public_library," \
          "group_id,books_name,isbn_card,state_card,adid," \
          "base_content_type,img_url,maker,type_card" \
          "" \
          ") values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
          % (
              jn["name"],
              jn["content"],
              jn["url"],
              jn["price"],
              jn["main_word"],
              jn["public_library"],
              jn["group_id"],
              jn["books_name"],
              jn["isbn_card"],
              jn["state_card"],
              jn["adid"],
              jn["base_content_type"],
              jn["img_url"],
              jn["maker"],
              jn["type_card"],
          )
    # cursor = db.cursor()
    cursor.execute('alter table book_list character set utf8;')

    try:
        cursor.execute(sql)
        db.commit()  # 提交到数据库执行，一定要记提交哦
    except Exception as e:
        db.rollback()  # 发生错误时回滚
        print(e)


if __name__ == '__main__':
    kw = [
        # "历史",
        # "唐朝",
        # "南",
        # "毛泽东",
        # "星球",
        # "世界",
        # "宇宙",
        # "爆炸",
    ]
    for j in kw:
        try:
            s = Book(j).search()

            for i in s:
                # i["name"] = str(i["name"])
                # print(i["name"])
                book_list_insert(i)
            print(j)
            time.sleep(5)
        except Exception as e:
            print(e)

# w = s[0]["groupid"]
# flag = 0
# for i in range(len(s)):
#     if s[i]["groupid"] == w:
#         flag += 1
#
# print(flag, len(s))

#
# # 打开数据库连接
# db = pymysql.connect("182.61.144.236", "mao", "123456", "school")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# # cursor.execute("SELECT * from my")
#
# sql = "insert into test2(url, time) values('%s','%s')" % ("url", "Time")
# # cursor = db.cursor()
# try:
#     cursor.execute(sql)
#     db.commit()  # 提交到数据库执行，一定要记提交哦
# except Exception as e:
#     db.rollback()  # 发生错误时回滚
#     print(e)
#
# cursor.close()
#
# db.close()
