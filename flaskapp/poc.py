from application import db
from application.models import VegRecipes, MeatRecipes
import json

print('loading the json file')
with open('./MeatRecipes.json', 'r') as json_file:
    json_file_contents = json_file.read()

meatrecipes_dictionary = json.loads(json_file_contents)

meatrecipes = []

print('creating python classes from the meat recipe dictionaries')
for meatrecipe in meatrecipes_dictionary:
    meatrecipes.append(MeatRecipes(
        name=meatrecipe['Name'],
        image=meatrecipe['Image'],
        method='\n'.join(MeatRecipes['Method']),
        ingredients='\n'.join(MeatRecipes['Ingredients']))
    )



print('loading the json file')
with open('./VegRecipes.json', 'r') as json_file:
    json_file_contents = json_file.read()

vegrecipes_dictionary = json.loads(json_file_contents)

vegrecipes = []

print('creating python classes from the veg recipe dictionaries')
for vegrecipe in vegrecipes_dictionary:
   vegrecipes.append(VegRecipes(
        name=vegrecipe['Name'],
        image=vegrecipe['Image'],
        method='\n'.join(VegRecipes['Method']),
        ingredients='\n'.join(VegRecipes['Ingredients']))
    )


print('saving the recipes to the database')
db.session.bulk_save_objects(recipes)
db.session.commit()

