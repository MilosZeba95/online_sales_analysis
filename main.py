from product_manager import ProductManager
from product import Product
if __name__ == "__main__":
    manager = ProductManager()
    
    #Adding products
    product1 = Product("Laptop",852,12)
    product2 = Product("Monitor",200,5)
    product3 = Product("Keyboard",70,10)
    product4 = Product("Mouse",120,9)

    #Displaying all products
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    manager.add_product(product4)
    
    
    #Displaying all products
    print("\nList of all products")
    manager.display_all_products()
    
    #Display total value of inventory
    print("\nTotal value of inventory")
    manager.total_value()
