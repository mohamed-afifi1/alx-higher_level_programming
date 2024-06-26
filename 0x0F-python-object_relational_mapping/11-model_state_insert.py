#!/usr/bin/python3
"""lists first State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    data = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(data.id))
    session.close()
