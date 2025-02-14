from product_manager import ProductManager
from product import Product
from cart import Cart
import random
if __name__ == "__main__":
    manager = ProductManager()
    
    #Adding products
    product1 = Product("Laptop",852,7)
    product2 = Product("Monitor",200,8)
    product3 = Product("Keyboard",70,3)
    product4 = Product("Mouse",120,12)

    #Displaying all products
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)
    
    
   #instance of Cart
    cart = Cart()

    #Adding random products to cart
    selected_products = random.sample(manager.products, 3)
    for product in selected_products:
        cart.add_product_to_cart(product, 1)  #Adding one of each products

    #Display of cart content and total value
    print("\nSadržaj korpe:")
    cart.display_cart()
