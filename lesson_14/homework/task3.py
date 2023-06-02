class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise TypeError("Wrong type of product")
        self.products.append((product, amount))
        print(f"In stock: {self.products}")

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            products = [prod for prod in self.products if prod[0].name == identifier]
        elif identifier_type == 'type':
            products = [prod for prod in self.products if prod[0].type == identifier]
        else:
            raise ValueError("Wrong identifier type")

        if not products:
            raise ValueError("No products found")

        for product, amount in products:
            product.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        for i, (product, stock) in enumerate(self.products):
            if product.name == product_name:
                if stock >= amount:
                    self.products[i] = (product, stock - amount)
                    self.income += product.price * amount
                    print(f"Sold {amount} of {product_name}")
                    print(f"In stock: {self.products}")
                    break
                else:
                    raise ValueError("Sorry, we dont have required amount of product")
        else:
            raise ValueError("Product not found")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product.name, stock) for product, stock in self.products]

    def get_product_info(self, product_name):
        for product, stock in self.products:
            if product.name == product_name:
                return product.name, stock
        else:
            raise ValueError("Product not found")


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)