import ipdb
from classes.coffee import Coffee


class Customer:    
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.coffees = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise AttributeError("Must be a string with a loength between 1 and 15")

    def __repr__(self):
        return f"Customer: {self.name}"

    def access_current_transactions(self, new_transaction=None):
        from classes.transaction import Transaction
        if isinstance(new_transaction, Transaction):
            self.transactions.append(new_transaction)
        return self.transactions

        

    def access_current_coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee) and new_coffee not in self.coffees:
            self.coffees.append(new_coffee)
        return self.coffees

    def place_order(self, name_of_coffee, price):
        from classes.transaction import Transaction
        from classes.coffee import Coffee
        new_coffee = Coffee(name_of_coffee)
        return Transaction(self, new_coffee, price)

    def calculate_total_money_spent(self):
        total_spent = 0
        for transaction in self.transactions:
            total_spent += transaction.price
        return total_spent
    
    def retrieve_coffees_within_price_range(self, min_price=0, max_price=999):
        new_coffee_list =  [transaction.coffee for transaction in self.transactions if min_price <= transaction.price <= max_price]
        return new_coffee_list


test = Customer("bob")
test.place_order("Espresso", 15)
test2 = Coffee("Espresso")
print(type(test.access_current_coffees()[0]))
print(type(test2))
print(test.access_current_coffees()[0] in test.access_current_coffees())

