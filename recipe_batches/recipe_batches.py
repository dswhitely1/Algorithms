#!/usr/bin/python

"""
Write a function that receives a recipe in the form of a dictionary,
as well as all of the ingredients you have available to you, also in the form of a dictionary.

Understand:

Compare ingredients by name, using the // operation to return the number of batches available
Return the minimum amount

Plan

Dictionaries are like JS Objects, they have a key value pair.

set minimum based on the loop, can terminate early if a 0 is returned
else compare minimum to next key and if minimum > current value, set new minimum
"""


def recipe_batches(recipe, ingredients):
    minimum = None
    try:
        for k, v in enumerate(recipe):
            if ingredients[v] // recipe[v] == 0:
                return 0
            elif k == 0:
                minimum = ingredients[v] // recipe[v]
            else:
                if minimum > ingredients[v] // recipe[v]:
                    minimum = ingredients[v] // recipe[v]
    except KeyError:
        return 0

    return minimum


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
