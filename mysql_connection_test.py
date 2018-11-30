import MySQLdb

conn = MySQLdb.connect(
    user='root',
    passwd='',
    host='127.0.0.1',
    db='sample',
    port=3306
)


# カーソルを取得する
cur = conn.cursor()
print(cur)

# # 初期化
# cur.execute("create table stock")
# cur.execute("delete from SYNONYM_RELATIONS;")
# conn.commit()
#
# # Insert実行
# for i in range(1000):
#     cur.execute("insert into SYNONYM_RELATIONS values (%s, %s);", ("Synonym" + str(i), "Representative" + str(i)))
#
# conn.commit()
#
# cur.execute("select * from SYNONYM_RELATIONS;")
# print(cur.rowcount)
# # print(cur.fetchall())
conn.close()
