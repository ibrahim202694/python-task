word = input("Enter a word: ")
reverseword = ""

for character in word:
    reverseword = character + reverseword

if reverseword != word:
    print("It's not a palindrome")
elif reverseword == word:
    print("It's a palindrome")
