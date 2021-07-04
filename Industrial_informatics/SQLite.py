import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect(':memory:')
conn.row_factory = dict_factory
##conn = sqlite3.connect('fastoryDB.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS robot (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             brand text,
             operationType text,
             numberJoints integer
             );""")

#CREATE
def insert_robot(brand,operationType,numberJoints):
    with conn:
        c.execute("INSERT INTO robot VALUES (:id,:brand, :operationType, :numberJoints)", {'id':None,'brand': brand, 'operationType': operationType, 'numberJoints': numberJoints})

#READ
def get_robots_by_brand(brand):
    #c.execute("SELECT * FROM robot WHERE brand=:brand", {'brand': brand})
    sqlSt="SELECT * FROM robot WHERE brand='"+brand+"'"
    c.execute(sqlSt)
    return c.fetchall()
#READ
def get_all_robots():
    #c.execute("SELECT * FROM robot WHERE brand=:brand", {'brand': brand})
    sqlSt="SELECT * FROM robot WHERE 1"
    c.execute(sqlSt)
    return c.fetchall()

#UPDATE
def update_operation_type(robID, operationType):
    with conn:
        c.execute("""UPDATE robot SET operationType = :operationType
                    WHERE id = :id""",
                  {'id': robID,'operationType':operationType})

#DELETE
def remove_robot(robID):
    with conn:
        c.execute("DELETE from robot WHERE id = :id",
                  {'id': robID})


#from here we manipulate the Database

insert_robot('ABB', 'welding', 6)
insert_robot('KUKA', 'assembly', 4)
insert_robot('ABB', 'assembly', 5)

print ("ABB robots")
robots = get_robots_by_brand('ABB')
print(robots)


robots=get_all_robots()
print ("All robots")
print(robots)


update_operation_type(2,"welding")


robots=get_all_robots()
print ("All robots after update")
print(robots)
exit()

remove_robot(2)
robots=get_all_robots()
print ("All robots after delete")
print(robots)


conn.close()
