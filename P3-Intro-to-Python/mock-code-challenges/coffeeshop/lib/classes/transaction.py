from classes.customer import Customer
from classes.coffee import Coffee
import ipdb

class Transaction:
    counter, catalog = 0, []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Transaction.counter += 1
        Transaction.catalog.append(self)

        self.coffee.access_current_transactions(self)
        self.coffee.access_current_customers(customer)
        self.customer.access_current_transactions(self)
        self.customer.access_current_coffees(coffee)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if 1 <= price <= 50:
            self._price = price
        else:
            raise AttributeError("Price must be between 1 and 50")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise AttributeError("Customer must be type Customer")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise AttributeError("Coffee must be a Coffee instance")

    def __repr__(self):
        return f"{self.customer.name} ordered a {self.coffee.name} for ${self.price}."