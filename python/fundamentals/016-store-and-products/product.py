class Product:
    _ids = 0

    def __init__(self, product_name, product_price, product_category):
        self.prod_id = Product._ids
        self.name = product_name
        self.price = product_price
        self.category = product_category
        Product._ids += 1

    def update_price(self, percent_change, is_increased):
        if (is_increased):
            self.price += (self.price * (percent_change/100))
        else:
            self.price -= (self.price * (percent_change/100))

        return self

    def print_info(self):
        print(self.name)
        print(self.price)
        print(self.category)
