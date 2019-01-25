num = int(input("Enter a three digit number: "))
output = ""
if len(str(num)) == 3:
    while num != 0:
        remainder = num % 10
        output = output + str(remainder)
        num = num // 10

    print("The reversed integer is: ", output)
