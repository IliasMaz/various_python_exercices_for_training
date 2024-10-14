import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
#testarw code
print(f"The solution is {chosen_word}.\n")

#create blanks
display = []
for _ in range(word_length):
    display += "_"
    
 # Use a while loop to let the user guess again. 
 # The loop should only stop once the user has guessed all the letters
 # in the chosen_word and 'display' has no more blanks ("_"). 
 # Then you can tell the user they've won.
 
end_of_game = False
 
while not end_of_game:
    
      #check guessed letter
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")                    
#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

# Check if there are no more "_" left in 'display'. 
# Then all letters have been guessed.   
if "_" not in display:
    end_of_game = True
    print(f"You Win!\n The Correct word is {chosen_word}! ")
#print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
print(stages[lives])    