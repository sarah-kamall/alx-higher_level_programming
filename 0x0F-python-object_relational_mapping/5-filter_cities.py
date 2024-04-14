#!/usr/bin/python3
"""  lists all states from the database ::hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = connection.cursor()
    query = ("SELECT c.name FROM cities AS c "
             ",states AS s "
             "WHERE c.state_id = s.id AND s.name = %s "
             "ORDER BY c.id ASC;")
    cur.execute(query, (sys.argv[4], ))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end="")
        if i < len(rows) - 1:
            print(", ", end="")
    cur.close()
    connection.close()
