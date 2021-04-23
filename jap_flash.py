import argparse
import csv
import random

parser = argparse.ArgumentParser(description="This is a program that takes the"
                                             " users specified text file full"
                                             " of japanese words and provides"
                                             " a test by randomly selecting"
                                             " words")
parser.add_argument("filepath", type=str, help="the filepath to the text file"
                                               " containing all the words to"
                                               " be featured in the test")

args = parser.parse_args()

words = []
with open(args.filepath, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["meaning"] = row["meaning"].split('/')
        words.append(row)

print("Type the answer or q to quit")
print("If you can't answer a question type p to pass")
print()
i = -1
test = "word"
while i != 'q':
    i = -1
    word_ind = random.randint(0, len(words)-1)
    print(words[word_ind][test])
    while i not in words[word_ind]["meaning"] and i != 'p' and i != 'q':
        i = input()
        if i == 'p':
            print("The answer was: {}".format(words[word_ind]["meaning"]))
        if i == 'q':
            pass
        if i in words[word_ind]["meaning"]:
            print("Correct")
            if len(words[word_ind]["meaning"]) > 1:
                print("All meanings are: "
                      "{}".format(words[word_ind]["meaning"]))
