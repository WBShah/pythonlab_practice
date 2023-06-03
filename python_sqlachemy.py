from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the database engine
engine = create_engine('sqlite:///ecommerce.db', echo =True)


# Create a session Factory
Session = sessionmaker(bind=engine)
session = Session()


# Create the base class for declarative models
Base = declarative_base()

# Define the customer model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    orders = relationship('Order', back_populates='customer')

# Define the Order model
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    product = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)

    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='orders')

# Create the database tables
Base.metadata.create_all(engine)

# Creating an instance of the Customer class
#customer1 = Customer(name = 'John Doe', email = 'john.doe@example.com')
#customer2 = Customer(name = 'Jane Smith', email ='jane.smith@example.com')
#customer3 = Customer(name = 'Alice Johnson', email = 'alice.johnson@example.com')

# Creating an instance of the Order class
#order1 = Order(product='Laptop', quantity=2)
#order2 = Order(product='Phone', quantity=1)
#order3 = Order(product='Tablet', quantity=3)

#customer1.orders.append(order1)
#customer2.orders.append(order2)
#customer3.orders.append(order3)

# Add the objects to the session and commit
#session.add_all([customer1, customer2, customer3])
#session.commit()

# Query the data
customers = session.query(Customer).all()
#for customer in customers:
    #print(customer.name)
for order in customer.orders:
    print(f'-{order.product}: {order.quantity}')
