#!/usr/bin/env python

from functools import reduce

# =============================================================================
# Create a dictionary containing “name”, “city”, and “cake” for 
#“John” from “Westminster” who likes “Chocolate”.
# Display the dictionary.
# =============================================================================
d = dict(name="John", city="Westminster", cake="Chocolate")
print(d)

# =============================================================================
# # Delete the entry for “cake”.
# # Display the dictionary.
# =============================================================================
del d["cake"]

# =============================================================================
# # Add an entry for “fruit” with “Mango” and display the dictionary.
# =============================================================================
d["fruit"] = "Mango"
print(d)

# =============================================================================
# # Display the dictionary keys.
# =============================================================================
print(d.keys())

# =============================================================================
# Display the dictionary values.
# =============================================================================
print(d.values())

# =============================================================================
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
# =============================================================================
print("cake" in d.keys())
print("Mango" in d.values())

# =============================================================================
# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of ‘t’s in each value.
# =============================================================================
d2 = dict(map(lambda x: (x[0], x[1].count("t")), d.items()))
print(d2)