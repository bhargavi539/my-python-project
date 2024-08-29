cities =("Hyderabad","Tokyo","Copenhagen","Paris")
print("Paris" in cities)
print("paris" in cities)
print("Mumbai" in cities)

cities_list = list(cities)
cities_list.append("Amaravati")
print(cities_list,type(cities_list))

cities = tuple(cities_list)
print(cities,type(cities))