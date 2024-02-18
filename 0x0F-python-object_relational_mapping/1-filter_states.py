#!/usr/bin/python3
""" module to select """
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id")
    result = cur.fetchall()
    for res in result:
        print(res)
    cur.close()
    connection.close()
