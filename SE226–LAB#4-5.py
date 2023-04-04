# a
divided = {'Tony': 41, 'Rhodey': 43, 'Nat   ': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = {**divided, **we_fall}

print("Name\tAge")
for a, b in united_we_stand.items():
    print(f"{a}\t{b}")
# b
print()
print("Removing Nat.......")
del united_we_stand['Nat   ']

print("Name\tAge")
for a, b in united_we_stand.items():
    print(f"{a}\t{b}")
# c
print()
print("Name\tAge")
for a, b in sorted(united_we_stand.items()):
    print(f"{a}\t{b}")
# d
print()
maxAge = max(united_we_stand.values())
minAge = min(united_we_stand.values())

print(f"Maximum age: {maxAge}")
print(f"Minimum age: {minAge}")