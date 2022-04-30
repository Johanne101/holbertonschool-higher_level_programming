#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
