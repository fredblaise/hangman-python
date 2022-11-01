import random

def main():
  global guessed_letters
  global incorrect_guesses
  global game_won
  global word
  global hidden_word
  
  guessed_letters = []
  incorrect_guesses = 0
  game_won = "no"
  
  print("Welcome to my game of hangman! You'll have 6 attempts tp guess the hidden word. If you fail, you get hanged!\n")

  word_bank = ["fantastic","appealing","popular","promise","dependable","sobriety","quarter","abstraction","pursuing","sabbatical","mountain","phillosophy","periodical","scratchable","fractional","memorized","meteoric","xylophone","permutation","internalize"]

  word = random.choice(word_bank)

  hidden_word = list(word)
  for i in range(len(hidden_word)):
    hidden_word[i] = "?"
  
  print_gallows(incorrect_guesses)

  print("\n")
  print("".join(hidden_word))
  print("\n")

  check_letter()
 
def check_letter():
  global guessed_letters
  global incorrect_guesses
  global game_won
  global word
  global hidden_word
  
  while (incorrect_guesses < 6) and (game_won == "no"):
    guess = str(input(f"Already guessed: {guessed_letters}\nGuess: "))
    
    if len(guess) == 1 and guess.isalpha() == True:
      if (guess in guessed_letters):
        print("\nAlready guessed that letter.")
      elif guess in word:
        print("\nCorrect.")
        for i in range(len(word)):
          if guess == word[i]:
            hidden_word[i] = guess
        guessed_letters.append(guess)
      else:
        print("\nIncorrect.")
        incorrect_guesses += 1
        guessed_letters.append(guess)
    elif guess == word:
      for i in range(len(hidden_word)):
        hidden_word[i] = word[i]
    else:
      print("Please input a single letter or the full word.")

    print("\n")
    print_gallows(incorrect_guesses)
  
    print("\n")
    print("".join(hidden_word))
    print("\n")

    if "?" not in hidden_word:
      game_won = "yes"
      print("Congratulations, you've solved it!")
    elif incorrect_guesses == 6:
      print(f"Sorry, you've lost. The word was {word}.")

def print_gallows(number):
  if (number) == 0:
    print("\
    ------\n\
    |    |\n\
    |     \n\
    |     \n\
    |     \n\
    |     \n\
    ----  ")
  elif (number) == 1:
    print("\
    ------\n\
    |    |\n\
    |    0\n\
    |     \n\
    |     \n\
    |     \n\
    ----  ")
  elif (number) == 2:
    print("\
    ------\n\
    |    |\n\
    |    0\n\
    |    |\n\
    |     \n\
    |     \n\
    ----  ")
  elif (number) == 3:
    print("\
    ------\n\
    |    |\n\
    |    0\n\
    |   /|\n\
    |     \n\
    |     \n\
    ----  ")
  elif (number) == 4:
    print("\
    ------\n\
    |    |\n\
    |    0\n\
    |   /|\ \n\
    |     \n\
    |     \n\
    ----  ")
  elif (number) == 5:
    print("\
    ------\n\
    |    |\n\
    |    0\n\
    |   /|\ \n\
    |   / \n\
    |     \n\
    ----  ")
  else:
    print("\
    ------\n\
    |    |\n\
    |    0\n\
    |   /|\ \n\
    |   / \ \n\
    |     \n\
    ----  ")
    
if __name__ == "__main__":
  main()