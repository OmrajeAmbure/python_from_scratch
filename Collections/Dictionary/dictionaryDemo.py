# A Python dictionary is a data structure that stores information in key-value pairs. While keys must be unique and immutable (like strings or numbers), the values can be of any data type, whether mutable or immutable. This makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list.
# Example: This example shows how a dictionary stores data using keys and values.
data = { "name": "Jake", "age": 22 }
print(data)

# Creating a Dictionary
data = { "name": "Jake", "age": 22 }
print(data)

data2 = dict({"name":"raj","age":20});
print(data2)

# Accessing Dictionary Items --> square brackets [ ] or with the get() method. Both return the value linked to the given key.
print(data["name"]); # using key index value
print(data.get("age")); # using get(value) method

# Removing Dictionary Items
# Dictionary items can be removed using built-in deletion methods that work on keys:
# del: removes an item using its key
# pop(): removes the item with the given key and returns its value
# clear(): removes all items from the dictionary
# popitem(): removes and returns the last inserted key–value pair

dist = {"name":"omraje","age":20};
# del dist;
# print(dist) throw NameError: name 'dist' is not defined. Did you mean: 'dict'?

val = dist.pop("name"); # here we must to pass key it will return specified key : vlaue;
print(val)

key , value = dist.popitem(); # this method will return the last key : value of the dictionary
print(f"key: {key} --> Value: {value}");

dist.clear()
print(dist) # clear the entire dictionary just {} show

# Iterating Through a Dictionary
# A dictionary can be traversed using a for loop to access its keys, values or both key-value pairs by using the built-in methods keys(), values() and items().
d = {1: 'Geeks', 2: 'For', 'age':22}

for key in d:
    print(key , end=" "); # just show key --> 1 2 age

for value in d.values():
    print(value,end=" ") # Just show value --> Geeks For 22

print(); # just for space
for key,value in d.items():
    print(f"[ {key} : {value} ]",end=" ");

# Nested Dictionaries --> A nested dictionary is a dictionary that contains another dictionary as one of its values. Below diagram shows how a nested dictionary works, where key 3 points to another dictionary inside the main dictionary.
# keys
#   1   : value1
#   2   : value2
#   3   :  -----------> Nested Key
#                                 A  :  value 1
#                                 B  :  value2
#                                 C  :  value3
print()
d = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
# print(d)

for i in d.values():
    print(i);
    for j in d[3].values():
        print(j);

print("---------------------------------------------------------")
for key, value in d.items():
    if isinstance(value, dict):   # check nested dictionary
        print(f"{key} :")
        for k, v in value.items():
            print(f"   {k} : {v}")
    else:
        print(f"{key} : {value}")
print("---------------------------------------------------------")