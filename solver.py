all_words_file = open("wordle-solver/words.txt", "r")

all_words = []
for line in all_words_file:
  stripped_line = line.strip()
  all_words.append(stripped_line)

all_words_file.close()

valid_words = []

for word in all_words:
    if len(word) == 5 and word.isalpha():
        valid_words.append(word.upper())

def check_valid(does_not_contain, contains, word, valid_letters, invalid_letters):

    for invalid_letter in invalid_letters:
        if word[invalid_letter["index"]] == invalid_letter["letter"]:
            return False

    for valid_letter in valid_letters:
        if word[valid_letter["index"]] != valid_letter["letter"]:
            return False

    for letter in contains:
        if word.count(letter) == 0:
            return False
    
    for letter in does_not_contain:
        if word.count(letter) > 0:
            return False
    
    return True

def generate_options(does_not_contain, contains, valid_letters, invalid_letters):
    options = []
    
    for word in valid_words:
        if check_valid(does_not_contain, contains, word, valid_letters, invalid_letters):
            options.append(word)

    return options

searching = True
does_not_contain = []
contains = []
valid_letters = []
invalid_letters = []


getting_input = True
while getting_input:
    first_guess = input("Enter first guess: ")
    if first_guess.isalpha() and len(first_guess) == 5 and first_guess.isupper():
        getting_input = False
    else:
        print("Invalid input...")

word = first_guess

while searching:

    getting_input = True
    while getting_input:
        input_result = input("Enter result of guess {} (b for blank, y for yellow, g for green): ".format(word))
        if (input_result.count('b') + input_result.count('y') + input_result.count('g')) == 5:
            getting_input = False
        else:
            print("Invalid input...")

    for i in range (0, 5):
        result_code = input_result[i]
        letter = word[i]
        log = {"index": i, "letter": letter}
        if result_code == 'b':
            if letter not in contains:
                does_not_contain.append(letter)
            else:
                invalid_letters.append(log)
        else:
            if result_code == 'y':
                invalid_letters.append(log)
                contains.append(letter)
            else:
                if result_code == 'g':
                    valid_letters.append(log)
                    contains.append(letter)

    valid_words = generate_options(does_not_contain, contains, valid_letters, invalid_letters)

    suggesting_word = True
    i = 0
    while suggesting_word:
        if i == len(valid_words):
            print("No possible words...")
            exit()

        print("Guess word {}".format(valid_words[i]))
        getting_input = True
        while getting_input:
            valid = input("Is suggested word valid (y/n): ")
            if valid == 'y' or valid == 'n':
                getting_input = False
            else:
                print("Invalid input...")
        if valid == 'y':
            suggesting_word = False
            word = valid_words[i]
        else:
            i += 1