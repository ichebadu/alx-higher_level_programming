#!/usr/bin/python3
""" list all states from the data base """
import MYSQLdb
import sys

if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cusor()
    cursor.execute("SELECT * FROM states")
    rows  = cursor.fetchall()
    for numRow in rows:
        print(row)
    cursor.close()
    db.close()
