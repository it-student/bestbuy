"""
This is the main file within this repository.
In here everything else needed will be imported and consumed.
"""
from store import Store
from products import Product

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)

def start(store: Store) -> None:
    """
    Show (print) the User the store menu
    :param store: Store Object conataining available products
    :return None:
    """
    print("""
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")
