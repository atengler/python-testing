import sqlite3

with sqlite3.connect("new.db") as connection:
  c = connection.cursor()

  cities = [
          ('Boston', 'MA', 600000),
          ('Chicago', 'IL', 2700000),
          ('Houston', 'TX', 2100000),
          ('Phoenix', 'AZ', 1500000)
           ]

  try:
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
  except sqlite3.OperationalError:
    print "Oops! Something went wrong. Try again later..."