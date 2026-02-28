import sqllite3

conn = sqllite3.connect('example.db')
cursor = conn.cursor()

cursor.execute(''' create table if not exists students (
               student_id integer primary key,
               name text
               )
               ''')

cursor.execute('''
               create table if not exists courses (
               course_id integer primary key,
               course_name text,
                student_id integer,
               )
               ''')


cursor.execute(''' insert into students (name) values (alice) ''')
cursor.execute(''' insert into students (name) values (bob) ''')


cursor.execute(''' insert into courses (course_name, student_id) values (math, 1) ''')
cursor.execute(''' insert into courses (course_name, student_id) values (science, 3) ''')
cursor.execute(''' insert into courses (course_name, student_id) values (history, 2) ''')


conn.commit()


#cursor.execute(''' select students.name, courses.course_name from students join courses on students.student_id = courses.student_id ''')

# cursor.execute(''' 
#     select students.name, courses.course_name
#     from students
#     left join courses on students.student_id = courses.student_id
    
               
# ''')


cursor.execute(''' 
    select students.name, courses.course_name
    from students
    right join courses on students.student_id = courses.student_id
    
               
''')


rows = cursor.fetchall()
for row in rows:
    print(f"Student: {row[0]}, Course: {row[1]}")
