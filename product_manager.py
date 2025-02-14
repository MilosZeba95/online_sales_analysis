from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        #Adds products to list
        self.products.append(product)

    def display_all_products(self):
        #Displays info about all products
        if not self.products:
            print("Product not available")
        for product in self.products:
            product.display_info()

    def total_value(self):
        #Calculates and displays sum of all products
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of all products: {total} RSD")
    
    def remove_product(self,product_name):
        #Removes product from list 
        self.products = [product for product in self.products if product.name != product_name]
        
