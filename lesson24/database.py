import sqlite3

connection = sqlite3.connect('afk_database.db')

cursor = connection.cursor()

cursor.execute(''' create table if not exists users (
    id integer primary key autoincrement,
               name text not null,
               postition text not null,
               department text not null,
               salery Real''')

connection.commit()

cursor.execute('''
               instert into users (name, position, department, salery) values(?, ?, ?, ?)
               ''', ('John Doe', 'Software Engineer', 'IT', 75000.0))

connection.commit()


cursor.execute(''' select * from users ''')

rows = cursor.fetchall()

for row in rows:
    print(row)



cursor.execute(''' update users set salery = ? where name = ? ''', (80000.0, 'Germanium'))


cursor.execute(''' delete from users where name = ? ''', ('John Doe',)  )
connection.commit()

cursor.close()
connection.close()


