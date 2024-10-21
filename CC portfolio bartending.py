class Recipe:
    def __init__(self, name, ings):
        self.name = name
        if type(ings) != dict:
            raise TypeError("Please provide ings as a dictionary")
        self.ings = ings
    def __repr__(self):
        return self.name
    def recipe(self):
        for ing in self.ings:
            print(ing + " " * (20 - len(ing)) + self.ings[ing])

# This code block pretends recipes are structured as in booze.py
# Will need to be rewritten once Recipes.txt is reformatted
recipes = []
infile = open("Recipes.txt", "r")
lines = [line.split(",") for line in infile.readlines()]
for line in lines:
    ing_names, amounts = [], []
    for i in range(1, len(line)):
        if i % 2 == 1: ing_names.append(line[i])
        elif i % 2 == 0: amounts.append(line[i])
    ings = {}
    for i in range(len(ing_names)):
        ings[ing_names[i]] = amounts[i]
    recipes.append(Recipe(line[0], ings))
print(recipes)

##### TESTING AREA #####
##### TESTING AREA #####
##### TESTING AREA #####

# daiquiri = Recipe("Daiquiri", {"White Rum":"2 oz", "Lime Juice":"0.75 oz",
#                                "Simple Syrup":"0.75 oz"})
# daiquiri.recipe()