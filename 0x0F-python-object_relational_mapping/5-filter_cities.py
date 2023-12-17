#!/usr/bin/python3
'''write a script that takes in arguments and displays'''
import MySQLdb
import sys


def main():
    # makes conn and executes query
    # Retrieve command-line arguments
    username, password, database, state_name = sys.argv[1],\
        sys.argv[2], sys.argv[3], sys.argv[4]
    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query to select states with a matching name
    query = """
        SELECT cities.name FROM cities JOIN states ON\
        cities.state_id = states.id AND states.name = %s ORDER BY cities.id ASC
        """
    cursor.execute(query, (state_name,))
    # Fetch all the results
    result = cursor.fetchall()
    ll = [x[0] for x in result]
    total = ", ".join(ll)
    print(total)
    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    from sys import argv
    main()
