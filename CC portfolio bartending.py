# ings must be input as a dictionary, not writing code to check
# self.vars is a list of variation names
# self.ings is a list of dictionaries, each corresponding to the ingredients
#   of a particular variation
class Recipe:
    def __init__(self, name, ings):
        self.name = name
        self.vars = [""]
        self.ings = [ings]
        write_recipe(self)
    def __repr__(self):
        return self.name
# Here, var will be input as an int corresponding to the variation's 
# position in the list self.vars
    def recipe(self, var):
        title = self.name
        if self.vars[var] != "":
            title += f" ({self.vars[var]})"
        print("\n" + title + "\n" + ("=" * 32))
        for ing in self.ings[var]:
            print(ing + " " * (20 - len(ing)) + self.ings[var][ing])
    def add_var(self, name, ings, original_name = ""):
        if original_name != "":
            self.vars[0] = original_name
        self.vars.append(name)
        self.ings.append(ings)
        write_recipe(self)

def write_recipe(recipe):
    infile = open("Recipes.txt", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.split(":")[0] == recipe.name:
            lines.remove(line)
            break

    recipe_string = f"{recipe.name}:"
    for i in range(len(recipe.vars)):
        recipe_string += recipe.vars[i] + ";"
        ing_names = ",".join(recipe.ings[i].keys())
        ing_amounts = ",".join(recipe.ings[i].values())
        recipe_string += ing_names + ";"
        recipe_string += ing_amounts
        if i != len(recipe.vars) - 1:
            recipe_string += ":"
    recipe_string += "\n"
    lines.append(recipe_string)
    lines.sort()

    outfile = open("Recipes.txt", "w")
    for line in lines:
        outfile.write(line)
    outfile.close()

def remove_recipe(recipe):
    recipes.remove(recipe)
    infile = open("Recipes.txt", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.split(":")[0] == recipe.name:
            lines.remove(line)
    outfile = open("Recipes.txt", "w")
    for line in lines:
        outfile.write(line)
    outfile.close()

def get_recipes():
    recipes = []
    infile = open("Recipes.txt", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        line = line.strip("\n")
        name = line.split(":")[0]
        orig = line.split(":")[1]
        vars = line.split(":")[2:]

        orig_name = orig.split(";")[0]
        ing_names = orig.split(";")[1].split(",")
        amounts = orig.split(";")[2].split(",")
        ings = {k:v for (k,v) in zip(ing_names, amounts)}
        recipe = Recipe(name, ings)

        for var in vars:
            var_name = var.split(";")[0]
            ing_names = var.split(";")[1].split(",")
            amounts = var.split(";")[2].split(",")
            var_ings = {k:v for (k,v) in zip(ing_names, amounts)}
            recipe.add_var(var_name, var_ings, orig_name)
        
        recipes.append(recipe)
    return recipes

def add_ing(ing):
    infile = open("Ingredients.txt", "r")
    lines = infile.readlines()
    lines = [line.strip("\n") for line in lines]
    infile.close()
    if ing in lines:
        print("Ingredient already on list!")
    else:
        lines.append(ing)
        lines.sort()
        outfile = open("Ingredients.txt", "w")
        for line in lines:
            outfile.write(line + "\n")
        outfile.close()

def remove_ing(ing):
    infile = open("Ingredients.txt", "r")
    lines = infile.readlines()
    lines = [line.strip("\n") for line in lines]
    infile.close()
    if ing not in lines:
        print("Ingredient not on list!")
    else:
        lines.remove(ing)
        outfile = open("Ingredients.txt", "w")
        for line in lines:
            outfile.write(line + "\n")
        outfile.close()

def get_ings():
    infile = open("Ingredients.txt", "r")
    lines = infile.readlines()
    lines = [line.strip("\n") for line in lines]
    infile.close()
    return lines

def missing_ings():
    my_ings = get_ings()
    missing_ings = {}
    for recipe in recipes:
        for i in range(len(recipe.vars)): #for each variation of this recipe:
            var_missing_ings = []
            for ing in recipe.ings[i]: #for each ing in this variation:
                if ing not in my_ings: var_missing_ings.append(ing)
            name = recipe.name
            if recipe.vars[i] != "": name += f" ({recipe.vars[i]})"
            missing_ings[name] = var_missing_ings
    return missing_ings

##### TESTING AREA #####
##### TESTING AREA #####
##### TESTING AREA #####

recipes = get_recipes()
