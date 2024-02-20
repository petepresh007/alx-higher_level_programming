#!/usr/bin/python3
""" Module to test for injection """
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    connection = (
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
            )
    engine = create_engine(connection)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    get_name = (
            session.query(State).filter_by(name='{}'.format(sys.argv[4])).all()
            )
    if not get_name:
        print("Not found")
    else:
        for name in get_name:
            print(name.id)
