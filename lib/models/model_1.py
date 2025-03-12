from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    
    passwords = relationship("PasswordEntry", back_populates="user", cascade="all, delete-orphan")

class PasswordEntry(Base):
    __tablename__ = "passwords"
    
    id = Column(Integer, primary_key=True)
    website = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)  # Encrypted password
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="passwords")

# Database setup
DATABASE_URL = "sqlite:///passwords.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
