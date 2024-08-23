#Task #11 -
#✅ Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

fibonacci = int(input("Enter the number of digits you want to print in Fibonacci series "))
value1 = 0
value2 = 1
print("Fibonacci series:",end=" ")
for _ in range(fibonacci):
    print(value1,end=" ")
    value3 = value2 + value1
    value1 = value2
    value2 = value3


