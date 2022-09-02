import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert, user)

users = [ 
    (2, 'rolf', 'asdf'),
    (3, 'bob', 'xyz')
]
cursor.executemany(insert, users)

select_query = "SELECT * FROM users"
for i in cursor.execute(select_query):  #this is just for knowledge
    print(i)

connection.commit()
connection.close()