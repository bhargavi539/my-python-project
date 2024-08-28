my_shopping_list = ["bread", "milk", "eggs"]
print(my_shopping_list[0])
print(len(my_shopping_list))


def bring_more_food(my_sh_list):
    more_item = input("Enter new item to the list")
    my_sh_list.append(more_item)
    #my_sh_list.remove(more_item)
    return my_sh_list


lst = bring_more_food(my_shopping_list)
print(lst)