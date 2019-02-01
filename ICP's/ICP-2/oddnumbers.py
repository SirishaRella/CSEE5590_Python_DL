numbers = []
for i in range(100, 500):
    s = str(i)
    if (int(s[0])%2!=0) and (int(s[1])%2!=0) and (int(s[2])%2!=0):
        numbers.append(s)
print( ",".join(numbers))
