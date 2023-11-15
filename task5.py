file = open("mbox-short.txt")
count = 0
for line in file:
    if (line.find("From ", 0, 5) < 0): continue

    print(line.split()[1])
    count += 1

print("There were", count, "lines in the file with From as the first word")