set1 = {"apple","banana","cherry","pineapple", "mango", "papaya"};
set1.remove("banana")
print(set1)
set1.discard("mango")
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)

#  returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

#  return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

# keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

# will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

# also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

"""
Python frozenset
    --> frozenset is an immutable version of a set.
    --> Like sets, it contains unique, unordered, unchangeable elements.
    --> Unlike sets, elements cannot be added or removed from a frozenset.
"""
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

"""
Frozenset Methods
Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

Method	            Shortcut	                     Description
copy()	 	                                            Returns a shallow copy	
difference()	              -	                        Returns a new frozenset with the difference	
intersection()	         &	                        Returns a new frozenset with the intersection	
isdisjoint()	 	                                    Returns whether two frozensets have an intersection	
issubset()	                <= / <	                Returns True if this frozenset is a (proper) subset of another	
issuperset()	            >= / >	                Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	                Returns a new frozenset with the symmetric differences	
union()                     	  |	                        Returns a new frozenset containing the union	

Set Methods -->
Python has a set of built-in methods that you can use on sets.

Method	                                            Shortcut	                                Description
add()	 	                                                                                Adds an element to the set
clear()	 	                                                                                Removes all the elements from the set
copy()	 	                                                                                Returns a copy of the set
difference()	                                            -	                            Returns a set containing the difference between two or more sets
difference_update()	                           -=	                            Removes the items in this set that are also included in another, specified set
discard()	 	                                                                            Remove the specified item
intersection()	                                        &	                            Returns a set, that is the intersection of two other sets
intersection_update()	                            &=	                        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                                                                        Returns whether two sets have a intersection or not
issubset()	                                                <=	                            Returns True if all items of this set is present in another set
 	                                                            <	                            Returns True if all items of this set is present in another, larger set
issuperset()	                                            >=	                            Returns True if all items of another set is present in this set
 	                                                            >	                            Returns True if all items of another, smaller set is present in this set
pop()	 	                                                                                Removes an element from the set
remove()	 	                                                                            Removes the specified element
symmetric_difference()	                        ^	                            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	            ^=	                            Inserts the symmetric differences from this set and another
union()	                                                    |	                            Return a set containing the union of sets
update()	                                                |=                          	Update the set with the union of this set and others

"""
