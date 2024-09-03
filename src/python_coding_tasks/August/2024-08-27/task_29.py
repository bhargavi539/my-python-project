#*args takes multiple values in the argument,but the function definition
# can have only one argument as *args,
def make_pizza(*toppings,base):
    for top in toppings:
        print(top,base)
make_pizza("Mushrooms","tomato",base="thin crust")

