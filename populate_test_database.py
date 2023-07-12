from models import *
import os

def main():
    populate_test_database()
    #delete_test_database()

# Populate database
def populate_test_database():

    user_data = [
        { "username":"SilverSphix", "name": "Ethan Thompson", "street": "Willow Street", "house_number": 22, "postal_code": "1142BC", "city": "London", "country": "United Kingdom", "bank_account_number": "GB29NWBK61562331926817" },
        { "username":"ElectricJaguar", "name":"Benjamin Walker", "street": "Maple Avenue", "house_number": 145, "postal_code": "3600TF", "city": "London", "country": "United Kingdom","bank_account_number": "GB29NWBK60112331925819"},
        { "username":"MidnightRider", "name":"Noah Adams", "street": "Oakwood Lane", "house_number": 10, "postal_code": "4587AA", "city": "London", "country": "United Kingdom","bank_account_number": "GB29NWBK50161341926888"},
        { "username":"ScraletFox", "name":"Sophia Walker", "street": "Elm Street", "house_number": 1, "postal_code": "4569CV", "city": "London", "country": "United Kingdom","bank_account_number": "GB29NWBK60161331926816"},
        { "username":"CosmicWhisper", "name":"Mia Foster", "street": "Cedar Street", "house_number": 29, "postal_code": "4500TB", "city": "London", "country": "United Kingdom","bank_account_number": "GB29NWBK60161441926514"},
    ]

    products = [
        {"product_name": "T-Shirt", "description": "Simple white T-Shirts, one size", "price_per_unit": 19.99, "amount_in_stock": 50, "product_tag": "1", "owner": "1"},
        {"product_name": "Jeans", "description": "Blue jeans", "price_per_unit": 49.99, "amount_in_stock": 25, "product_tag": "1", "owner": "1"},
        {"product_name": "Watch", "description": "Woman watch in gold color", "price_per_unit": 149.99, "amount_in_stock": 20, "product_tag": "2", "owner": "1"},
        {"product_name": "Maxi Dress", "description": "Floral maxi dress in more colors, the skirt part is beutiful", "price_per_unit": 39.99, "amount_in_stock": 40, "product_tag": "1", "owner": "2"},
        {"product_name": "Sweater", "description": "Made from cotton", "price_per_unit": 59.99, "amount_in_stock": 30, "product_tag": "1", "owner": "2"},
        {"product_name": "Legging", "description": "In different colors", "price_per_unit": 29.99, "amount_in_stock": 60, "product_tag": "1", "owner": "2"},
        {"product_name": "Shorts", "description": "Farmer shorts", "price_per_unit": 29.99, "amount_in_stock": 50, "product_tag": "1", "owner": "3"},
        {"product_name": "Blouse", "description": "White and blue colors", "price_per_unit": 34.99, "amount_in_stock": 10, "product_tag": "1", "owner": "3"},
        {"product_name": "Sneaker", "description": "Woman sneakers in white and balck color", "price_per_unit": 39.99, "amount_in_stock": 20, "product_tag": "3", "owner": "3"},
        {"product_name": "Jacket", "description": "Winter jacket filled with wool", "price_per_unit": 19.99, "amount_in_stock": 50, "product_tag": "1","owner": "4"},
        {"product_name": "Jeans", "description": "Black jeans", "price_per_unit": 59.99, "amount_in_stock": 15, "product_tag": "1", "owner": "4"},
        {"product_name": "Skirt", "description": "Skirt in more colors", "price_per_unit": 25.99, "amount_in_stock": 80, "product_tag": "1", "owner": "4"},
        {"product_name": "Bracelet", "description": "Handmade woman bracelet", "price_per_unit": 9.99, "amount_in_stock": 25, "product_tag": "2", "owner": "5"},
        {"product_name": "Bag", "description": "Black shoulder bag", "price_per_unit": 55.99, "amount_in_stock": 30, "product_tag": "2","owner": "5"},
        {"product_name": "Swimsuit", "description": "One piece swim suit in more in the color blue, balck and white", "price_per_unit": 49.99, "amount_in_stock": 35, "product_tag": "1", "owner": "5"}
        ]

    transactions = [{"buyer": 1, "product": 10, "amount_bought": 2},
                    {"buyer": 2, "product": 15, "amount_bought": 1},
                    {"buyer": 3, "product": 2, "amount_bought": 1},
                    {"buyer": 4, "product": 1, "amount_bought": 10},
                    {"buyer": 5, "product": 8, "amount_bought": 3}]
    
    tags = [{"tag": "chlotes"},
            {"tag": "accessories"},
            {"tag": "shoes"}]
    
    with db:
        db.create_tables([User, Products, Transaction, Tag])
        
    with db.atomic():
        User.insert_many(user_data).execute()
        Products.insert_many(products).execute()
        Transaction.insert_many(transactions).execute()
        Tag.insert_many(tags).execute()
       
# Remove existing test database
def delete_test_database():
    pass
    cwd = os.getcwd()
    path = os.path.join(cwd, "betsy_database.db")
    if os.path.exists(path):
        os.remove(path)


if __name__ == "__main__":
    main()     