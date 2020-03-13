from flask import Flask
import app
import random

app = Flask(__name__)

@app.route("/")
def randomRecipe():
    veg_recipes_list = random.choice(VegRecipes.query.all())


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
