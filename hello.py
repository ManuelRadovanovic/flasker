from enum import unique
from flask import Flask, render_template, flash, request
from flask.wrappers import Request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask Instance
app = Flask(__name__)

# Add Database

# SQLite DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# MySQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:M&Rzastozato1000r@localhost/users'

# Initialize Database
db = SQLAlchemy(app)

# Create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True )
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name


# Secret Key!
app.config['SECRET_KEY'] = "my super secret key that no is suppost know"

# Create a Form Class
class UserForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Sumbit")

# Update Database Record
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        try:
            db.session.commit()
            flash("User Updated Successfully!")
            return render_template("update.html", form=form,
                                                name_to_update=name_to_update)
        except:
            db.session.commit()
            flash("Error! Looks like there was a problem. Try again!")
            return render_template("update.html", form=form,
                                                name_to_update=name_to_update)

    else:
        return render_template("update.html", form=form,
                                                name_to_update=name_to_update)



# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sumbit")

    # BooleanField
    # DateField
    # DateTimeFiel
    # DecimalField
    # FileField
    # HiddenField
    # FieldList
    # FloatField
    # FormField
    # IntegerField
    # PasswordField
    # RadioField
    # SelectField
    # SelectMultipleField
    # SubmitField
    # StringField
    # TextField

    ## Validators
    # DataRequired
    # Email
    # EqualTo
    # InputRequied
    # IPAddress
    # Length
    # MacAddress
    # NumberRange
    # Optional
    # Regexp
    # URL
    # UUID
    # AnyOf
    # NoneOf 


# Create a route decorator
# @app.route('/')
# def index():
#    return "<h1>Hello World!</h1>"

# Jinja2 

# safe
# capitalize
# lower
# uper
# title
# trim
# striptags

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
     # Validate Form
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        flash("User Added Successfully!")
    
    our_users = Users.query.order_by(Users.date_added)

    return render_template("add_user.html", form=form,
                                            name=name,
                                            our_users=our_users)

# Create a route decorator
@app.route('/')
def index():
    first_name= "Manuel"
    stuff = "This is <strong>Bold</strong> text."
    flash("Welcome To Our Website!")
    favorite_pizza = ["Pepperoni", "Cheese", "Mishrooms", 41]
    
    return render_template("index.html", 
                                first_name=first_name,
                                stuff=stuff,
                                favorite_pizza=favorite_pizza)


# localhost:5000/user/Manuel
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Pages

# Invalid URL
# @app.errorhandler(404)
# def page_not_found(e):
    #return render_template("404.html"), 404

# Interval Server Error 
# @app.errorhandler(500)
# def page_not_found(e):
    # return render_template("404.html"), 500

# Create Name Page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Sumitted Successfully!")

    return render_template("name.html", name=name,
                                        form=form)



    




