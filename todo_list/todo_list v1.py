import psycopg2
import datetime

CONN = psycopg2.connect("dbname=todo_list user=postgres password = 25356256")

# DB FUNCTIONS


def db_delete_task(id):
    cur = CONN.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s;', [id])
    CONN.commit()


def db_insert_task(title, creation_date):
    cur = CONN.cursor()
    cur.execute('SELECT max(id) FROM tasks;')
    max_id = cur.fetchone()[0] or 0
    cur.execute("INSERT INTO tasks (id, title, creation_date, done) VALUES (%s,%s,%s,%s);",
                [max_id + 1, title, creation_date, False])
    CONN.commit()


def db_select_tasks():
    cur = CONN.cursor()
    cur.execute('SELECT id, title, creation_date, done FROM tasks;')
    return cur.fetchall()


def db_mark_task_as_done(task_id):
    cur = CONN.cursor()
    cur.execute("UPDATE tasks SET done = 't' WHERE id = %s;", [task_id])
    CONN.commit()


def add_tasks():
    while True:
        task_title = input('Введите задачу: ')
        if task_title == '':
            break
        else:
            today = datetime.date.today()
            db_insert_task(task_title, today)


def print_task_list(tasks):
    if len(tasks) == 0:
        print('Нет задач')
    else:
        for i in range(len(tasks)):
            task = tasks[i]
            print(f"{task[0]}. {task[1]} [{task[2]}] {'DONE' if task[3] else ''}")


def quit():
    print('До свидания')
    CONN.close()
    exit(0)


if __name__ == '__main__':

    while True:
        print('Todo_list\n'
              'Menu:\n'
              'a - Добавить задачу\n'
              'd - Удалить задачу\n'
              'm - Пометить как выполнено\n'
              'l - Список задач\n'
              'q - Выход')
        menu_item = input('Ваш выбор: ')
        if menu_item == 'a':
            add_tasks()
        elif menu_item == 'l':
            print_task_list(db_select_tasks())
        elif menu_item == 'd':
            task_id = int(input('Номер задачи: '))
            db_delete_task(task_id)
        elif menu_item == 'm':
            task_id = int(input('Номер задачи: '))
            db_mark_task_as_done(task_id)
        elif menu_item == 'q':
            quit()
