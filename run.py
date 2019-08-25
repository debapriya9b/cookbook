# importing modules
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm

# declaring app name
app = Flask(__name__)

# Secret key got from secrets.token_hex()
app.config['SECRET_KEY'] = '1645866b6820e28f1915bc58ebb62d53'

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://debapriya9b:Chotolok10@myfirstcluster-bsyfh.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', recipes=mongo.db.recipes.find().sort('recipe_views', pymongo.DESCENDING).limit(4))
    
    
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',  recipes=mongo.db.recipes.find().sort('recipe_views', pymongo.DESCENDING).limit(4))

#Registration
@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

#Login
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)