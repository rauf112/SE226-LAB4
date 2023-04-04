# a

x = {i: (i - 1) * i for i in range(1, 31)}

print(x)

# b
for a, b in x.items():
    print(f"{a}: {b}")

# c
summ = 0
for y in x.values():
    summ += y
print("summary =", summ)

# d

a = int(input("Write a key you want to remove: "))

if a in x:
    del x[a]
    print("After the removal of the item with key", a, ":")
    print(x)
else:
    print("Wrong input!")
