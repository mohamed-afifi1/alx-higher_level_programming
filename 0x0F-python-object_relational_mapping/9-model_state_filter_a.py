#!/usr/bin/python3
"""lists first State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    data = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in data:
        print("{}: {}".format(state.id, state.name))
    session.close()
