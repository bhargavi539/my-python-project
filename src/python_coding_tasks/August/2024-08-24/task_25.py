# Function with multiple arguments
def multiple_args(name1="Akbar",name2="Abrahim",name3="Anthony"):
    print("Multiple Arguments",name1,name2,name3)


multiple_args()
multiple_args("Ram","Sam","Pam")


#4.with return values and with Arguments
def sum_of_two_numbers(num1=100,num2=300):
    return num1+num2

sum1 = sum_of_two_numbers(10,55)
sum2 = sum_of_two_numbers()
sum3 = sum_of_two_numbers(num2=500)
print(sum1)
print(sum2)
print(sum3)