from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, ARRAY, text
from database.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    ingredients = Column(ARRAY(String), nullable=False)
    directions = Column(ARRAY(String), nullable=False)
    ner = Column(ARRAY(String), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    disabled = Column(Boolean, unique=False,nullable=False)
