from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import AtomicData, Base

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


def insertvals(*args):
    session = DBSession()
    new_data = AtomicData(
        atomic_number=args[0],
        atomic_symbol=args[1],
        mass_number=args[2],
        rel_atomic_mass=args[3],
        isotopic_composition=args[4],
        std_atomic_wt=args[5],
        notes=args[6])
    session.add(new_data)
    session.commit()
