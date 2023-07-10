import sqlite3 as sql

students = [
    ('Ivan', 'Junior'),
    ('Dmytro', 'Junior'),
    ('Petr', 'Middle'),
    ('Ivan', 'Junior'),
    ('Petr', 'Junior'),
    ('Sergey', 'Senior'),
    ('Olga', 'Junior'),
    ('Maria', 'Junior')
]

try:
    with sql.connect('mydatabase.db') as cur:
        cur = cur.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            t_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            subject TEXT
        )""")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            exp_level TEXT NOT NULL
        )""")

        cur.execute("""
            INSERT OR IGNORE INTO teachers VALUES (1, "Ivan", "Python")
        """)

        """Команды снимать с коммента поочередно, чтобы увидеть результат шаг за шагом"""

        # Добавляем студентов из списка в таблицу
        # cur.executemany("INSERT OR IGNORE INTO students (name, exp_level) VALUES (?, ?)", students)

        # Обновляем уровень опыта студентов с именем, которое начинается на P на Middle
        # cur.execute("""
        #     UPDATE students SET exp_level = 'Middle' WHERE name LIKE 'P%' AND exp_level = 'Junior'
        # """)

        # Удаляем студентов со статусом Senior
        # cur.execute("""
        #     DELETE FROM students WHERE exp_level = "Senior"
        # """)

        # Удаляем студента с id = 1
        # cur.execute("""
        #     DELETE FROM students WHERE user_id = 1
        # """)

except sql.Error as e:
    print('Something happened with your database:', e)
except Exception as y:
    print('Something happened with my code', y)
finally:
    cur.close()
