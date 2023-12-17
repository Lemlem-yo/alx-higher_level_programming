#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa
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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Check if the State object exists
    if state_to_update:
        # Change the name to "New Mexico"
        state_to_update.name = "New Mexico"

        # Commit the changes to the database
        session.commit()

    # Close the session
    session.close()
