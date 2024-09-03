# Sets-> A collection of unique elements
# represented by {}

list_of_unique_items = {10, 25, 15, 25, 10, 55, 34}
print(list_of_unique_items) # -> returns only unique values

set1 ={10,20,30,40}
set2 = {15,20,30,55}
union_set = set2.union(set1)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set2.difference(set1)
print(difference_set)

subset_set = set2.issubset(set1)
print(subset_set)

set_a = {10,25,35,45,55,65}
set_b = {35,55,65}
subset_set1 = set_b.issubset(set_a)
print(subset_set1)