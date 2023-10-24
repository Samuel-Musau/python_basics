#comparisson operators

a=5
b=22
fruits = ["mango", "orange", "banana", "watermelon", 67]
num = [11, 3, 7, 0, 14]
num.sort()
num[3] = 9

print(fruits)

# tuple immutable-cannot change
cars = ("Toyota", "mercedes", "nissan")
print(cars)
print(cars[0])
tup = cars*3
print(tup)
print(tup.count("nissan"))
name = ("dan", "kim", ["rose", "kim"])
print(name)
# sets unordered
days = {"mon", "tue", "wed", "thur", "fri"}
print(days)

# dictionary
staff_details = { "name":"sam","age":22,"company":"kiro_ventures", "gender":"male"}
print(staff_details)
print(f"name %s" %staff_details["name"])