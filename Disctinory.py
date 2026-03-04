# A Python dictionary is a data structure that stores data in key-value pairs, where each key is unique and is used to retrieve its associated value. It is mainly used when you want to store and access data by a name (key) instead of by position like in a list.


list1  = [1,2,3,4,"rohit",7.8,True,[23,45,67],(12,34,56),{12,34,56},{"name":"rohit","age":24}]
print("Original List:", list1)
print("Length of List:", len(list1))

# Dictionary in python
dict1 = {"name":"rohit","age":24}
print("Dictionary:", dict1)
print("Length of Dictionary:", len(dict1))
# dictionary also created using dict() function. it is constructor of dictionary class
dict2 = dict(name="rohit", age=24);
print("Dictionary using dict() function:", dict2)

# Accessing elements of dictionary
print(dict2["name"])
print(dict2.get("age"))
# Adding and updating elements to dictionary
dict2["city"] = "New York"  # Adding new key-value pair
dict2["age"] = 25           # Updating existing key-value pair
print("Updated Dictionary:", dict2)
# Removing elements from dictionary
    # del: removes an item using its key
    # pop(): removes the item with the given key and returns its value
    # clear(): removes all items from the dictionary
    # popitem(): removes and returns the last inserted key–value pair
# del dict2["city"]
# pop_value = dict2.pop("age")
popitem_key, popitem_value = dict2.popitem()
# print("Popped value for 'age':", pop_value)
print("Popped item using popitem() Value :", popitem_value, "for key:", popitem_key)
print ("After deleting 'city':", dict2)