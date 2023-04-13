from flaskshop.database import Column, Model, db



class ProductImportBTS(Model):
    __tablename__ = "product_import_bts"

    id = Column(db.Integer(), primary_key=True, nullable=False)  #BTSWholesaler internal ID
    ean = db.Column(db.Integer(), nullable=False)                #Product reference
    categories = db.Column(db.String(), nullable=False)          #Product category ID separated by “/”
    manufacturer = db.Column(db.String(), nullable=False)        #Product brand
    name = db.Column(db.String(), nullable=False)                #Product name
    description = db.Column(db.String(100), nullable=False)      #Product description
    recommended_price = db.Column(db.Float(), nullable=False)    #Recommended or slashed price
    price = db.Column(db.Float(), nullable=False)                #Product price
    stock = db.Column(db.Integer(), nullable=False)              #Available stock
    image = db.Column(db.String(255), nullable=False)            #URL for the product’s image
    delivery = db.Column(db.Integer(),nullable=False )           #Leadtime to ship: 24/48 or 48/72 hours
    gender = db.Column(db.String(),nullable=False)               #Product genre: male, female or unisex

class ListProduct(Model):
    __tablename__ = "product_list_import_bts"

    id = Column(db.Integer(), primary_key=True, nullable=False)  #BTSWholesaler internal ID
    ean = db.Column(db.Integer(), nullable=False)                #Product reference
    categories = db.Column(db.String(), nullable=False)          #Product category ID separated by “/”
    manufacturer = db.Column(db.String(), nullable=False)        #Product brand
    name = db.Column(db.String(), nullable=False)                #Product name
    description = db.Column(db.String(100), nullable=False)      #Product description
    recommended_price = db.Column(db.Float(), nullable=False)    #Recommended or slashed price
    price = db.Column(db.Float(), nullable=False)                #Product price
    stock = db.Column(db.Integer(), nullable=False)              #Available stock
    image = db.Column(db.String(255), nullable=False)            #URL for the product’s image
    delivery = db.Column(db.Integer(),nullable=False )           #Leadtime to ship: 24/48 or 48/72 hours
    gender = db.Column(db.String(),nullable=False)               #Product genre: male, female or unisex


class ListCategories(Model):
    __tablename__ = "categories_list_import_bts"

    id = Column(db.Integer(), primary_key=True, nullable=False) #BTSWholesaler category ID
    name = Column(db.Integer(), nullable=False)                 #Category name
    pareny_id = Column(db.String(),nullable=False)              #Parent category ID

class ShippingPrices(Model):
    __tablename__ = "shipping_prices_import_bts"

    id = Column(db.Integer(), primary_key=True, nullable=False) #Shippping cost ID to use when placing the order
    devilery_time = Column(db.Integer(), nullable=False)        #Expected delivery time
    company_name = Column(db.Integer(), nullable=False)         #Shipping company
    shipping_cost = Column(db.Float(), nullable=False)          #Shipping rate, excluding taxes
    free_shipping = Column(db.Float(), nullable=False)          #Minimum order to be entitled to free shipping 
 

class CancelOrder(Model):
    __tablename__ = "cancel_order_import_bts"


class Order(Model):
    __tablename__ = "order_import_bts"

    order_number = Column(db.String(), primary_key=True, nullable=False) #Order number
    order_status = Column(db.String(),nullable=False)                    #Order status
    tracking = Column(db.String(),nullable=False)                        #Tracking number for order
    order_total = Column(db.Float(), nullable=False)                     #Total cost
    client_name = Column(db.String(),nullable=False)                     #Customer's name
    client_email = Column(db.String(),nullable=False)                    #Customer's email
    address = Column(db.String(),nullable=False)                         #Customer's address
    postal_code = Column(db.String(),nullable=False)                     #Customer's post code
    city = Column(db.String(),nullable=False)                            #Customer's city
    state_code = Column(db.String(),nullable=False)                      #State code
    country_code = Column(db.String(),nullable=False)                    #Delivery country code
    shipping_company = Column(db.String(),nullable=False)                #Shippping company
    shipping_cost = Column(db.Float(),nullable=False)                    #Shipping cost
    telephone = Column(db.String(),nullable=False)                       #Customer's telephone
    comments = Column(db.String(),nullable=False)                        #Customer's comments
    expected_delivery_date = Column(db.String(),nullable=False)          #Earliest estimated delivery date
    expected_delivery_date_2 = Column(db.String(),nullable=False)        #Latest estimated delivery date
    expected_dispatch_date = Column(db.String(),nullable=False)          #Earliest estimated dispatch date
    expected_dispatch_date_2 = Column(db.String(),nullable=False)        #Latest estimated dispatch date
    dropshipping = Column(db.Integer(),nullable=False)                   #Drop-shipping order 0 - NO, 1 - YES 
    entry_date = Column(db.String(),nullable=False)                      #Order date




class PointRelais(Model):
    __tablename__ = "point_relais_import_bts"

    id = Column(db.Integer(), primary_key=True, nullable=False) #Delivery point ID
    name = Column(db.Integer(), nullable=False)                 #Delivery point name
    address = Column(db.Integer(), nullable=False)              #Delivery point address
    city = Column(db.Integer(), nullable=False)                 #Delivery point city
    postal_code = Column(db.Integer(), nullable=False)          #Delivery point post code


class Countries(Model):
    __tablename__ = "countries_import_bts"

    code = Column(db.String(), nullable=False)                  #Country code
    name = Column(db.String(), nullable=False)                  #Country name

class StatesByCountryCode(Model):
    __tablename__ = "states_import_bts"

    code = Column(db.String(), nullable=False)                  #State code
    name = Column(db.String(), nullable=False)                  #State name