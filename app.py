from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from models import db, User, Product
from forms import ProductForm, LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    db.app = app
    # This needs to be changed. db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    db.create_all()

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = LoginForm()

        if not form.validate_on_submit():
            return render_template('login.html', form=form)

        else:
            flash('Login requested for user {}, \
                   remember_me={}'.format(form.username.data, form.remember_me.data))
            # Code here to see if the user is in the system and if so throw an error.
            return redirect('/home')

        # if form.validate_on_submit():
        #     flash('Login requested for user {}, \
        #            remember_me={}'.format(form.username.data, form.remember_me.data))
        #     # Code here to see if the user is in the system and if so throw an error.
        #     return redirect('/home')
        # return render_template('login.html', form=form)


    @app.route('/add_product', methods=['GET', 'POST'])
    def product():
        form = ProductForm()
        if form.validate_on_submit():
            flash('Product being made with name={}, cost={}'.format(form.product_name.data, form.product_cost.data))
            p = Product(product_name=form.product_name.data, product_cost=form.product_cost.data)
            db.session.add(p)
            db.session.commit()
            return redirect('/products')
        return render_template('add_product.html', form=form)


    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/products')
    def products():
        products = Product.query.all()
        return render_template('products.html', products=products)

    return app

# Customer Data Grouping - Statistics, Machine Learning
# Data Permissions for Users - Regional Manager, Store Managers,
# Page Permissions for Users


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
