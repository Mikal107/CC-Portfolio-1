## CS101 Portfolio Project: The Bartender's Virtual Assistant

Welcome to The Bartenders' Virtual Assistant! As a beginner programer and cocktail enthusiast, I wrote this command line program to help catalog and organize cocktail recipes, while also tracking the ingredients available at my home bar and the drinks I can make with them. Here's an outline of what the program can do:

1. **Recipes**: Recipes are stored in a dedicated text document and converted to Recipe objects using the get_recipes() function. The recipe name is stored as a string in self.name, and the ingredients are stored as a dictionary, whose keys are the ingredient names and whose values are the ingredient quantities. When a new recipe is added (via user input), it is written into the text file with the write_recipe() function.
2. **Variations**: Once a recipe is initalized, the user can add variations of the recipe to be stored in the same Recipe object. When a variation is added to a recipe, the name of that variation is appended to the list self.vars, and its ingredients (stored in a dictionary) are appended to the list self.ings. These two lists are created when the recipe is first initialized. For a recipe that has one basic recipe and no variations, the list self.vars will contain nothing but an empty string "", indicating that a variation name is not needed. Once a variation is added, the user will be prompted to provide names for both the new variation and the original recipe, both of which are stored in self.vars. Similarly, self.ings is a list of dictionaries, with one dictionary holding the ingredients for each variation.
3. **Tags**: Any time a recipe is initialized or has a variation added to it, a new list of tags is automatically generated based on the recipe's ingredients. These tags are stored as sublists of a list stored as self.tags, with one sublist for each variation. *See below for disclaimers*
4. **Ingredient Tracker**: The program (optionally) uses another dedicated text file to track the ingredients a user has available. Ingredients are added and removed from this list using the add_ing() and remove_ing() functions, but like everything else, can be done in the terminal with user input without needing to know the inner workings of the program. The user can also search for cocktail recipes that they can make with their ingredients, as well as those that are only missing a set number of ingredients.

Some other notes:  

**Using sample ingredients and recipes**: In case you'd like to play with the program without having to input a bunch of recipes and ingredients, I've included a sample recipe book and ingredient list. To use them, after downloading the repsitory, just delete the files "Recipes.txt" and "Ingredients.txt", then rename "Sample Recipes.txt" to "Recipes.txt" and rename "Sample Ingredients.txt" to "Ingredients.txt" (those are case sensitive!).  
**Disclaimers regarding tags**: Some tags generated by the program might not be quite right for a couple of reasons. First, everyone's taste is subjective and different people might disagree on whether a drink is sweet, sour, boozy, etc. Second, accurately tagging every possible recipe would require giving the program information (i.e. sweetness and alcohol level) about every possible cocktail ingredient, which falls outside the scope of this project (I didn't feel like it). Regardless, I still believe the tags feature is very useful in its current state, and I encourage you to play around with it and tweak the parameters in the generate_tags() function if you disagree with any of the choices I've made there.  

Thanks for checking out my work, and feel free to reach out if you have any questions, comments or concerns!