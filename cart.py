class Cart():
    def __init__(self):
        self.cart_items = []
        
    def add_product_to_cart(self,product,price,quantity):
        #Adding products to cart
        if quantity > 0:
            self.cart_items.append(product)
        else:
            print("Quantity must be greater then 0.")
    
    def calculate_total(self):
        #Calculates total value of cart
        total = sum(product.price * quantity for product,quantity in self.cart_items)
        return total
    
    def display_cart(self):
        #Displays cart content
        
        if not self.cart_items:
            print("Cart is empty")
        else:
            print("Cart content:")
            for product,quantity in self.cart_items:
                print(f"{product.name} - {quantity}, Price for one: {product.price} EUR")
            print(f"Total value: {self.calculate_total()}EUR")    