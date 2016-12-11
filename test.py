restrictions = ["vegan","gluten free","dairy free","egg free"]

flavors = ["strawberry","chocolate"]

recipe = Recipe()

recipe.setFlavors(flavors)
recipe.setRestrictions(restrictions)
recipe.setType(type)

recipe.checkInput()

recipe.buildRecipe()

recipe.printIngredients()
recipe.printSteps()