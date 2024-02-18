#!/usr/bin/python3
""" module to select """
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = connection.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    result = cur.fetchall()
    for res in result:
        print(res)
    cur.close()
    connection.close()
