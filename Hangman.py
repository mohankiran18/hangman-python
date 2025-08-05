import random

# --- STEP 1: Word list and selection ---
words = ['apple', 'banana', 'grapes', 'mango', 'cherry']
word = random.choice(words)
hidden_word = ['_'] * len(word)

# --- STEP 2: Setup game state ---
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman!\n")

# --- STEP 3: Game Loop ---
while wrong_guesses < max_wrong_guesses and '_' in hidden_word:
    # Display current state
    print("\nWord:", ' '.join(hidden_word))
    print("Guessed letters:", ', '.join(guessed_letters))
    print(f"❌ Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    
    # Ask for input
    guess = input("🔤 Guess a letter: ").lower()
    
    # Validation: check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    # Check guess in word
    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("❌ Incorrect!")
        wrong_guesses += 1

# --- STEP 4: End of Game ---
if '_' not in hidden_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
