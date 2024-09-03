"""
More about the list
removing items from the list
"""
my_shopping_list = ['New string', 'butter', '10000', 5748.3, 100, 453, 'Milk', 'Sugar', 'cream', 'coffee']
my_shopping_list.remove(5748.3)
print(my_shopping_list,"\n")
print("***********")

duplicate_shopping_list = my_shopping_list.copy()
print(duplicate_shopping_list)

my_shopping_list.clear()
print(my_shopping_list)

my_shopping_list = [24,56,100,78,34.675,1000]
my_shopping_list.sort()
print(my_shopping_list)

my_shopping_list.reverse()
print(my_shopping_list)