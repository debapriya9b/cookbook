 
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
1. Manual Browser Testing during develoment  
2. User testing

#### Browser Testing

While my main choice of browser for development is google chrome, I regularly checked the performance on firefox and opera browsers. 
Making use of browser resizing and dev tools device toolbars on each browser to test responsiveness and how how the grid, fonts and media queries were performing and the consistency between each. Adjusting to find a happy medium for all three. 

After I had test deployed the site to heroku I was able to see the real life versions which I was able to test on android phone, amazon fire tablet and different orientations. Unfortunitely, I have no safari devices which I am able test on.

####  User testing

I have asked multiple friends to test the website on their devices and recieved very little feedback on errors indicating that there was not many issues to be found. I am satisfied with the outcome.

####  Manual Teating

**Creating an Account**

I've created my own personal account. In addition, I've tested with about 10 fake accounts in order to confirm authentication and validation worked as expected.

**Add | Edit | Delete a Recipe**

In addition to my personal recipes, I've created about 10 test recipes, mostly *Abcd*, *Efgh* in order to check the add recipe functionality,flash message functionality etc. These recipes were created using my actual account, and several test accounts.

For several recipes, I've edited minor things like the recipe description, adding additional ingredients or directions, to test the functionality of updating a recipe to the database.Even deleted fake recipes to check the delete functionality.

---

## Validators

---

## Deployment

---

## Credits




