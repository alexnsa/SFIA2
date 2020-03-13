from application import db
from application.models import Users, Recipe, VegRecipes, MeatRecipes, Favourites

db.drop_all()
db.create_all()
import poc
