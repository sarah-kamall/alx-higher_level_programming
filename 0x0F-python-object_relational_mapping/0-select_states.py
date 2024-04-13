#!/bin/python3
import sys
import MySQLdb

args= sys.argv
if len(args)< 4:
    exit()

    
mysql_username=args[1]
mysql_password=args[2]
database_name=args[3]

# Establishing a connection to the MySQL server
connection = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name
    )

if connection:
    print("Connected to MySQL server")
   
