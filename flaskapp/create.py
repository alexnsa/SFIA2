from application import db
from application.models import Users, Favourites, MeatRecipes, VegRecipes

db.drop_all()
db.create_all()
import poc
