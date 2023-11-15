file = open("romeo.txt", "r")
result = []
for line in file:
    li = line.split()
    result+=li

result = sorted(list(set(result)))
print(result)