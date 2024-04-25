products = []

def sell(product):
    pass

def restock(product, amount):
    pass

def displayProducts():
    # Product name: Sugar
    # price: 80 birr/Kg
    for product in products:
        print(f"Product name: {product["name"]}\nPrice: {product["price"]} {product["currency"]}/{product["unit"]}")
        print()

def createProduct(*, name:str, price:float, unit:str, currency:str):
    product = {"name": name, "price": price, "unit": unit, "currency": currency}
    products.append(product)

createProduct(name="Sugar", price=90.5, unit="Kg", currency="birr")
createProduct(name="Jordan Shoe", price=3000, unit="piece", currency="birr")
displayProducts()