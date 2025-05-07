import sqlite3

# 连接到SQLite数据库（如果不存在会创建）
con = sqlite3.connect('student.db')
cur = con.cursor()

# 如果表已存在，先删除它
cur.execute("DROP TABLE IF EXISTS student")

# 创建新表
cur.execute("CREATE TABLE student(id integer primary key autoincrement, name text not null, age integer not null)")

# 如果你需要插入一些测试数据
cur.execute("INSERT INTO student (name, age) VALUES ('张三', 20)")
cur.execute("INSERT INTO student (name, age) VALUES ('李四', 22)")
con.commit()

res = cur.execute("select * from student")
print(res.fetchall())

# 关闭连接
con.close()