#!/usr/bin/python3
"""  lists all states from the database ::hbtn_0e_0_usa """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).where(
        State.name.like(sys.argv[4])).order_by(State.id)
    isPrinted = False
    for state in states:
        isPrinted = True
        print(str(state.id))
    if not isPrinted:
        print("Not found")
