#Converting list of tuples with Dictionary keys and values.
input = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)),
         ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]

#Declaring empty dictionary
result_dict = {}

#For every input
for item in input:
    res_tuple = item
    if res_tuple[0] in result_dict.keys():
        result_dict[res_tuple[0]].append(res_tuple[1])
    else:
        result_dict[res_tuple[0]] = [res_tuple[1]]


#printing dictionary
for key, value in result_dict.items():
    print(key, sorted(value))
