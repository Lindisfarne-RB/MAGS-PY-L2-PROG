import random
def choose_random_word():
 words = []
 with open('sowpods.txt', 'r') as file:
 line = file.readline()
 while line:
 words.append(line.replace("\n", "".strip()))
 line = file.readline()
 choice = words[random.randint(0, len(words) - 1)]
 return choice
print("Welcome to Hangman!")
secret_word = choose_random_word()
dashes = list(secret_word)
display_list = []
for i in dashes:
 display_list.append("_")
count = len(secret_word)
guesses = 0
letter = 0
used_list = []
while count != 0 and letter != "exit":
 print(" ".join(display_list))
 letter = input("Guess your letter: ")
 if letter.upper() in used_list:
 print("Oops! Already guessed that letter.")
 else:
 for i in range(0, len(secret_word)):
 if letter.upper() == secret_word[i]:
 display_list[i] = letter.upper()
 count -= 1
 guesses += 1
 used_list.append(letter.upper())
if letter == "exit":
 print("Thanks!")
else:
 print(" ".join(display_list))
 print("Good job! You figured that the word is " + secret_word + "
after guessing %s letters!" % guesses)
"""
Practice Python exercise 32
Hangman
http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
"""
import random
def pick_random_word():
 """
 This function picks a random word from the SOWPODS
 dictionary.
 """
 # open the sowpods dictionary
 with open("sowpods.txt", 'r') as f:
 words = f.readlines()
 # generate a random index
 # -1 because len(words) is not a valid index into the list `words`
 index = random.randint(0, len(words) - 1)
 # print out the word at that index
 word = words[index].strip()
 return word
def ask_user_for_next_letter():
 letter = input("Guess your letter: ")
 return letter.strip().upper()
def generate_word_string(word, letters_guessed):
 output = []
 for letter in word:
 if letter in letters_guessed:
 output.append(letter.upper())
 else:
 output.append("_")
 return " ".join(output)
if __name__ == '__main__':
 WORD = pick_random_word()
 letters_to_guess = set(WORD)
 correct_letters_guessed = set()
 incorrect_letters_guessed = set()
 num_guesses = 0
 print("Welcome to Hangman!")
 while (len(letters_to_guess) > 0) and num_guesses < 6:
 guess = ask_user_for_next_letter()
 # check if we already guessed that
 # letter
 if guess in correct_letters_guessed or \
 guess in incorrect_letters_guessed:
 # print out a message
 print("You already guessed that letter.")
 continue
 # if the guess was correct
 if guess in letters_to_guess:
 # update the letters_to_guess
 letters_to_guess.remove(guess)
 # update the correct letters guessed
 correct_letters_guessed.add(guess)
 else:
 incorrect_letters_guessed.add(guess)
 # only update the number of guesses
 # if you guess incorrectly
 num_guesses += 1
 word_string = generate_word_string(WORD,
correct_letters_guessed)
 print(word_string)
 print("You have {} guesses left".format(6 - num_guesses))
 # tell the user they have won or lost
 if num_guesses < 6:
 print("Congratulations! You correctly guessed the word
{}".format(WORD))
 else:
 print("Sorry, you list! Your word was {}".format(WORD))