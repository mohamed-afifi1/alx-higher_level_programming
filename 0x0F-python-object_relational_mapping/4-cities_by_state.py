#!/usr/bin/python3
"""  lists names states that validate from the database hbtn_0e_0_usa """

if __name__ == '__main__':

    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    mydb = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        database=database,
        port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT cities.id, cities.name, states.name
                FROM cities LEFT JOIN states
                ON states.id = cities.state_id
                ORDER BY cities.id ASC""")
    for row in mycursor:
        print(row)
    mycursor.close()
    mydb.close()
