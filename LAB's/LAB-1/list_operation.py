p = input("Enter list of students in python ")
list_p = p.split()
w = input("Enter list of students in web ")
list_w = w.split()
set_p = set(list_p)
set_w = set(list_w)
print("Students in Python class", list_p)
print("Students in Web class", list_w)
#set operation intersection to find the common records
common = set_p & set_w
print("Students common in both classes", list(common))
# perfrom union operation to get all the records and remove the records which are common using the difference (set)
union_p_w = set_p | set_w
print("Students not common in both the classes ", list(union_p_w.difference(common)))
