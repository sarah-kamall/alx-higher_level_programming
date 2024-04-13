#!/usr/bin/python3
import sys
import MySQLdb

"""  lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        exit()

    username, password, database = sys.argv[1:]
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    try:
        if connection:
            myCursor=connection.cursor()
            myCursor.execute("SELECT * FROM states ORDER BY id ASC")
            states=myCursor.fetchall()
            for state in states:
                print(state)
            myCursor.close()
            connection.close()
    except:
        exit()
        
