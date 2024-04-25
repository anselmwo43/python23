products = []

def sell(product):
    pass

def restock(product, amount, unit):
    pass

def displayProducts():
    # Product name: Sugar
    # price: 80 birr/Kg
    pass

def createProduct(*, name:str, price:float, unit:str, currency:str):
    product = {"name": name, "price": price, "unit": unit, "currency": currency}
    products.append(product)
    print(products)

createProduct(name="Sugar", price=90.5, unit="Kg", currency="birr")
createProduct(name="Jordan Shoe", price=3000, unit="piece", currency="birr")