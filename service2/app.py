from flask import Flask
import random
import app

app = Flask(__name__)

@app.route("/")
def randomRecipe():
    meat_recipes_list = random.choice(MeatRecipes.query.all())


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')



