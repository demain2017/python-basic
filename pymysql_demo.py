import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
"""
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
"""

#创建表
"""
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
cursor.execute(sql)
"""

#插入数据
"""
事务的四个特性
原子性（atomicity）

事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做

一致性（consistency）

事务必须使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的

隔离性（isolation）

一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰

持久性（durability）

持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响
"""
"""
id = '20130001'
user = 'Bob'
age = 20

sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()  #执行失败,则调用rollback()执行数据回滚
"""
#更新数据
"""
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except:
    db.rollback()
"""
#删除数据
"""
table = 'students'
condition = 'age > 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table = table, condition = condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
"""
#查询数据
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')
db.close()

