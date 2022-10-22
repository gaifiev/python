import sqlite3

bd = sqlite3.connect("Data_base.db")

cursor = bd.cursor()

cursor.execute('DELETE from personal WHERE id=1')

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)
