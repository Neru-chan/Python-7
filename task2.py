li = ["a", "b", "cd", "e", "fg"]
count = 0
for s in li:
    if (len(s) >= 2): count += 1

print(f"{count} strings have two or more characters.")