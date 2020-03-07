import sqlite3 as a

db = a.connect("todo")



def createTable():
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todolist(Event TEXT, Date TEXT, Priority TEXT,Completed INTEGER DEFAULT 0,Username TEXT)''')
    print(cursor.fetchall())
    cursor.close()

def readIncomplete(t):
    cursor = db.cursor()
    cursor.execute('''SELECT Event, Date, Priority FROM todolist WHERE Completed = 0 AND Username = ?''',(t,))
    lst = cursor.fetchall()
    y = ""
    lst1 = []
    for k in lst:
        y=''
        for i in k:
            for j in i:
                y+= j
            y += " "
        lst1.append(y.strip())
    cursor.close()
    return lst1

def readCompleted(t):
    cursor = db.cursor()
    cursor.execute("SELECT Event, Date, Priority FROM todolist WHERE Completed = 1 AND Username = ?",(t,))
    lst = cursor.fetchall()
    y = ""
    lst1 = []
    for k in lst:
        y=''
        for i in k:
            for j in i:
                y+= j
            y += " "
        lst1.append(y.strip())
    cursor.close()
    return lst1

def deleteTable():
    cursor = db.cursor()
    cursor.execute("DELETE from todolist")
    cursor.close()

def addEvent(lst,t):
    cursor = db.cursor()
    #lst = ['qwe 123 1', 'qswe 123 12']
    for i in range(len(lst)):
        y  =''
        y = lst[i].split()
    cursor.execute('''INSERT INTO todolist(Event,Date,Priority,Username) values(?,?,?,?)''',(y[0],y[1],int(y[3]),t))
    cursor.execute("SELECT * FROM todolist WHERE Username = ?",(t,))
    print(cursor.fetchall())
    cursor.close()
    db.commit()

def deleteEvent(x,t):
    #x is string-  event
    cursor = db.cursor()
    y=''
    y = x.split()
    print(" y is : ",y)
    print(type(y))
    cursor.execute('DELETE FROM todolist WHERE Event = ? AND Username = ?',(y[0],t))
    cursor.close()
    db.commit()

def completedEvent(x,t):
    cursor = db.cursor()
    print("x is:", x)
    y,z = "",""
    y = x.split()[0]
    z = x.split()[1]
    print(y)
    #update tablename set event =  where id =
    cursor.execute('''UPDATE todolist SET Completed = 1 WHERE Event = ? AND Date = ? AND Username = ?''',(y,z,t))
    print("Check completed:")
    cursor.execute('SELECT * FROM todolist WHERE Username = ?',(t,))
    print(cursor.fetchall())
    db.commit()
    cursor.close()

def prioritizeEvents(t):
    cursor = db.cursor()
    lst = []
    cursor.execute("CREATE TABLE IF NOT EXISTS tl(Event TEXT, Date TEXT, Priority TEXT,Completed INTEGER DEFAULT 0,Username TEXT)")
    cursor.execute("INSERT INTO tl(Event,Date,Priority,Completed,Username) SELECT * FROM todolist WHERE Completed = 0 AND Username =? ORDER BY Date,Priority",(t,))
    cursor.execute("DROP TABLE todolist")
    cursor.execute("ALTER TABLE tl RENAME TO todolist")
    cursor.execute("SELECT Event, Date, Priority FROM todolist WHERE Completed = 0 AND Username = ? ORDER BY Date, Priority",(t,))
    lst = cursor.fetchall()
    y = ""
    lst1 = []
    for k in lst:
        y=''
        for i in k:
            for j in i:
                y+= j
            y += " "
        lst1.append(y.strip())
    print("lst1 = ",lst1)
    db.commit()
    cursor.close()
    return lst1

def createUsers():
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(Name TEXT, email TEXT UNIQUE,
    Username TEXT UNIQUE,Password TEXT)''')
    print(cursor.fetchall())
    cursor.close()

def searchUsers(x,y):
    cursor = db.cursor()
    print("x is:", x)
    print(y)
    #print(z)
    cursor.execute('''SELECT * FROM users WHERE Username = ? 
    AND Password = ? ''',(x,y))
    res = []
    #try:
    res = cursor.fetchall()
    if(res == []):
        return 0
    else:
        return 1


def addUser(lst):
    cursor = db.cursor()
    #lst = ['qwe 123 1', 'qswe 123 12']
    #for i in range(len(lst)):
    #    y = lst[i].split()
    print(lst)
    cursor.execute('''INSERT INTO users(Name,email,Username,Password) values(?,?,?,?)''',(lst[0],lst[1],lst[2],lst[3]))
    cursor.execute("SELECT * FROM users")
    print("Values in DB : ")
    print(cursor.fetchall())
    cursor.close()
    db.commit()
