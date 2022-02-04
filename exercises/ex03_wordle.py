"""EX03 - Wordle."""

__author__ = "730460994"


def contains_char(guess: str, single_char: str) -> bool: 
    """Indicates if the single char exists in the guessed word."""
    # creating a function to call when I want to evaluate if the character exists in the secret word or not
    assert len(single_char) == 1
    idx_check: int = 0
    while idx_check < len(guess):  
        if guess[idx_check] == single_char: 
            return True
        else: 
            anywhere: bool = False  
            alt_idx: int = 0 
            while not anywhere and alt_idx < len(guess):  
                if guess[alt_idx] == single_char:
                    anywhere = True  
                else: 
                    alt_idx = alt_idx + 1  
            if anywhere: 
                return True  
            else:
                return False 
        idx_check = idx_check + 1 
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns an emoji string that correlates to the accuracy of the guess."""
    # creating a function to call when I want to print the emoji result of the comparison of the guessed word to the secret word
    assert len(guess) == len(secret_word)
    emoji_result: str = "" 
    idx_check: int = 0
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    GREEN_BOX: str = "\U0001F7E9"
    while idx_check < len(secret_word):
        if contains_char(secret_word, guess[idx_check]) and guess[idx_check] == secret_word[idx_check]:
            emoji_result = emoji_result + GREEN_BOX
        else:
            if contains_char(secret_word, guess[idx_check]):
                emoji_result = emoji_result + YELLOW_BOX
            else:
                emoji_result = emoji_result + WHITE_BOX
        idx_check = idx_check + 1
    return emoji_result


def input_guess(expected_len: int) -> str: 
    """Prompts the user for a guess that is the expected length."""
    # creating a function to call when I want to prompt the user for a guess that is the expected length
    guess: str = input(f"Enter a {expected_len} character word: ")  
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    # creating a main function to tie in the previous 3 functions
    secret_word: str = "codes"
    # establishing what the secret word is as a variable
    max_turns: int = 6
    current_turn: int = 1
    # creating a counter to only allow 6 turns
    won: bool = False
    # creating a bool variable to act as a 'switch' that will allow the while loop to iterate when the player has not yet won
    while current_turn <= max_turns and not won: 
        print(f"=== Turn {current_turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {current_turn}/6 turns!")
            won = True
        else: 
            current_turn = current_turn + 1
            if not won and current_turn > max_turns:   
                # since not yet won and after turn 6, I want to print this result     
                print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()