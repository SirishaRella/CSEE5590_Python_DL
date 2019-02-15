#longest substring
l = input("enter the string ")
longest_till_now = ""
longestoverall = ""
# initilize a set
se = set()
#loop through every character in string
for i in range(0, len(l)):
#check if the character is already in set
    c = l[i]
#if it exists then empty the longest_till_now and set
    if c in se:
        longest_till_now = ""
        se.clear()
#if it doesnot exist then add to longest_till_now and to the set
    longest_till_now = longest_till_now + c
    se.add(c)
#check if the current substring lenght is greater than previous substring
#if it is then modify the overalllongest_substring
    if len(longest_till_now) > len(longestoverall):
        longestoverall = longest_till_now
print("the longest substring is", longestoverall)
print(" length is ", len(longestoverall))

