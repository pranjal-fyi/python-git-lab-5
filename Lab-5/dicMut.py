"""
(a) Write a function add_entry(d) that adds a new key-value pair into a dictionary.
(b) Write another function reassign_dict(d) that reassigns the dictionary variable to a new dictionary. 
Test both functions on the same dictionary and observe the results. 
"""
def add_entry(d):
    d["city"] = "Delhi"


def reassign_dict(d):
    d = {"name": "Rahul", "age": 20}


my_dict = {"name": "Amit", "age": 25}

print("Before:", my_dict)

add_entry(my_dict)
print("After add_entry:", my_dict)

reassign_dict(my_dict)
print("After reassign_dict:", my_dict)
