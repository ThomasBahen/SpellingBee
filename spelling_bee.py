import argparse

MINIMUM_WORD_SIZE=5

def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def load_answers(letters,valid_words):
    answers = []
    valid_words = [w for w in valid_words if not w.strip(letters)]
    threes = [w for w in valid_words if all(l in w for l in list(letters))]
    answers.append(threes)
    non_threes = [w for w in valid_words if w not in threes and (len(w)>MINIMUM_WORD_SIZE-1 and letters[0] in w)]
    answers.append(non_threes)
    return answers



if __name__ == '__main__':
    arg = argparse.ArgumentParser()

    #parse letters put into the spelling bee solver
    arg.add_argument("-l", type=str, default="cbriwok")
    args = arg.parse_args()
    valid_words = load_words()
    answers =load_answers(letters=args.l, valid_words=valid_words)
    print("Three point words:{0}".format(answers[0]))
    print("Other valid words:{0}".format(answers[1]))
