import sqlite3


def execute_query(sql_query):
    """
    function to execute sql commands
    :return: returns values if select command used
    """
    # print(sql_query)
    with sqlite3.connect("todo.db") as con:
        cur = con.cursor()
        result = cur.execute(sql_query)
        con.commit()
    return result


def add_todo_item(text):
    """
    function to add todo text into the database
    :param text: text input by the user
    :return: None
    """
    sql_query = """insert into Todo(text,complete) VALUES ( '%s',%s )""" % (text, 0)
    execute_query(sql_query)


def mark_complete(id):
    """
    function to change the todo status as complete
    :param id: id of the todo item
    :return: None
    """
    sql_query = """UPDATE Todo set complete= %s where id= %s""" % (1, id)
    execute_query(sql_query)


def get_complete():
    """
    function to get all complete todo items
    :return: items marked as done or 1 in the database
    """
    sql_query = """select * from Todo where complete = 1"""
    return execute_query(sql_query).fetchall()


def get_incomplete():
    """
    function to get all incomplete todo items
    :return: items marked as not done or 0 in the database
    """
    sql_query = """select * from Todo where complete = 0"""
    return execute_query(sql_query).fetchall()

