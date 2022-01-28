"""EX02 - One Shot Wordle."""

__author__ = "730460994"

WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
GREEN_BOX: str = "\U0001F7E9"
secret_word: str = "python"
secret_len: int = len(secret_word)


guess: str = input(f"What is your {secret_len}-letter guess? ")  # using f string to substitute secret_len with an integer value equal to len(secret_word) when this expression is evaluated
while len(guess) != secret_len:
    guess = input(f"That was not {secret_len} letters! Try again: ")


idx_check: int = 0
emoji_result: str = ""


while idx_check < secret_len:  # ensuring the while loop only evaluates when the index being checked is less than the length of the secret word
    if guess[idx_check] == secret_word[idx_check]: 
        emoji_result = emoji_result + GREEN_BOX
    else: 
        anywhere: bool = False  # declaring a bool variable to keep track of whether the guessed character exists anywhere in the word
        alt_idx: int = 0  # declaring a variable to check for a match at all of the alternate indicies
        while not anywhere and alt_idx < secret_len:  # while True and the index being checked is less than the length of the secret word this while loop will run
            if guess[idx_check] == secret_word[alt_idx]:
                anywhere = True  # assigning True to the boolean variable anywhere when the current index check of the guessed word is equal to any alternate index in the secret word
            else: 
                alt_idx = alt_idx + 1  # increasing the alternate index so the nested while loop moves towards completion 
        if anywhere: 
            emoji_result = emoji_result + YELLOW_BOX  # if anywhere is True it means the character is anywhere in the guessed word so the program needs to print a yellow box
        else:
            emoji_result = emoji_result + WHITE_BOX  # if anywhere is False it means the character is nowhere in the guessed word so the program needs to print a white box
    idx_check = idx_check + 1  # increasing the index check so the overarching while loop moves towards completion
print(emoji_result)

if guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
