import unittest
import todo_list as tl
import datetime
import psycopg2

CONN = psycopg2.connect("dbname=todo_list_test user=postgres password = 25356256")
date = datetime.date(2023, 11, 4)
date2 = datetime.date(2021, 11, 25)
tl.Task.conn = CONN


def db_select_tasks():
    cur = CONN.cursor()
    cur.execute('SELECT id, title, creation_date, done FROM tasks;')
    return cur.fetchall()


def db_delete_all_tasks():
    cur = CONN.cursor()
    cur.execute('DELETE FROM tasks;')
    CONN.commit()


class TaskTestCase(unittest.TestCase):
    def setUp(self):
        db_delete_all_tasks()

    def test_constructor(self):
        t = tl.Task(id=123, title='hello', creation_date=date, done=True)
        self.assertEqual(t.id, 123)
        self.assertEqual(t.title, 'hello')
        self.assertEqual(t.creation_date, date)
        self.assertEqual(t.done, True)

    def test_save(self):
        t = tl.Task(id=123, title='hello', creation_date=date, done=True)
        tasks = db_select_tasks()
        self.assertEqual(len(tasks), 0)
        t.save()
        tasks = db_select_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][0], t.id)
        self.assertEqual(tasks[0][1], t.title)
        self.assertEqual(tasks[0][2], t.creation_date)
        self.assertEqual(tasks[0][3], t.done)

    def test_mark_as_done(self):
        t = tl.Task(id=123, title='hello', creation_date=date, done=False)
        t.save()
        tasks = db_select_tasks()
        self.assertFalse(tasks[0][3])
        t.mark_as_done()
        tasks = db_select_tasks()
        self.assertTrue(tasks[0][3])
        self.assertTrue(t.done)

    def test_delete(self):
        t1 = tl.Task(id=1, title='hello', creation_date=date, done=False)
        t2 = tl.Task(id=2, title='hello', creation_date=date, done=False)
        t1.save()
        t2.save()
        tasks = db_select_tasks()
        self.assertEqual(len(tasks), 2)
        t1.delete()
        tasks = db_select_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][0], t2.id)

    def test_str(self):
        t1 = tl.Task(id=1, title='hello', creation_date=date, done=False)
        t2 = tl.Task(id=2, title='good-bye', creation_date=date2, done=True)
        self.assertEqual(t1.__str__(), '1. hello [2023-11-04]')
        self.assertEqual(t2.__str__(), '2. good-bye [2021-11-25] DONE')

    def test_all(self):
        t1 = tl.Task(id=1, title='hello', creation_date=date, done=False)
        t2 = tl.Task(id=2, title='hello', creation_date=date, done=False)
        t3 = tl.Task(id=3, title='hello', creation_date=date, done=False)
        t1.save()
        t2.save()
        t3.save()
        tasks = tl.Task.all()
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].id, t1.id)
        self.assertEqual(tasks[0].title, t1.title)
        self.assertEqual(tasks[0].creation_date, t1.creation_date)
        self.assertEqual(tasks[0].done, t1.done)

    def test_find(self):
        t1 = tl.Task(id=456, title='hello', creation_date=date, done=False)
        t1.save()
        task = tl.Task.find(123)
        self.assertEqual(task, None)
        task = tl.Task.find(456)
        self.assertEqual(task.id, t1.id)
        self.assertEqual(task.title, t1.title)
        self.assertEqual(task.creation_date, t1.creation_date)
        self.assertEqual(task.done, t1.done)


if __name__ == '__main__':
    unittest.main()
