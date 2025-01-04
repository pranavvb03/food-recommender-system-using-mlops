from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    foodID = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cuisine = Column(String, index=True)
    course = Column(String, index=True)
    totalCaloriesInCal = Column(Integer)
    isVeg = Column(Boolean, default=False)
    isSugarFree = Column(Boolean, default=False)
    isHighProtein = Column(Boolean, default=False)
    isGluttenFree = Column(Boolean, default=False)
    isSattvic  =Column(Boolean, default=False)
    isVegan = Column(Boolean, default=False)
  
class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    foodID = Column(Integer, index=True)
    rating = Column(Float)
