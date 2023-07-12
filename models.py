from peewee import *

# Defining database
db = SqliteDatabase("betsy_database.db")

# Basemodel
class BaseModel(Model):
    class Meta:
        database = db

# Models
class User(BaseModel):
    username = CharField()
    name = CharField()
    street = CharField()
    house_number = IntegerField()
    postal_code = CharField()
    city = CharField()
    country = CharField()
    bank_account_number = CharField()

class Tag(BaseModel):
    tag = CharField(unique=True)

class Products(BaseModel):
    product_name = CharField()
    description = TextField()
    price_per_unit = DecimalField(decimal_places=2, auto_round=True)
    amount_in_stock = IntegerField()
    product_tag = ForeignKeyField(Tag, backref="product_tag")
    owner = ForeignKeyField(User, backref="product")

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref="buyer")
    product = ForeignKeyField(Products, backref="product")
    amount_bought = IntegerField()