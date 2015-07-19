import sqlite3

with sqlite3.connect("new.db") as connection:
  c = connection.cursor()

  try:
    c.execute("UPDATE population SET population = 900000 WHERE city='New York City'")
  except sqlite3.OperationalError as e:
    "Failed to update database data:", e

  try:
    c.execute("DELETE FROM population WHERE city='Boston'")
  except sqlite3.OperationalError as e:
    "Failed to delete database data:", e

  print "\nNEW DATA:\n"

  try:
    c.execute("SELECT * FROM population")
  except sqlite3.OperationalError as e:
    "Failed to fetch database data:", e

  rows = c.fetchall()

  for r in rows:
    print r[0], r[1], r[2]