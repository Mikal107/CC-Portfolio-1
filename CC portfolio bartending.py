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

##### TESTING AREA #####
##### TESTING AREA #####
##### TESTING AREA #####

bs_ings = {"Scotch":"0.75 oz", "Cherry Heering":"0.75 oz",
           "Sweet Vermouth":"0.75 oz", "Orange Juice":"0.75 oz"}
blood_and_sand = Recipe("Blood and Sand", bs_ings)
bsm_ings = {"Scotch":"1.5 oz", "Cherry Heering":"0.5 oz",
           "Sweet Vermouth":"0.5 oz", "Orange Juice":"0.75 oz"}
blood_and_sand.add_var("Meehan", bsm_ings, "Classic")
bss_ings = {"Blood":"1.5 oz", "Sand":"1.5 oz"}
blood_and_sand.add_var("Authentic", bss_ings)

recipes = get_recipes()

blood_and_sand.recipe(0)
blood_and_sand.recipe(1)
blood_and_sand.recipe(2)