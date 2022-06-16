
# Ahmad Seyar
# global varibales and we could name anything our dictionary.

lookup_dictionary = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
                     'L': 1, 'M': 3, 'N': 1, 'O':1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4,
                     'X': 8, 'Y': 4, 'Z': 10}

# we created a cal function

def calc_word_points(word):
    points_for_word = 0
    for letter in word:
        # look up the letter and inside the bracket has to be a key which is letter
        points_for_letter = lookup_dictionary[letter]
        # add the points_for_word- accumulate
        points_for_word += points_for_letter
    return points_for_word


# this is a function
def play_word_game():
    outer_list = []   # create list of word to keep track of what user play
    total_points = 0
    while True:
        # ask user for a word
        word = input("Enter a word: ").upper()
        # check to see if a alpha- display error if not alpha
        if not word.isalpha():
            print("enter only letters. Try again, please. ")
            continue
        #   call calc word point to find out # points for a word and we make a call here for the word cal.
        word_points = calc_word_points(word)

        # print # of points for worda
        print(word, "is", word_points, "points")

        # add the word to the list
        inner_list = []
        inner_list.append(word)
        inner_list.append(word_points)
        outer_list.append(inner_list)

        # add the word points to my total points
        total_points += word_points

        # DYWTPA? y/n
        playagain = input ("Do you want to play again? Y/N: ")
        if playagain == "N":
            break


    # print the list of words the user played
    print("Your Words: ", outer_list)
    # print the total points
    print("Total points earned: ", total_points)


def main():
    play_word_game()


main()  # this function means call the main