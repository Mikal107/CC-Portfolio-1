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
    def view_all_vars(self):
        if len(self.vars) == 1: self.recipe(0)
        else:
            for i in range(1, len(self.vars), 2):
                title_1 = self.name
                if self.vars[i-1] != "":
                    title_1 += f" ({self.vars[i-1]})"
                title_2 = self.name
                if self.vars[i] != "":
                    title_2 += f" ({self.vars[i]})"
                print("\n" + title_1 + " " * (37 - len(title_1)) + title_2)
                print("=" * 32 + " " * 5 + "=" * 32)
                ing_strings = []
                for ing in self.ings[i - 1]:
                    name = ing
                    amount = self.ings[i - 1][ing]
                    s = name + " " * (20 - len(name)) + amount
                    ing_strings.append(s)
                while len(ing_strings) < len(self.ings[i]):
                    ing_strings.append("")
                j = 0
                for ing in self.ings[i]:
                    name = ing
                    amount = self.ings[i][ing]
                    s = " " * (37 - len(ing_strings[j]))
                    s += name + " " * (20 - len(name)) + amount
                    ing_strings[j] += s
                    j += 1
                for s in ing_strings: print(s)
            if len(self.vars) % 2 == 1:
                self.recipe(len(self.vars) - 1)
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
    for recipe in get_recipes():
        for i in range(len(recipe.vars)): #for each variation of this recipe:
            var_missing_ings = []
            for ing in recipe.ings[i]: #for each ing in this variation:
                if ing not in my_ings: var_missing_ings.append(ing)
            name = recipe.name
            if recipe.vars[i] != "": name += f" ({recipe.vars[i]})"
            missing_ings[name] = var_missing_ings
    return missing_ings

def main(skip_intro = False):
    if not skip_intro:
        print("\nWelcome to the Bartender's Virtual Assistant!")
        print("\nThis program is designed to help you track your cocktail ")
        print("recipes, discover new ones, and track your collection of ")
        print("cocktail ingredients. It can also show you what drinks you ")
        print("can make using the ingredients you have, and even all the ")
        print("drinks you could make if you had just one more ingredient!")
    print("\nMain Menu")
    print("1. View a recipe")
    print("2. Edit your recipes")
    print("3. View your ingredients")
    print("4. Edit your ingredients")
    print("5. View recipes you can make with your ingredients")
    print("6. View recipes missing only a few ingredients")
    print("7. View recipes containing a desired ingredient")
    print("8. Quit (Or enter 'quit' at any time)")
    choice = str(input("\nChoose a menu option: "))
    if choice == "1":
        choice = str(input("Enter a recipe name, or type "
                           "'all' to view all recipes: "))
        if choice == "all":
            for recipe in get_recipes():
                recipe.view_all_vars()
        else:
            recipe_found = False
            for recipe in get_recipes():
                if choice == recipe.name:
                    recipe.view_all_vars()
                    recipe_found = True
            if not recipe_found:
                print("Recipe not found!")
    elif choice == "2":
        print("\nEdit a Recipe")
        print("1. Add a new recipe")
        print("2. Add a variation to an existing recipe")
        print("3. Remove a recipe")
        print("4. Remove a variation from an existing recipe")
        choice = str(input("\nChoose a menu option: "))
        if choice == "1":
            name = str(input("\nEnter cocktail name: "))
            n = int(input("Enter number of ingredients: "))
            ings, amounts = [], []
            for i in range(n):
                ings.append(str(input(f"Enter ingredient {i+1} name: ")))
                amounts.append(str(input(f"Enter ingredient {i+1} amount: ")))
            ings = {ings[i]:amounts[i] for i in range(n)}
            new_recipe = Recipe(name, ings)
            print("\nRecipe saved!")
            new_recipe.recipe(0)
        elif choice == "2":
            name = str(input("\nChoose a cocktail to modify: "))
            r = ""
            for recipe in get_recipes():
                if recipe.name == name:
                    r = recipe
            if r == "":
                print("Recipe not found!"); return
            var_name = str(input("Enter a name for this variation: "))
            n = int(input("Enter number of ingredients: "))
            ings, amounts = [], []
            for i in range(n):
                ings.append(str(input(f"Enter ingredient {i+1} name: ")))
                amounts.append(str(input(f"Enter ingredient {i+1} amount: ")))
            ings = {ings[i]:amounts[i] for i in range(n)}
            if len(r.vars) == 1:
                orig_name = str(input("Enter a new name for the "
                                      "original recipe: "))
            else: orig_name = ""
            r.add_var(var_name, ings, orig_name)
            print("\nRecipe saved!")
            r.recipe(-1)
        elif choice == "3":
            name = str(input("\nChoose a cocktail to remove: "))
            conf = str(input(f"Are you sure you want to remove all variations"
                             f" of the {name} from your recipe book? (y/n) "))
            if conf.lower()[0] == "y":
                for recipe in get_recipes():
                    if recipe.name == name:
                        remove_recipe(recipe)
                        print(f"{name} recipe removed.")
        elif choice == "4":
            name = str(input("\nChoose a cocktail to "
                             "remove a variation: "))
            bad_var = str(input("Enter a variation name to remove: "))
            for recipe in get_recipes():
                if recipe.name == name:
                    for var in recipe.vars:
                        if var == bad_var:
                            bad_index = recipe.vars.index(var)
                            recipe.vars.pop(bad_index)
                            recipe.ings.pop(bad_index)
                            write_recipe(recipe)
                            print(f"{bad_var.title()} variation removed.")
                        if len(recipe.vars) == 1:
                            recipe.vars[0] = ""
                            write_recipe(recipe)
    elif choice == "3":
        print("\nYour Ingredients\n" + "=" * 32)
        for ing in get_ings():
            print(ing)
    elif choice == "4":
        ing = str(input("Enter an ingredient name: "))
        if ing in get_ings():
            choice = str(input(f"{ing} is on your list! Remove it? (y/n) "))
            if choice.lower()[0] == "y":
                remove_ing(ing)
        else:
            choice = str(input(f"{ing} is not on your list! Add it? (y/n) "))
            if choice.lower()[0] == "y":
                add_ing(ing)
    elif choice == "5":
        missing = missing_ings()
        for key in missing.keys():
            if missing[key] == []: print(key)
    elif choice == "6":
        n = int(input("Enter your desired number of missing ingredients: "))
        missing = missing_ings()
        for key in missing.keys():
            if len(missing[key]) == n: 
                s = f"{key}: "
                for ing in missing[key]:
                    s += ing
                    if not ing == missing[key][-1]: s += ", "
                print(s)
    elif choice == "7":
        desired = str(input("Enter an ingredient to find recipes: "))
        names = []
        for recipe in get_recipes():
            for i in range(len(recipe.vars)):
                if desired in recipe.ings[i]:
                    s = recipe.name
                    if len(recipe.vars) > 1:
                        s += f" ({recipe.vars[i]})"
                    names.append(s)
        for name in names: print(name)

##### TESTING AREA #####
##### TESTING AREA #####
##### TESTING AREA #####

if __name__ == "__main__":
    main(False)
