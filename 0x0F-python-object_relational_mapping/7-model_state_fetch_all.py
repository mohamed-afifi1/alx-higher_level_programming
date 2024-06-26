#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = session(engine)
    data = session.query(State).order_by(State.id).all()
    for row in data:
        print("{}: {}".format(row.id, row.name))
