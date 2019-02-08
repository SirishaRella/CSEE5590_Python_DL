import numpy
from collections import Counter
frequent_list = []
array = numpy.random.randint(20, size=15)
print(array)
frequent = Counter(array)
print(frequent)

print("Most frequent items")
for key,value in frequent.items():
    if value == max(frequent.values()):
        print(key)




