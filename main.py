from models import *
from peewee import *
# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line
def main():
    search("sweater")
    list_user_products(2)
    list_products_per_tag(2)
    add_product_to_catalog(1, "jumpsuit", "Long jumpsuit for the cooler summer days", 159.89, 5, "dress")
    remove_product(5)
    update_stock(1, 60)
    purchase_product(1, 2, 10)

#Search for products based on a term. Searching for 'sweater' should yield all products that have the word 'sweater' in the name. This search should be case-insensitive
def search(term):
    query = Products.select().where((fn.lower(Products.product_name.contains(fn.lower(term)))) | (fn.lower(Products.description.contains(fn.lower(term)))))
    query2 = Products.select().join(Tag).where(Tag.tag == fn.lower(term))
    if query:
        for product in query:
            print(product.product_name)
    elif query2:
        for product in query2:
            print(product.product_name)
    else:
        print("There is no product what fits the given term!")

# View the products of a given user.
def list_user_products(user_id):
    query = Products.select().where(Products.owner == user_id)
    if query:
        for i in query:
            print(f"{i.owner.username} has the following products: ")
            break
        for products in query:
            print(f"{products.product_name}")
    else:
        print("There is no user with the given id!")

# View all products for a given tag.        
def list_products_per_tag(tag_id):
    query = Products.select().join(Tag).where((Products.product_tag == tag_id) | (Tag.tag == tag_id))
    if query:
        for products in query:
            print(products.product_name)
    else:
        print("There is no product with the given tag id!")

# Add a product to a user.
def add_product_to_catalog(user_id, product, description, price_per_unit, amount_in_stock, product_tag):
    tag_list = []
    for t in Tag.select():
        tag_list.append(t.tag)
    if product_tag not in tag_list:
        query = Tag.create(tag = product_tag)
        query.save()
        for t in Tag.select():
            if t.tag == product_tag:
                p_query = Products.create(product_name = product, description = description, price_per_unit = price_per_unit, amount_in_stock = amount_in_stock, product_tag = t.id, owner = user_id)
                p_query.save()
    else:
        query = Products.create(product_name = product, description = description, price_per_unit = price_per_unit, amount_in_stock = amount_in_stock, product_tag = t.id, owner = user_id)
        query.save()   
    print(f"We have added {product} to the catalog!")

# Remove a product from a user
def remove_product(product_id):
   for product in Products.select().where(Products.id == product_id):
       print(f"We have deleted {product.product_name} product from the database!")
   query = Products.delete().where(Products.id == product_id)
   query.execute()

# Update the stock quantity of a product.
def update_stock(product_id, new_quantity):
    if Products.select().where(Products.id == product_id):
        query = Products.update(amount_in_stock = new_quantity).where(Products.id == product_id)
        query.execute()
        for product in Products.select().where(Products.id == product_id):
            if product.amount_in_stock > 0:
                print(f"You have now {product.amount_in_stock} available {product.product_name} for sale.")
            else:
                print(f"There is no more {product.product_name} available for sale!")
                remove_product(product_id) 
    else:
        print("There is no product with the given product id!")              

# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    for product in Products.select().where(Products.id == product_id):
        if quantity > product.amount_in_stock:
            print(f"We have only {product.amount_in_stock} {product.product_name} left in stock! Please choose a different quantity!")
            return
        else:
            old_quantity = product.amount_in_stock
            new_quantity = old_quantity - quantity
            query = Transaction.create(buyer = buyer_id, product = product_id, amount_bought = quantity)
            query.save()
            for i in (Transaction.select().join(User).where((User.id == buyer_id) & (Transaction.product == product_id))):
                print(f"{i.buyer.username} bought {quantity} {i.product.product_name}")
                break
            update_stock(product_id, new_quantity)

if __name__ == '__main__':
    main()