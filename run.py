# importing modules
import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

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
    
@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return render_template('recipes.html', title='All Recipes', recipes=mongo.db.recipes.find())
    #db.companies.find().skip(NUMBER_OF_ITEMS * (PAGE_NUMBER - 1)).limit(NUMBER_OF_ITEMS )
    #return render_template('recipes.html', title='All Recipes', recipes=mongo.db.recipes.find().skip(4 *  (1 - 1)).limit(6))

@app.route('/get_starter', methods=['GET'])
def get_starter():
    return render_template('recipes.html', title='Starters', recipes=mongo.db.recipes.find({'recipe_category': 'Starter'}))

@app.route('/get_main', methods=['GET'])
def get_main():
    return render_template('recipes.html', title='Main Dish', recipes=mongo.db.recipes.find({'recipe_category': 'Main'}))

@app.route('/get_snacks', methods=['GET'])
def get_snacks():
    return render_template('recipes.html', title='Snacks', recipes=mongo.db.recipes.find({'recipe_category': 'Snacks'}))

@app.route('/get_desserts', methods=['GET'])
def get_desserts():
    return render_template('recipes.html', title='Desserts', recipes=mongo.db.recipes.find({'recipe_category': 'Dessert'}))
    
@app.route('/get_drinks', methods=['GET'])
def get_drinks():
    return render_template('recipes.html', title='Desserts', recipes=mongo.db.recipes.find({'recipe_category': 'Drinks'}))    

@app.route('/view/recipe_id?=<id>')
def view(id):
    
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    return render_template('view.html', title='View Full Recipe', recipe=recipe)

    
@app.route('/add_recipe')
def add_recipe():
    
    #check for logged in user
    email = session.get('email')
    if not email:
        flash('You need to login to add your recipe!')
        return redirect(url_for('login'))
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find(),
    difficulties=mongo.db.difficulties.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
   print(request.form)
   print(request.form.getlist('recipe_ingredients[]'))
   print(request.form.getlist('recipe_procedure[]'))
   print(request.form.to_dict())
   recipes = mongo.db.recipes
   data = request.form.to_dict()
   data.update({'recipe_ingredients':request.form.getlist('recipe_ingredients[]')})
   data.update({'recipe_procedure':request.form.getlist('recipe_procedure[]')})
   del data['recipe_ingredients[]']
   del data['recipe_procedure[]']
   recipes.insert_one(data)
   flash('You have added your recipe successfully!!')
   return redirect(url_for('get_recipes'))
 
 
@app.route('/edit_recipe/recipe_id?=<id>',methods=['GET'])
def edit_recipe(id):
    #check for logged in user
    email = session.get('email')
    if not email:
        return redirect(url_for('login'))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)}) 
    categories=mongo.db.categories.find()
    difficulties=mongo.db.difficulties.find()
    return render_template('editrecipe.html', title='Edit Recipe', recipe=recipe, categories=categories, difficulties=difficulties)


@app.route('/update_recipe/recipe_id?=<id>', methods=['POST'])
def update_recipe(id):
    recipe = mongo.db.recipes
    recipe.update( {'_id': ObjectId(id)},
        {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_description':request.form.get('recipe_description'),
        'recipe_ingredients':request.form.getlist('recipe_ingredients[]'),
        'recipe_procedure':request.form.getlist('recipe_procedure[]'),
        'recipe_category':request.form.get('recipe_category'),
        'recipe_time':request.form.get('recipe_time'),
        'recipe_recipe_difficulty_level':request.form.get('recipe_recipe_difficulty_level'),
        'recipe_author':request.form.get('recipe_author'),
        'recipe_image':request.form.get('recipe_image')
    })
    
    return redirect(url_for('view', id=id))
 
@app.route('/delete_recipe/recipe_id?=<id>')
def delete_recipe(id):
    
        # check for logged in user
    email = session.get('email')
    emailid = mongo.db.users.find({'email': email})
    if not email:
        flash('You need to login to delete your own recipe!')
        return redirect(url_for('login'))
    try:
        mongo.db.recipes.delete_one({"_id": ObjectId(id), 'email': emailid})
    except:
        flash('You can only delete your own recipe!')
        return redirect(url_for('get_recipes'))
    return redirect(url_for('get_recipes'))
    

    
    
    

@app.route('/register', methods=['POST', 'GET'])
def register():
    '''Accepts POST and GET requests.
    If the request is a GET request, checks for a session email.
    If session email is found, the homepage is rendered.
    If no session email is found, the register template is rendered.
    If the request is a POST request, form data is retrieved.
    A check is performed to verify that the user email doesn't already exist.
    If the user already exists, the register page is rendered with a user_exists error.
    If a user does not exist, the user is added to the database and the login page is rendered.'''

    # check for logged in user
    email = session.get('email')
    if email:
      return redirect(url_for('home'))

    user = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = {'name': name, 'email': email, 'password': password}
        flash('Congratulation!!You are registered now!')
        if mongo.db.users.find_one({"email": email}):
            return render_template('register.html', title='Register', error="user_exists")
        else:
            mongo.db.users.insert_one(user)
            return render_template('login.html', title='Login', user=user, password=password)
          
    return render_template('register.html', title='Register')


@app.route('/login', methods=['POST', 'GET'])
def login():
    # check for logged in user
    email = session.get('email')
    if email:
        return redirect(url_for('register'))

    user = None
    if request.method == 'POST':
        email = request.form["email"]
        user = mongo.db.users.find_one({"email": email})

        try:
            assert(user["password"] == request.form["password"])
        except (AssertionError, TypeError):
            return render_template('login.html', title='Login', user=None, error="incorrect_login")
        else:
            try:
                session['name'] = user['name']
            except KeyError:
                session['name'] = 'John Doe'
            session['email'] = email
            return redirect(url_for("home"))

    return render_template('login.html', title='Login', user=user)

    
    
@app.route('/logout')
def logout():
    #  logout user and clear session
    session['email'] = None
    session['name'] = None
    # session.clear()
    return redirect(url_for('home'))



if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)