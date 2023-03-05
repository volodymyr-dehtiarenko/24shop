from flaskshop.database import db



class ProductImportBTS(db.Model):
    __tablename__ = "product_importBTS"

    # BTSWholesaler internal ID
    id = db.Column(db.Integer(), nullable=False)
    # Product reference
    ean = db.Column(db.Integer())
    # Product category ID separated by “/”
    categories = db.Column(db.String())
    # Product brand
    manufacturer = db.Column(db.String())
    # Product name
    name = db.Column(db.String())
    # Product description
    description = db.Column(db.String(100))
    # Recommended or slashed price
    recommended_price = db.Column(db.Float())
    # Product price
    price = db.Column(db.Float())
    # Available stock
    stock = db.Column(db.Integer())
    # URL for the product’s image
    image = db.Column(db.String(255))
    # Leadtime to ship: 24/48 or 48/72 hours
    delivery = db.Column(db.Integer())
    # Product genre: male, female or unisex
    gender = db.Column(db.String())

