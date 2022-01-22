"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730460994"

word: str = input("Enter a 5-character word: ")
if len(word) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_char + " in " + word)

if single_char == word[0]: 
    print(single_char + " found at index 0")
if single_char == word[1]: 
    print(single_char + " found at index 1")
if single_char == word[2]: 
    print(single_char + " found at index 2")
if single_char == word[3]: 
    print(single_char + " found at index 3")
if single_char == word[4]: 
    print(single_char + " found at index 4")

matches: int = single_char in word[0]
matches = matches + (single_char in word[1])
matches = matches + (single_char in word[2])
matches = matches + (single_char in word[3])
matches = matches + (single_char in word[4])

if matches == 0: 
    print("No instance of " + single_char + " found in " + word) 
if matches == 1:
    print("1 instance of " + single_char + " found in " + word)
if matches == 2:
    print("2 instances of " + single_char + " found in " + word)
if matches == 3:
    print("3 instances of " + single_char + " found in" + word)


    



    
 
