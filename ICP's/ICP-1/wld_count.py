statement = input("Enter a sentence: ")
lettersCount = 0
digitsCount = 0
wordCount = statement.split()

for char in statement:
    if char.isdigit():
        digitsCount = digitsCount + 1
    if char.isalpha():
        lettersCount = lettersCount + 1

print("Words Count", len(wordCount))
print("Letters Count", lettersCount)
print("Digits Count", digitsCount)

