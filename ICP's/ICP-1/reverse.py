#Entering a number
num = int(input("Enter a three digit number: "))
output = ""

#checking if the length of a string is 3
if len(str(num)) == 3:
    while num != 0:
        remainder = num % 10
        output = output + str(remainder)
        num = num // 10
	#Printing the reverse of a number
    print("The reversed integer is: ", output)
