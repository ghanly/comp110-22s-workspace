"""EX01 - Chardle - A cute step toward Wordle."""

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

indicies: int = 0 

if single_char == word[0]: 
    print(single_char + " found at index 0")
    indicies = indicies + 1
if single_char == word[1]: 
    print(single_char + " found at index 1")
    indicies = indicies + 1
if single_char == word[2]: 
    print(single_char + " found at index 2")
    indicies = indicies + 1
if single_char == word[3]: 
    print(single_char + " found at index 3")
    indicies = indicies + 1
if single_char == word[4]: 
    print(single_char + " found at index 4")
    indicies = indicies + 1

if indicies == 0: 
    print("No instances of " + single_char + " found in " + word) 
if indicies == 1:
    print("1 instance of " + single_char + " found in " + word)
if indicies == 2:
    print("2 instances of " + single_char + " found in " + word)
if indicies == 3:
    print("3 instances of " + single_char + " found in " + word)
if indicies == 4: 
    print("4 instances of " + single_char + " found in " + word)
if indicies == 5: 
    print("5 instances of " + single_char + " found in " + word)


    



    
 
