import argparse

def load_three_point_words(letters_list,letters_string):
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
        valid_words = [w for w in valid_words if all(l in w for l in letters_list) and not w.strip(letters_string)]
    return valid_words


if __name__ == '__main__':
    arg = argparse.ArgumentParser()

    #parse letters put into the spelling bee solver
    arg.add_argument("-l", type=str, default="mnopytr")
    args = arg.parse_args()
    three_pointers =load_three_point_words(letters_list=list(args.l),letters_string=args.l)
    print(three_pointers)
