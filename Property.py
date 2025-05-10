class Product:
    def __init__(self, price):
        self._price = price
    
    # Getter for price
    @property
    def price(self):
        return self._price
    
    # Setter for price
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Price cannot be negative")
    
    # Deleter for price
    @price.deleter
    def price(self):
        print("Price is being deleted")
        del self._price

# Example usage
product = Product(100)
print(product.price)  # Using getter

product.price = 150  # Using setter
print(product.price)

del product.price  # Using deleter
