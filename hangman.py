import random
from hangman_word import word_list
end = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives=6
from hangman_art import logo
print(logo)
print(f'Pssst, the solution is {chosen_word}.')
#Create blanks
display=[]
for _ in range(word_length):
    display = ["_"] * word_length

while not end:
    guess = input("guess a letter:").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
           display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end = True
            print("you lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
       end = True
       print("you win")
    from hangman_art import stages
    print(stages[lives])