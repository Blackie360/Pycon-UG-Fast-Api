from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base

# SQLite database URL
DATABASE_URL = "sqlite:///./database.db"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables
Base.metadata.create_all(bind=engine)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
