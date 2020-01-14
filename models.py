from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    product_cost = db.Column(db.Float)   


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)
#   permissions = Column(PERMISSION_GROUP)
#   organizational_level = Column()  # User, Sally has an organizational level of 1.3.5 --> 1 is the region,
                                      # 3 is the district, and 5 is the store.
