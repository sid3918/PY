masala_spices = ('cardamom', 'ginger', 'cloves')
"""giving values or variables to the tuple's value present in the brackets"""
(spice1, spice2, spice3) = masala_spices 

print(f"main masala spices : {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
"""while reading the above code, 
it works same as tuple only
wether if we give round brackets to it or not, it will work the same as tuple"""

print(f"ratio for ginger is : {ginger_ratio} and for cardamom is : {cardamom_ratio} ")

"""we can also flip or swap the values"""
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"ratio for ginger is : {ginger_ratio} and for cardamom is : {cardamom_ratio} ")

# membership in python programming

print(f"is ginger in masala spices : {'ginger' in masala_spices}")
print(f"is ginger in masala spices : {'car' in masala_spices}")
