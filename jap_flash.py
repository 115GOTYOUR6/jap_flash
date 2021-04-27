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

parser.add_argument("test", type=str, choices=["meaning", "hiragana"],
                    help="Determines the information the user will have to"
                         " provide for the words presented.")

args = parser.parse_args()

words = []
line = 1
with open(args.filepath, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["meaning"] = row["meaning"].split('/')
        row["hiragana"] = row["hiragana"].split('/')
        line += 1
        # this should be set to the number of columns in the csv
        if None not in row:
            if len([i for i in row.keys() if row[i] is None]) == 0:
                words.append(row)
            else:
                print("line {} failed".format(line))
        else:
            print("line {} failed".format(line))

print("Type the answer or q to quit")
print("If you can't answer a question type p to pass")
print()
i = -1
info = "word"
while i != 'q':
    i = -1
    word_ind = random.randint(0, len(words)-1)
    print(words[word_ind][info])
    while i not in words[word_ind][args.test] and i != 'p' and i != 'q':
        i = input()
        if i == 'p':
            print("The answer was: {}".format(words[word_ind][args.test]))
            if args.test == "meaning" and words[word_ind]["kanji"] == 'y':
                print("Hiragana: {}".format(words[word_ind]["hiragana"]))
        if i == 'q':
            pass
        if i in words[word_ind][args.test]:
            print("Correct")
            if len(words[word_ind][args.test]) > 1:
                print("All meanings are: "
                      "{}".format(words[word_ind][args.test]))
