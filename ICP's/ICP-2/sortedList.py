list = ["1", "4", "0", "6", "9"]
new = []
for i in range(0, len(list)):
    list[i] = int(list[i])

print(sorted(list, key=int))

