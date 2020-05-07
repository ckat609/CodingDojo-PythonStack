class Store:
    def __init__(self, store_name):
        self.name = store_name
        self.products = {}

    def add_product(self, new_product, quantity):
        self.products[new_product.prod_id] = {'name': new_product.name, 'category': new_product.category, 'price': new_product.price, 'quantity': 1}
        self.show_store_info("----------NEW PRODUCT ADDED---------")
        return self

    def update_product(self, prod_id, quantity):
        if (self.products[prod_id]['quantity'] + quantity >= 0):
            self.products[prod_id]['quantity'] += quantity
        else:
            print("There's not enough in stock!")
        self.show_store_info("----------PRODUCT UPDATED---------")

        return self

    def sell_product(self, prod_id, quantity):
        self.update_product(prod_id, -quantity)
        return self

    def inflation(self, percentage_increase):
        for prod in self.products.values():
            prod['price'] += (prod['price']*(percentage_increase/100))
        self.show_store_info("----------PRODUCT UPDATED---------")
        return self

    def set_clearance(self, category, percent_discount):
        for prod in self.products.values():
            if(prod['category'] == category):
                prod['price'] -= (prod['price']*(percent_discount/100))
        self.show_store_info("----------PRODUCT UPDATED---------")

    def show_store_info(self, msg):
        print(msg)
        for key, prod in self.products.items():
            print(f"ID: {key} - Product: {prod['name']} - Category: {prod['category']} - Price: ${prod['price']} - {prod['quantity']}")
        return self


if __name__ == "__main__":
    pass
