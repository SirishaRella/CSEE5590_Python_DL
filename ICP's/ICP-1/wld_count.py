#input a sentence
statement = input("Enter a sentence: ")
lettersCount = 0
digitsCount = 0

#Counting number of words
wordCount = statement.split()

for char in statement:
	#counting number of digits
    if char.isdigit():
        digitsCount = digitsCount + 1
		
	#Counting number of letters	
    if char.isalpha():
        lettersCount = lettersCount + 1

print("Words Count", len(wordCount))
print("Letters Count", lettersCount)
print("Digits Count", digitsCount)

