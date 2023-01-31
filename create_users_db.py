import sqlite3

connection = sqlite3.connect('Users.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
    (User_id INT, FirstName TEXT, LastName TEXT, Email TEXT)''')

#cursor.execute("INSERT INTO Users VALUES (1, 'Bob', 'Smith', 'bsmith@gmail.com')")

initUsers = [(1, 'Bob', 'Smith', 'bsmith@gmail.com'),
(2, 'Jane', 'Smith', 'jsmith@gmail.com'),
(3, 'Alan', 'Smith', 'asmith@gmail.com'),
(4, 'Ethan', 'Smith', 'esmith@gmail.com'),
(5, 'Ryan', 'Smith', 'rsmith@gmail.com')]

cursor.executemany('INSERT INTO Users VALUES (?,?,?,?)', initUsers)

cursor.execute("SELECT Email FROM Users")

print(cursor.fetchall())

connection.commit()
connection.close()
