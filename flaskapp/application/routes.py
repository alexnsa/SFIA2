from flask import render_template, redirect, url_for
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm
from application.models import Users, Recipe, VegRecipes, MeatRecipes, Favourites
from flask_login import login_user, current_user, logout_user, login_required
from application import db
import random
import requests
import bcrypt
import app

@app.route('/')
@app.route('/home')
def home():
        return render_template('home.html', title='Home')


# =============== Account routes =============== #

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.email.errors)
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password = hash_pw)

        db.session.add(user)
        db.session.commit()
        login_user(user)

        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account_updated'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)



@login_required
@app.route("/account/updated", methods=['GET'])
def account_updated():
    return render_template("updatesuccess.html")

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))


@app.route("/account/favourites", methods=["GET", "POST"])
@login_required
def account_favourites():
    favourites = Favourites.query.filter_by(user_id=current_user.id).all()
    recipes = []
    for favourite in favourites:
        recipe = Recipe.query.filter_by(id=favourite.recipe_id).first()
        recipes.append(recipe)

    return render_template('recipepage.html', recipe_list=recipes, favourite_page=True)

@app.route('/account/favourite/delete/<id>')
@login_required
def delete_favourite_by_id(id):
	fav = Favourites.query.filter_by(recipe_id=id).all()
	for favourite in fav:
		recipe = Recipe.query.filter_by(id=favourite.recipe_id).first()
		if current_user.id:
			db.session.delete(favourite)
	db.session.commit()
	return redirect(url_for('account_favourites'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



# =============== Recipe routes =============== #

@login_required
@app.route("/meatrecipes")
def recipe():
    recipe_list = MeatRecipes.query.all()
    print(recipe_list)
    return render_template('meatrecipes.html', name='recipe', recipe_list=recipe_list)

@login_required
@app.route("/vegrecipes")
def recipe():
    recipe_list = VegRecipes.query.all()
    print(recipe_list)
    return render_template('vegrecipes.html', name='recipe', recipe_list=recipe_list)



@login_required
@app.route("/randomrecipe")
def randomRecipe():
    response = requests.get("http://service4:5000")
    coordinate = response.text
    return render_template("recipepage.html", coordinate=coordinate)

@login_required
@app.route("/randomrecipe/addtofavourites/<meat_recipes_id>")
def favouriteMeatRecipe(meat_recipes_id):
	fave_recipe=MeatRecipe.query.filter_by(id=meat_recipes_id).first()
	if fave_recipe:
            favourite = Favourites( meat_recipes_id=fave_recipe.id, user_id=current_user.id, image=fave_recipe.image, name=fave_recipe.name)
            db.session.add(favourite)
            db.session.commit()
	return redirect(url_for('meatrecipes'))


@login_required
@app.route("/randomrecipe/addtofavourites/<veg_recipes_id>")
def favouriteVegRecipe(veg_recipes_id):
        fave_recipe=Recipe.query.filter_by(id=veg_recipes_id).first()
        if fave_recipe:
            favourite = Favourites(veg_recipes_id=fave_recipe.id, user_id=current_user.id, image=fave_recipe.image, name=fave_recipe.name)
            db.session.add(favourite)
            db.session.commit()
        return redirect(url_for('vegrecipes'))
