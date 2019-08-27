# importing modules
import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm

# declaring app name
app = Flask(__name__)

app.config["SECRET_KEY"] = '7473f88e01ba1bf3f40ce59c38d644ff'

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://debapriya9b:Chotolok10@myfirstcluster-bsyfh.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', recipes=mongo.db.recipes.find().sort('recipe_views', pymongo.DESCENDING).limit(4))
    
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',  recipes=mongo.db.recipes.find())

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)





if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)