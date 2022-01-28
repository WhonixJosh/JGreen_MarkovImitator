
import random
from sys import prefix

def generateText(nprefix,table):
    #TODO: using markov chain table generate 100 to 200 word text box If there are multiple possible words, one is chosen at random to 
    #append to the output. Each time a word is chosen, the prefix is updated by removing the first word and 
    # adding the chosen word. The process continues until the end marker is appended to the output, as at 
    #the end of the sample, or until a pre-determined number of words are generated
    generated_text = ""

    for key, value in table.items():
        if nprefix == 1:
           generated_text += key[0]+" "+value[random.randint(0,len(value)-1)]+" "
        elif nprefix == 2:
            generated_text += value[random.randint(0,len(value)-1)]+" " + key[1] + " " 
        elif nprefix == 3:
             generated_text += value[random.randint(0,len(value)-1)]+" " + key[1] + " " + key[2]+" "    

    print(generated_text)

def createBigramMap(nprefix, filename):
    
    file_eof = True
    bigrammap = {}
    prefix = ""
    keytoenter =""
    while file_eof:
        
        file_line = filename.readline()
        if not file_line:
            file_eof = False
        words = file_line.split()
        i=0
        
        while i <  len(words)-nprefix :
            
            if nprefix == 2:
                prefix = words[i]+" "+words[i+1]
            elif nprefix == 3:
                prefix = words[i]+" "+words[i+1]+" "+words[i+2]
            elif nprefix == 1:
                prefix = words[i]
            
            keytoenter = tuple(prefix.split(" "))
            if keytoenter not in bigrammap.keys():
                bigrammap[keytoenter] = [words[i+nprefix]]
            else:
                    bigrammap[keytoenter].append(words[i+nprefix])
            i+=1     
    filename.close()
    return bigrammap

prefix_length = 0

print("First Specificy length of prefix for Makrov Imitator\n")

while True:
    print('1) for length of 1\n')
    print('2) for length of 2\n')
    print('3) for length of 3\n')

    choice = input('Please enter the length of the prefix:\n')
    
    if  choice == "1":
        prefix_length = 1
        break
    elif choice == "2": 
        prefix_length = 2
        break
    elif choice == "3":
        prefix_length = 3
        break
    else:
        print("Invalid option, try again\n")

print("Current available texts are: \n\n AdventuresofHuckleberryFinn.txt \n\n TheSoulsofBlackFolk.txt \n")

while True:
    try:
        text = input("Enter file name of text: ").lower()
        file_text = open(text, encoding="utf8")
        break
    except FileNotFoundError:
        print("Oops! No valid file with that name was found. Try again...")
m_table = createBigramMap(prefix_length,file_text)
print("Reading in: "+text+"...")

# print(m_table)


generateText(prefix_length,m_table)
 
