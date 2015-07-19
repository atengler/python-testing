import sqlite3

with sqlite3.connect("new.db") as connection:
  c = connection.cursor()

  try:
    c.execute("SELECT city FROM population")
  except sqlite3.OperationalError:
    "Failed to fetch data from database, please try again later ..."

  rows = c.fetchall()
  for r in rows:
    print r[0]