import product
import store

zapatos = product.Product("Nike Shoes", 300, "shoes")
zapatos2 = product.Product("Sandals", 50, "shoes")
shirt = product.Product("Shirt", 50, "clothing")

zapatos.update_price(10, False)
print(zapatos.prod_id)
print(zapatos2.prod_id)
print(shirt.prod_id)

my_store = store.Store("MegaShoes")
my_store.add_product(zapatos, 3)
my_store.add_product(shirt, 1)
my_store.add_product(zapatos2, 5)

my_store.update_product(1, 3)
my_store.sell_product(1, 7)

my_store.inflation(10)
my_store.set_clearance("shoes", 50)
