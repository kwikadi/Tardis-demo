import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class AtomicData(Base):
    __tablename__ = 'atomicdata'

    pri_key = Column(Integer, primary_key=True)
    atomic_number = Column(Integer)
    atomic_symbol = Column(String(5))
    mass_number = Column(Integer)
    rel_atomic_mass = Column(String(50))
    isotopic_composition = Column(String(50))
    std_atomic_wt = Column(String(50))
    notes = Column(String(50))

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.create_all(engine)
