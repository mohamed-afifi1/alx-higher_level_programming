#!/usr/bin/python3
"""  lists names states that validate from the database hbtn_0e_0_usa """

if __name__ == '__main__':

    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]
    mydb = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        database=database,
        port=3306)
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT cities.name
                FROM cities LEFT JOIN states
                ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (search_name, ))
    print(", ".join([row[0] for row in mycursor]))
    mycursor.close()
    mydb.close()
