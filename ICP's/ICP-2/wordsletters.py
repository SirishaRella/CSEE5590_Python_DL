f = open("siri.txt", "r")
for i in f:
    print("Sentence: " + i + 'Words:' + str(len(i.split())))
    count = 0
    for letter in i:
        if letter.isalpha():
            count = count+1
    print('Letters ' + str(count))

