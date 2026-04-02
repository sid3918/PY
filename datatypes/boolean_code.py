is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling
"""this above code is called upcasting"""
print(f"total actions : {total_actions}")

milk_present = 1 # no milk 
print(f"is there milk present? : {bool(milk_present)}")
"""where, the "bool" is a method or function in python
so if milk_present = 0,None -> false
else true for all other values """

water_hot = True
tea_added = True
can_serve = water_hot and tea_added
print(f"can serve chai ? : {can_serve}")