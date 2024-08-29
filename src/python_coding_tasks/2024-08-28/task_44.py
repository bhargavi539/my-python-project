# Tuples -> immutable in nature
# cannot change the values that already exists in the tuple

my_tuple = (1, 4, 9, 16, 25)
# my_tuple[3] = 64 cannot support item assignment
print(my_tuple)

my_api_list = list(my_tuple)  # converting tuple into list
print("Converted tuple into list", my_api_list)

my_api_list[3] = 64
print("Modified list", my_api_list)

# A tuple can be coverted into list and viceversa
my_tuple = tuple(my_api_list)
print("tuple",my_tuple)
print("list",my_api_list)