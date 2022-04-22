
import random
from sys import prefix


def generateText(nprefix, table):

    generated_text = ""

    for key, value in table.items():
        if nprefix == 1:
            generated_text += key[0]+" " + \
                value[random.randint(0, len(value)-1)]+" "
        else:
            generated_text += " ".join(key)+" "+  value[random.randint(0, len(value)-1)]+" "

    print(generated_text)


def createbigramMap(nprefix, filename):

    file_eof = True
    bigramMap = {}
    prefix = []
    keytoenter = ""

    while file_eof:

        file_line = filename.readline()

        if not file_line:
            file_eof = False
        words = file_line.split()

        i = 0
        k = 1
        while i < len(words)-nprefix:

            prefix.append(words[i])

            if nprefix > 1:

                while len(prefix) < nprefix:
                    prefix.append(words[i + k])
                    k += 1
            keytoenter = tuple(prefix)

            if keytoenter not in bigramMap.keys():
                bigramMap[keytoenter] = [words[i+nprefix]]
            else:
                bigramMap[keytoenter].append(words[i+nprefix])
            prefix = []
            k = 1
            i += 1

    filename.close()
    return bigramMap


prefix_length = 0

print("First Specificy length of prefix for Makrov Imitator\n")

while True:

    try:
        choice = int(input('Please enter the length of the prefix:\n'))
        if choice <= 5:
            prefix_length = choice
            break
    except:
        print("Invalid option, try again\n")

print("Current available texts are:*NOTE THESE ARE PLACEHOLDERS- OTHER FILES MAY BE USED IN DIRECTORY* \n\n AdventuresofHuckleberryFinn.txt \n\n TheSoulsofBlackFolk.txt \n")

while True:
    try:
        text = input("Enter file name of text: ").lower()
        file_text = open(text, encoding="utf8")
        break
    except FileNotFoundError:
        print("Oops! No valid file with that name was found. Try again...")
m_table = createbigramMap(prefix_length, file_text)
print("Reading in: "+text+"...")
print(m_table)
generateText(prefix_length, m_table)
