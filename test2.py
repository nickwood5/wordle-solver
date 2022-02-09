from pickle import FALSE


a_file = open("words.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  list_of_lists.append(stripped_line)

a_file.close()

print(list_of_lists)

valid_words = []

for word in list_of_lists:
    if len(word) == 5 and word.isalpha():
        valid_words.append(word.upper())

print(valid_words)


does_not_contain = ['R', 'O', 'S', 'B', 'D']
contains = ['A', 'E']
known_positions = ['0', 'A', '0', 'E', '0']
known_not_positions = ['A', '0', '0', '0', 'E']

#1 AROSE
#2 BAAED
#3 CACEI

def check_valid(does_not_contain, contains, word, known_positions, known_not_positions):
    for i in range (0, 5):
        if known_positions[i] != '0' and word[i] != known_positions[i]:
            #print("Word {} does not have leter {} at index {}".format(word, known_positions[i], i))
            return False
        
        for i in range (0, 5):
            if known_not_positions[i] != '0' and word[i] == known_not_positions[i]:
                #print("Word {} does not have leter {} at index {}".format(word, known_positions[i], i))
                return False

    for letter in contains:
        if word.count(letter) == 0:
            return False
    
    for letter in does_not_contain:
        if word.count(letter) > 0:
            #print("Word {} contains letter {}".format(word, letter))
            return False

    
    
    return True

options = []

for word in valid_words:
    if check_valid(does_not_contain, contains, word, known_positions, known_not_positions):
        options.append(word)
        print("aaa")

print(options)