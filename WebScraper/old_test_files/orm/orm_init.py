from sqlalchemy import create_engine
from models.location import Location
from models.election import Election
from models.office import Office
from models.candidate import Candidate
from models.cfr_page import CFR
from models.crri_page import CRRI
from models.donation import Donation
from base import Base 

engine = create_engine('sqlite:///orm/database.db')


Base.metadata.create_all(engine)
