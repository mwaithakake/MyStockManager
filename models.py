from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship("Supplier", back_populates="products")

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    products = relationship("Product", back_populates="supplier")
