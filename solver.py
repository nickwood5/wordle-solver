all_words_file = open("wordle-words.txt", "r")

valid_words = []
for line in all_words_file:
  stripped_line = line.strip()
  valid_words.append(stripped_line.upper())

all_words_file.close()

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

def generate_options(does_not_contain, contains, valid_letters, invalid_letters, valid_words):
    options = []
    
    for word in valid_words:
        if check_valid(does_not_contain, contains, word, valid_letters, invalid_letters):
            options.append(word)

    return options

def select_option(does_not_contain, contains, valid_letters, invalid_letters, possible_words):
    num_potential_options = []
    for word in possible_words:
        # Assume that all new letters won't be in the guessed word
        new_letters = []
        for letter in word:
            if letter not in contains:
                new_letters.append(letter)

        ideal_does_not_contain = new_letters + does_not_contain

        options_result = generate_options(ideal_does_not_contain, contains, valid_letters, invalid_letters, possible_words)
        num_potential_options.append(len(options_result))
    
    min_words = min(num_potential_options)
    min_index = num_potential_options.index(min_words)

    return possible_words[min_index]

searching = True
does_not_contain = []
contains = []
valid_letters = []
invalid_letters = []

# First guess -> calculated using select_option function on empty game state
word = "STOAE"

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

    valid_words = generate_options(does_not_contain, contains, valid_letters, invalid_letters, valid_words)

    word = select_option(does_not_contain, contains, valid_letters, invalid_letters, valid_words)

    print("Guess word {}".format(word))