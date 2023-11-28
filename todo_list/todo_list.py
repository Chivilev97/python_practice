import psycopg2
import datetime


class Task():
    conn = psycopg2.connect("dbname=todo_list user=postgres password = 25356256")

    @classmethod
    def all(cls):
        all_tasks = []
        cur = cls.conn.cursor()
        cur.execute('SELECT id, title, creation_date, done FROM tasks;')
        task_records = cur.fetchall()
        for t in task_records:
            task = Task(t[0], t[1], t[2], t[3])
            all_tasks.append(task)
        return all_tasks

    @classmethod
    def find(cls, id):
        cur = cls.conn.cursor()
        cur.execute('SELECT id, title, creation_date, done FROM tasks WHERE id = %s;', [id])
        task_record = cur.fetchone()
        if task_record:
            return Task(task_record[0], task_record[1], task_record[2], task_record[3])

    def __init__(self, id, title, creation_date, done):
        self.id = id
        self.title = title
        self.creation_date = creation_date
        self.done = done

    def save(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO tasks (id, title, creation_date, done) VALUES (%s,%s,%s,%s);",
                    [self.id, self.title, self.creation_date, self.done])
        self.conn.commit()

    def mark_as_done(self):
        cur = self.conn.cursor()
        cur.execute("UPDATE tasks SET done = 't' WHERE id = %s;", [self.id])
        self.conn.commit()
        self.done = True

    def delete(self):
        cur = self.conn.cursor()
        cur.execute('DELETE FROM tasks WHERE id = %s;', [self.id])
        self.conn.commit()

    def __str__(self):
        return f"{self.id}. {self.title} [{self.creation_date}]{' DONE' if self.done else ''}"


def add_tasks():
    while True:
        task_title = input('Введите задачу: ')
        if task_title == '':
            break
        else:
            today = datetime.date.today()
            task_ids = map(lambda t: t.id, Task.all())
            task = Task(max(task_ids) + 1, task_title, today, False)
            task.save()


def print_task_list(tasks):
    if len(tasks) == 0:
        print('Нет задач')
    else:
        for t in tasks:
            print(t)


def quit():
    print('До свидания')
    Task.conn.close()
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
            print_task_list(Task.all())
        elif menu_item == 'd':
            task_id = int(input('Номер задачи: '))
            task = Task.find(task_id)
            task.delete()
        elif menu_item == 'm':
            task_id = int(input('Номер задачи: '))
            task = Task.find(task_id)
            task.mark_as_done()
        elif menu_item == 'q':
            quit()
