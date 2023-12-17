#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

    # Close the session
    session.close()

