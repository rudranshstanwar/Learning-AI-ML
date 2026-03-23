class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"The price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total product is store is {Product.count}")

    @staticmethod
    def calc_discount(price, percentage):
        print(f"Final price = {price - (price*percentage/100)}")

ptd1 = Product("Phone", 9000)


