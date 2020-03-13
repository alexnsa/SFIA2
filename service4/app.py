from flask import Flask
import app
import random
import requests

app = Flask(__name__)

@app.route("/randomrecipe")
def randomRecipe():
    response = requests.get("http://service2:5000")
    meat_recipes_list = random.choice(MeatRecipes.query.all())
    response = requests.get("http://service3:5000")
    veg_recipes_list = random.choice(VegRecipes.query.all())
    return(meat_recipes_list + veg_recipes_list)

if __name__== '__main__':
	app.run(debug=True, host='0.0.0.0')
