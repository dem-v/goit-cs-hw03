from datetime import datetime
import faker
from random import randint, choice
import psycopg2 as pg

NUMBER_USERS = 5
NUMBER_STATUSES = 3
NUMBER_TASKS = 30

PG_CONN = "postgresql://postgres:pass@localhost:5432/postgres"

def generate_fake_data(number_users, number_status, number_tasks) -> tuple():
    fake_users = []
    fake_status = []
    fake_tasks = []

    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    #for _ in range(number_status):
    fake_status.append('new')
    fake_status.append('in progress')
    fake_status.append('completed')

    for _ in range(number_tasks):
        fake_tasks.append((fake_data.word(), fake_data.sentence(nb_words=5)))

    return fake_users, fake_status, fake_tasks


def prepare_data(users, status, tasks) -> tuple():
    for_users = []
    for_status = []
    for_tasks = []

    # для таблиці users
    for u in users:
        for_users.append((*u, ))

    # для таблиці status
    for s in status:
        for_status.append((s, ))

    # для таблиці tasks
    for t in tasks:
        for_tasks.append((*t, choice(status), choice([u[0] for u in for_users])))

    return for_users, for_status, for_tasks


def insert_data_to_db(users, status, tasks) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними

    with pg.connect(PG_CONN) as con:

        cur = con.cursor()

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (%s,%s)"""
        cur.executemany(sql_to_users, users)

        sql_to_status = """INSERT INTO status(name)
                               VALUES (%s)"""
        cur.executemany(sql_to_status, status)

        sql_to_tasks = """INSERT INTO tasks(name, description, status_id, user_id)
                              SELECT %s, %s, status.id, users.id
                              FROM status, users
                              WHERE status.name = %s AND users.fullname = %s"""
        cur.executemany(sql_to_tasks, tasks)

        con.commit()


if __name__ == "__main__":
    users, status, posts = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_STATUSES, NUMBER_TASKS))
    print(users, status, posts)
    insert_data_to_db(users, status, posts)

