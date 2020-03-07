import sqlite3

conn = sqlite3.connect('todo.db')

sql_query = """
CREATE TABLE IF NOT EXISTS Todo (
  id INTEGER PRIMARY KEY,
  text TEXT,
  complete boolean
);
"""

conn.execute(sql_query)
conn.close()