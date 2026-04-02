ingredients_for_chai = ['water', 'milk', 'black tea']

"""but as list is mutable, we can add values even though the list is closed """
ingredients_for_chai.append('sugar')    # for adding values in the list
print(f"ingredients for chai : {ingredients_for_chai}")


ingredients_for_chai.remove('water')    # for remove values from the list
print(f"ingredients for chai : {ingredients_for_chai}")


print(f"ingredients for chai : {ingredients_for_chai.count('milk')}")     # for counting how many times that values repeated in the list


print(f"ingredients for chai : {len(ingredients_for_chai)}")     # for counts how many values are present in the list


spice_option = ['gingner', 'cardamom']
chai_ingredients = ['water', 'milk']
chai_ingredients.extend(spice_option)# for extending 1 list using another list
print(f"chai ingredients : {chai_ingredients}")


chai_ingredients.insert(2, 'sugar')     # it is used to add values on specific index
print(f"chai ingredients : {chai_ingredients}")


last_ingredient = chai_ingredients.pop()    # it pops out or display the last value present in the list 
print(f"last ingredient : {last_ingredient}")
# now the last value is removed 
print(f"chai ingredients : {chai_ingredients}")


#reverse the list 
chai_ingredients.reverse()
print(f"chai ingredients : {chai_ingredients}")


#sorts the list 
chai_ingredients.sort()
print(f"chai ingredients : {chai_ingredients}")
"""right now it actually done the sorting by 1st letters of the values"""


chai_levels = {1,2,3,4,5}
print(f"maximum chai level : {max(chai_levels)}")
# it will give max value '5' present in the list
print(f"minimum chai level : {min(chai_levels)}")
# minimum