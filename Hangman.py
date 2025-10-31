import random
def hangman():
    word_hints = {
        "python": "A popular programming language named after a snake.",
        "apple": "A fruit that keeps the doctor away.",
        "computer": "An electronic device used to process information.",
        "hangman": "The name of this very game!",
        "banana": "A yellow fruit that monkeys love."
    }
    word = random.choice(list(word_hints.keys()))
    hint = word_hints[word]
    guessed_letters = []
    attempts = 6  
    print("🎯 Welcome to Hangman!")
    print("You have 6 incorrect guesses. Good luck!\n")
    print(f"💡 Hint: {hint}\n") 
    display_word = ["_"] * len(word)
    while attempts > 0 and "_" in display_word:
        print("Word: " + " ".join(display_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter!\n")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.\n")
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.\n")
            attempts -= 1
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("😢 Out of attempts! The word was:", word)
if __name__ == "__main__":
    hangman()
