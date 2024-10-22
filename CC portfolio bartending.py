# ings must be input as a dictionary, not writing code to check
# self.vars is a list of variation names
# self.ings is a list of dictionaries, each corresponding to the ingredients
#   of a particular variation
class Recipe:
    def __init__(self, name, ings):
        self.name = name
        self.vars = [""]
        self.ings = [ings]
        write_recipe("Recipes.txt", self)
    def __repr__(self):
        return self.name
# Here, var will be input as an int corresponding to the variation's 
# position in the list self.vars
    def recipe(self, var):
        for ing in self.ings[var]:
            print(ing + " " * (20 - len(ing)) + self.ings[ing])
    def add_var(self, name, ings, original_name = ""):
        if original_name != "":
            self.vars[0] = original_name
        self.vars.append(name)
        self.ings.append(ings)
        write_recipe("Recipes.txt", self)

def write_recipe(file, recipe):
    infile = open(file, "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.split(";")[0] == recipe.name:
            lines.remove(line)
            break

    recipe_string = f"{recipe.name};"
    for i in range(len(recipe.vars)):
        recipe_string += recipe.vars[i] + ";"
        ing_names = ",".join(recipe.ings[i].keys())
        ing_amounts = ",".join(recipe.ings[i].values())
        recipe_string += ing_names + ";"
        recipe_string += ing_amounts + ";"
    recipe_string += "\n"
    lines.append(recipe_string)
    lines.sort()

    outfile = open(file, "w")
    for line in lines:
        outfile.write(line)
    outfile.close()

# This code block pretends recipes are structured as in booze.py
# Will need to be rewritten once Recipes.txt is reformatted
# recipes = []
# infile = open("Recipes.txt", "r")
# lines = [line.split(",") for line in infile.readlines()]
# for line in lines:
#     ing_names, amounts = [], []
#     for i in range(1, len(line)):
#         if i % 2 == 1: ing_names.append(line[i])
#         elif i % 2 == 0: amounts.append(line[i])
#     ings = {}
#     for i in range(len(ing_names)):
#         ings[ing_names[i]] = amounts[i]
#     recipes.append(Recipe(line[0], ings))
# print(recipes)

##### TESTING AREA #####
##### TESTING AREA #####
##### TESTING AREA #####

bs_ings = {"Scotch":"0.75 oz", "Cherry Heering":"0.75 oz",
           "Sweet Vermouth":"0.75 oz", "Orange Juice":"0.75 oz"}
blood_and_sand = Recipe("Blood and Sand", bs_ings)
bsm_ings = {"Scotch":"1.5 oz", "Cherry Heering":"0.5 oz",
           "Sweet Vermouth":"0.5 oz", "Orange Juice":"0.75 oz"}
blood_and_sand.add_var("Meehan", bsm_ings, "Classic")