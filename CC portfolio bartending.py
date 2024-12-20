class Recipe:
    def __init__(self, name, ings):
        self.name = name
        self.vars = [""]
        self.ings = [ings]
        self.tags = [generate_tags(ings)]
        write_recipe(self)
    def __repr__(self):
        return self.name
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
        self.tags.append(generate_tags(ings))
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
        for i in range(len(recipe.vars)):
            var_missing_ings = []
            for ing in recipe.ings[i]:
                if ing not in my_ings: var_missing_ings.append(ing)
            name = recipe.name
            if recipe.vars[i] != "": name += f" ({recipe.vars[i]})"
            missing_ings[name] = var_missing_ings
    return missing_ings

def generate_tags(ings):
    volume = 0
    for val in ings.values():
        if val[-2:] == "oz":
            volume += float(val.split()[0])
    tags = []
    gins = ["Gin", "London Dry Gin", "Old Tom Gin", "Plymouth Gin"]
    tequilas = ["Blanco Tequila", "Reposado Tequila", "Anejo Tequila"]
    rums = ["White Rum", "Gold Rum", "Dark Rum"]
    vodkas = ["Vodka", "Lemon Vodka"]
    whiskies = ["Bourbon", "Rye Whiskey", "Single Malt Scotch",
                "Blended Scotch"]
    brandies = ["Brandy", "Cognac", "Pisco", "Apple Brandy"]
    base_spirits = gins + tequilas + rums + vodkas + whiskies + brandies

    for item in gins:
        if item in ings: tags.append("Gin"); break
    for item in tequilas:
        if item in ings: tags.append("Tequila"); break
    for item in rums:
        if item in ings: tags.append("Rum"); break
    for item in vodkas:
        if item in ings: tags.append("Vodka"); break
    for item in whiskies:
        if item in ings: tags.append("Whiskey"); break
    for item in brandies:
        if item in ings: tags.append("Brandy"); break
    
    sugar_values = {"Simple Syrup": 1, "Rich Simple Syrup": 2,
                   "Semi-Rich Simple": 1.5, "Bourbon": 0.2,
                   "Ginger Beer": 0.85, "Creme de Cassis": 0.75,
                   "White Rum": 0.5, "Gold Rum": 0.5,
                   "Dark Rum": 0.5, "Sweet Vermouth": 0.5,
                   "Maraschino Liqueur": 0.5, "Cherry Heering": 0.4,
                   "Amaretto": 0.8, "Orange Juice": 0.9,
                   "Cointreau": 0.3, "Apple Brandy": 0.5,
                   "Grand Marnier": 0.5}
    sugar_index = 0
    for ing in ings:
        if ing in sugar_values:
            sugar_index += sugar_values[ing] * float(ings[ing].split()[0])
    if sugar_index >= 0.5 * volume: tags.append("Sweet")
    
    boozy_ings = base_spirits + ["Cointreau"]
    booze_index = 0
    for ing in ings:
        if ing in boozy_ings:
            booze_index += float(ings[ing].split()[0])
    if booze_index >= 0.65 * volume: tags.append("Boozy")

    sour_ings = ["Lemon Juice", "Lime Juice"]
    sour_index = 0
    for ing in ings:
        if ing in sour_ings:
            sour_index += float(ings[ing].split()[0])
    if sour_index >= 0.2 * volume: tags.append("Sour")

    fizzy_ings = ["Ginger Beer", "Seltzer", "Tonic Water", "Sparkling Wine"]
    for ing in ings:
        if ing in fizzy_ings: tags.append("Fizzy"); break

    return tags

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
    print("8. Search recipes by tags")
    print("9. Quit")
    choice = str(input("\nChoose a menu option: "))
    if choice == "1":
        while True:
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
            choice = str(input("\nView another recipe? (y/n): "))
            if choice[:1].lower() != "y": break
    elif choice == "2":
        while True:
            print("\nEdit a Recipe")
            print("1. Add a new recipe")
            print("2. Add a variation to an existing recipe")
            print("3. Remove a recipe")
            print("4. Remove a variation from an existing recipe")
            choice = str(input("\nChoose a menu option: "))
            if choice == "1":
                name = str(input("Enter cocktail name: "))
                n = int(input("Enter number of ingredients: "))
                ings, amounts = [], []
                for i in range(n):
                    ings.append(str(input(f"Enter ingredient {i+1} name: ")))
                    amounts.append(str(input(f"Enter ingredient {i+1} "
                                              "amount: ")))
                ings = {ings[i]:amounts[i] for i in range(n)}
                new_recipe = Recipe(name, ings)
                print("\nRecipe saved!")
                new_recipe.recipe(0)
            elif choice == "2":
                name = str(input("Choose a cocktail to modify: "))
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
                    amounts.append(str(input(f"Enter ingredient {i+1} "
                                             f"amount: ")))
                ings = {ings[i]:amounts[i] for i in range(n)}
                if len(r.vars) == 1:
                    orig_name = str(input("Enter a new name for the "
                                          "original recipe: "))
                else: orig_name = ""
                r.add_var(var_name, ings, orig_name)
                print("\nRecipe saved!")
                r.recipe(-1)
            elif choice == "3":
                name = str(input("Choose a cocktail to remove: "))
                conf = str(input(f"Are you sure you want to remove "
                                 f"all variations of the {name} from "
                                 f"your recipe book? (y/n): "))
                if conf.lower()[0] == "y":
                    for recipe in get_recipes():
                        if recipe.name == name:
                            remove_recipe(recipe)
                            print(f"{name} recipe removed.")
            elif choice == "4":
                name = str(input("Choose a cocktail to "
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
            choice = str(input("\nEdit another recipe? (y/n): "))
            if choice[:1].lower() != "y": break
    elif choice == "3":
        print("\nYour Ingredients\n" + "=" * 32)
        for ing in get_ings():
            print(ing)
        print()
    elif choice == "4":
        while True:
            ing = str(input("Enter an ingredient name: "))
            if ing in get_ings():
                choice = str(input(f"{ing} is on your list! "
                                   f"Remove it? (y/n) "))
                if choice.lower()[0] == "y":
                    remove_ing(ing)
                    print(f"{ing} removed from list.")
            else:
                choice = str(input(f"{ing} is not on your list! "
                                   f"Add it? (y/n) "))
                if choice.lower()[0] == "y":
                    add_ing(ing)
                    print(f"{ing} added to list.")
            choice = str(input("\nEdit another ingredient? (y/n): "))
            if choice[:1].lower() != "y": break
    elif choice == "5":
        print("You can make the following cocktails:\n")
        missing = missing_ings()
        for key in missing.keys():
            if missing[key] == []: print(key)
        print()
    elif choice == "6":
        n = int(input("Enter your desired number of missing ingredients: "))
        print("Here's a list of cocktails with "
              "their missing ingredient(s):\n")
        missing = missing_ings()
        for key in missing.keys():
            if len(missing[key]) == n: 
                s = f"{key}: "
                for ing in missing[key]:
                    s += ing
                    if not ing == missing[key][-1]: s += ", "
                print(s)
        print()
    elif choice == "7":
        while True:
            desired = str(input("Enter an ingredient to find recipes: "))
            print()
            names = []
            for recipe in get_recipes():
                for i in range(len(recipe.vars)):
                    if desired in recipe.ings[i]:
                        s = recipe.name
                        if len(recipe.vars) > 1:
                            s += f" ({recipe.vars[i]})"
                        names.append(s)
            for name in names: print(name)
            if len(names) == 0: print("No recipes found!")
            choice = str(input("\nSearch for another ingredient? (y/n): "))
            if choice[:1].lower() != "y": break
    elif choice == "8":
        while True:
            choice = str(input("Enter a tag to search for, or enter "
                            "'options' for a list of possible tags: "))
            if choice == "options":
                print("Gin, Tequila, Rum, Vodka, Whiskey, Brandy, "
                    "Sweet, Sour, Boozy, Fizzy")
                choice = str(input("Enter a tag to search for: "))
            print()
            good_recipes = []
            for recipe in get_recipes():
                for i in range(len(recipe.vars)):
                    if choice in recipe.tags[i]:
                        name = recipe.name
                        if len(recipe.vars) > 1:
                            name += f" ({recipe.vars[i]})"
                        good_recipes.append(name)
            for name in good_recipes: print(name)
            if len(good_recipes) == 0: print("No recipes found!")
            choice = str(input("\nSearch for another tag? (y/n): "))
            if choice[:1].lower() != "y": break
    elif choice == "9": return
    choice = str(input("Return to main menu? (y/n): "))
    if choice[:1].lower() == "y": main(True)

if __name__ == "__main__":
    main(False)
