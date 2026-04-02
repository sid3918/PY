# integer
tea_in_grams = 23
ginger_grams = 10
total_grams = tea_in_grams + ginger_grams
print(f"total grams : {total_grams}")
remaining_tea = tea_in_grams - ginger_grams
print(f"remaining grams : {remaining_tea}")

"""division"""
milk_in_liters = 24
servings = 12
milk_per_servings = milk_in_liters / servings
print(f"milk per servings : {milk_per_servings}")

"""division but approx"""
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
"""here, the // means it will work same as division but it will give approx value"""
print(f"bags per pot : {bags_per_pot}")

"""division but getting remainder"""
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"leftover pods : {leftover_pods}")

"""scaling or raise to or power"""
base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
"""note : it scales the value like 2 raise 2 = 4"""
print(f"powerful flavor : {powerful_flavor}")


