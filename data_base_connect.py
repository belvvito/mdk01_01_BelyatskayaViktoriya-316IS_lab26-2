import sqlite3

connection = sqlite3.connect('students.db')

cursor = connection.cursor()

cursor.execute('''create table if not exists students (
                    id_student integer primary key autoincrement,
                    fio varchar(150) not null,
                    phone varchar(30),
                    address varchar(100),
                    course_number integer not null,
                    group_number varchar(10) not null
                )''')

cursor.execute('''create table if not exists english_grades (
                    id_english_grades integer primary key autoincrement,
                    id_student integer,
                    english_grades integer,
                    foreign key(id_student) references students(id_student)
                )''')
students_data = [
    ('Беляцкая Виктория Александровна', '89993457865', 'б-р Сиреневый', 3, '316ИС-22'),
    ('Пинтеску Анна Мариановна', '89612346734', 'ул.Добрая', 1, '117П-24'),
    ('Алибеков Алибек Шарипович', '89399987654', 'ул.Первомайская', 2, '212ИС-23'),
    ('Хан Варвара Дмитриевна', '89434567893', 'ул.Строгая', 3, '316ИС-22'),
    ('Тян Артур Вячеславович', '89056789078', 'ул.Грусти', 2, '212ЗИО-23')
]

cursor.executemany(
    'INSERT INTO students (fio, phone, address, course_number, group_number) VALUES(?, ?, ?, ?, ?)', students_data)

connection.commit()

cursor.execute('SELECT id_student FROM students')
student_ids = [row[0] for row in cursor.fetchall()]

english_grades_data = [
    (student_ids[0], 5),
    (student_ids[1], 5),
    (student_ids[2], 3),
    (student_ids[3], 4),
    (student_ids[4], 5)
]

cursor.executemany(
    'INSERT INTO english_grades (id_student, english_grades) VALUES(?, ?)', english_grades_data)

connection.commit()

cursor.execute('SELECT * FROM students')
result = cursor.fetchall()

for row in result:
    print(row)

cursor.execute('SELECT * FROM english_grades')
result2 = cursor.fetchall()

for i in result2:
    print(i)

cursor.execute('SELECT * FROM english_grades WHERE english_grades = 5')
result3 = cursor.fetchall()

for i in result3:
    print(i)

connection.close()
