# Encapsulation with access controllers like public and private

class Myclass:
    public_var = "I am a public variable"
    __private_var = "I am a private variable"
    balance = 0
    __password = "123abc"
    _protected_var = "protected variable"


object = Myclass()
print(object.public_var)
# print(object.private_var) -> private attributes are not accessed outside the class
print(object.balance)
#print(object.__password)
print(object._protected_var) # -> protected variables are accessible within the same package
