import random

# List of words to choose from
word_list = ['python', 'django', 'hangman', 'developer', 'programming', 'software', 'engineer']

def select_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                return
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")
    
    print(f"Sorry, you've run out of guesses. The word was: {word}")

# Run the game
hangman()
