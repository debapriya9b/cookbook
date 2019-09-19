 
#### **[Live Site](https://heroku details/)**
  
# CookBook
--- 
  
Python & Flask - Data Centric Development  - Milestone Project 3 for Code Institute by Debapriya Bhattacharya

---

## Project Summary

The purpose is to build a full-stack site that allows users to manage a common dataset about a particular domain.Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.

The objective for this milestone project is to "*Create a web application that allows users to store and easily access cooking recipes*", using the **CRUD** operations of **C**reate, **R**ead, **U**pdate, and **D**elete for their recipes.

CookBook is an online recipe website built on **Flask** as the backend and incorporates **MongoDB** as the Database, **Bootstrap** as well as **Materializecss** as a CSS Framework and **Vanilla JavaScript**.

CookBook is where the art of cookery made plain and easy.Users can create their own free account and add an unlimited number of recipes to share with the world! If users like some of the recipes that other's have submitted, they can share their opinions by clicking on Like or Dislike buttons.Users can edit,delete their own recipes whenever they wish.

I tried to keep the website very simple and user friendly.Hope you enjoy viewing and using this site as much as I have had building it!

---

## UX

I have decided to build a Cookbook, since I personally love food and always try out new recipes from different public sites like Cooking blogs, youtube etc. This was the perfect opportunity to finally have a single application to contain all of my favourite recipes in one source. A lot of people often ask me for specific recipes, so now I can quickly provide a single source for all of my tried and tasted recipes. It also allows others to store their own recipes securely.

### User Stories

- "I love cooking!Whenever I come across a good recipe I note it down.But it is very difficult to access those recipes all the time,you cannot carry your cooking book everywhere.Right?So it will be great if I can have it online in one place."
- "I want to view the site from any device like mobile,tablet,laptop"
- "Is it possible to view all the recipes without registering or logging in?"
- "What if I post my recipe and later want to change it or delete it?"
- "I am not that computer savy,so cannot use a very complicated website."
- "I love cooking but those measurements are always confusing for me.If I get a quick reference where I can see the standard cooking conversion table it will be great"

---

## Design

### Framework

- [Materialize](http://archives.materializecss.com/0.100.2/)
    - To give a modern and clean layout.
    
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
    - Easy to use.Easy documentation.

- [jQuery 3.4.0](https://code.jquery.com/jquery/)
    - Used to simplify some of the DOM minipulations.
    
- [Flask 1.0.2](http://flask.pocoo.org/)
    - Flask is a microframework that I've used to render the back-end Python with the front-end Materialize and Bootstrap 4.

### Color Scheme

The concept for Cookbook is to make cooking fun and easy, so to keep the overall site welcoming, I have opted for a bright and colorful color scheme. These standard [Materialize Colors](http://archives.materializecss.com/0.100.2/color.html) work quite well for my project.

### Icon

[Materialize Colors](http://archives.materializecss.com/0.100.2/icons.html) has been used for this project.

---

## Wireframes

I've used Microsoft Word to create my wireframe / mock-up.

---

## Features

### Existing Features

### Features Left to Implement


---

## Technologies Used

- [GitHub](https://github.com/) - Used as remote storage of my code online.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [jQuery](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- [Materialize](https://materializecss.com/) - Used as the design framework.
- [Bootstrap](https://getbootstrap.com/) - Used as the design framework.


### Back-End Technologies

- **Flask**
    - [Flask 1.0.2](http://flask.pocoo.org/) - Used as a microframework.
    - [Jinja 2.10](http://jinja.pocoo.org/docs/2.10/) - Used for templating with Flask.
    - [Werkzeug 0.14](https://werkzeug.palletsprojects.com/en/0.14.x/) - Used for password hashing, authentication, and authorization.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.
    - [MongoDB Atlas](https://www.mongodb.com/) - Used to store my database in the 'cloud'.
    - [PyMongo 3.8.0](https://api.mongodb.com/python/current/) - Used as the Python API for MongoDB.

---

## Testing

Testing was performed in 2 different ways.  
1. Browser Testing
2. User testing
3. Manual Testing 

#### Browser Testing

While my main choice of browser for development is google chrome, I regularly checked the performance on firefox and opera browsers. 
Making use of browser resizing and dev tools device toolbars on each browser to test responsiveness and how how the grid, fonts and media queries were performing and the consistency between each. Adjusting to find a happy medium for all three. 

After I had test deployed the site to heroku I was able to see the real life versions which I was able to test on android phone, amazon fire tablet and different orientations. Unfortunitely, I have no safari devices which I am able test on.

####  User testing

I have asked multiple friends to test the website on their devices and recieved very little feedback on errors indicating that there was not many issues to be found. I am satisfied with the outcome.

####  Manual Testing

**Creating an Account**

I've created my own personal account. In addition, I've tested with about 10 fake accounts in order to confirm authentication and validation worked as expected.

**Add | Edit | Delete | Read a Recipe**

In addition to my final recipes, I've created about 10 test recipes, mostly *Abcd*, *Efgh* in order to check the add recipe functionality,flash message functionality etc. These recipes were created using my actual account, and several test accounts.All these recipes can be viewed without logging in.

**Edit,Delete button**:If the user login,then only for their own recipes edit and delete button will be visible.Tested.

For several recipes, I've edited minor things like the recipe description, adding additional ingredients or directions, to test the functionality of updating a recipe to the database.Even deleted fake recipes to check the delete functionality.

Tested all **filtered links from navbar,dropdowns** in the form,functionality of the **floating button**.Tooltips are working fine for all buttons.

**Login-Logout link in Navigation bar**

In the navbar,when the user is logged in,its showing the user's name with a welcoming note and the logged out link.Whenever user session is no more valid,its automatically showing login link instead of logout,and the use name is not visible any more:Teated this feature also.

---

## Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - Unfortunately the W3C Validator for HTML does not understand the Jinja templating syntax, so it therefore shows a lot of errors with regards to `{{ variables }}`, `{% for %} {% endfor %}`, etc. Aside from the Jinja warnings and errors, all of the remaining code is perfectly validating. Also due to the Jinja templating, certain elements cannot be 'beautified' across multiple lines, and must remain on a single line. An example of this is the `<select>` element, which is rather long with specific Materialize classes, and Jinja templating.

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - No error found
 
**JavaScript**
- [JShint](https://jshint.com/)
    - There are 8 functions in this file.
      Function with the largest signature take 0 arguments, while the median is 0.
      Largest function has 3 statements in it, while the median is 2.
      The most complex function has a cyclomatic complexity value of 2 while the median is 1.

 - `$` (21 times - this is for jQuery)
 - `M` (1 time - this is for Materialize)

**Python**
- [PEP8 Online](http://pep8online.com/)- Validated

---

## Deployment

#### Deployment to Heroku

In order the deploy my project to Heroku I have completed the following steps:

- Created a `Procfile` with the command `echo web: python run.py > Procfile`.
- Created a requirement.txt file so Heroku know what python modules it will need to run my application with the command `pip freeze > requirements.txt`
- Created a new branch to test deployment to heroku changing  MONGO_URI  from local to mongo atlas, changed app.run() to set debug to false.
- Created a new project on heroku and in the deploy section linked my github repositiory with heroku in order to deploy straight from the source.
- Configured any enviornment variables in Heroku App Settings > Config Vars such as my Secret Key, IP PORT and MONGO_URI.
- Finalised all code, and made sure that it was production ready and ensured that my `.gitignore` was not uploading any `__pycache__`, `.env` files  or `venv` folders.
- Made a final commit / push to github.
- Deployed the application from heroku admin page using linked repository and master branch.
- The application was now fully deployed


#### Setting the project up in a local development environment

Should you wish the run a local copy of this application of your local machine, you will need to follow the instructions listed below:

**Tools you may need:**   

Python 3 installed on your machine https://www.python.org/downloads/  
PIP installed on your machine https://pip.pypa.io/en/stable/installing/  
Git installed on your machine: https://gist.github.com/derhuerst/1b15ff4652a867391f03  
A text editor such as https://code.visualstudio.com/ Visual Studio Code  
An account at  https://www.mongodb.com/cloud/atlas MongoDB Atlas or MongoDB running locally on your machine

**Instructions**

- Obtain a copy of the github repository located at https://github.com/debapriya9b/cookbook by clicking the download zip button and extracting the zip file to a chosen folder. If you have git installed on your system you can clone the repository with the command `git clone https://github.com/debapriya9b/cookbook.git`.
- If possible open a termial session in the unzip folder or `cd` to the correct location
- Next you need to install a virtual environment for the python interpreter, I recommend using pythons built in virtual environment. Enter the command `python -m venv venv` . NOTE: Your python command may differ, such as `python3` or `py`.
- Activate the venv with the command `source venv/bin/activate`, again this may differ depending on your operating system, please check https://docs.python.org/3/library/venv.html for further instructions.
- If needed, Upgrade pip locally by `pip install --upgrade pip`.
- Install all required modules withh the command `pip -r requirements.txt`.
- Its now time to open your text editor and create a file called `.flaskenv`.
- Inside this file you will need to create a SECRET_KEY variable and a MONGO_URI  to link to your own database. Please make sure to call your database 'cookbook', with 4 collections called recipes, users, categories and difficulties. You will find the source for these collections in `/app/data`.
- Lastly, open run.py and on replace line 10 to ` app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)` and save the file
- You can now run the application with the command `python run.py`
- You can visit the website at `http://127.0.0.1:5000`

---

## Credits




