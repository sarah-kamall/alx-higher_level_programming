#!/bin/python3
import sys
import MySQLdb


def list_states(username, password, database):

   
# Establishing a connection to the MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    try:
        if connection:
            print("Connected to MySQL server")
            myCursor=connection.cursor()
            myCursor.execute("SELECT * FROM states ORDER BY id ASC")
            states=myCursor.fetchall()
            for state in states:
                print(state)
    except:
        exit()
if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        exit()

    username, password, database = sys.argv[1:]
    list_states(username, password, database)
        
