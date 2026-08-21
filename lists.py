fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0])

print(fruits[-1])

fruits[1]  = "blueberry"

print(fruits)

fruits[2] = "lemon"
print(fruits)

fruits.append("date")
print(fruits)

fruits.insert(1, "banana")
print(fruits)

fruits.insert(5, "kiwi")
print(fruits)

fruits.remove("kiwi")
print(fruits)

del fruits[0]
print(fruits)

mixed_list = [1, "hello", 3.14, [1, 2, 3]]
print(mixed_list)