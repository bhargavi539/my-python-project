#List - is a collection of items and to note duplicates are allowed
#length starts from 1 and index starts from 0

my_shopping_list = ["Almonds", "butter", 5748.300, 100]
my_score_list = [87, 98, 56, 99]
print(type(my_shopping_list))
print(type(my_score_list))

print(len(my_shopping_list))
print(my_shopping_list[0])
my_shopping_list[0] = "New string"
print(f"{my_shopping_list[0] + "\n"}")

for item in my_shopping_list:
    print(item)

my_shopping_list.append(453)  # append() is used to add items to the end of the list
print(my_shopping_list, "\n")

my_shopping_list.append("Milk")
print(my_shopping_list)

my_shopping_list.extend(["Sugar", "coffee"])  # use extend() to add more items to the list at once
print(my_shopping_list,"\n")

my_shopping_list.insert(2,"10000")
print(my_shopping_list,"\n")
print("length of my shopping list ",len(my_shopping_list))

my_shopping_list.insert(-1,"cream") # if we try to add item at index -1, it adds as the second last item in the list
print(my_shopping_list,"\n")
