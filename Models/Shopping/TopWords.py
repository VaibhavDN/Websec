import os
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd
from nltk.stem import WordNetLemmatizer

lemitizer = WordNetLemmatizer()

dirList = os.listdir("Training")
parentDir = "Training"
print(dirList)
data = ""
wordCounter = {}
topWordsTaken = 200

stpwds = set(stopwords.words('english'))
stpwds.add('html')
stpwds.add('href')
stpwds.add('id')
stpwds.add('com')
stpwds.add('us')
stpwds.add('august')
stpwds.add('aug')
unigram_freq = pd.read_csv("Hundred_unigram_freq.csv")
unigram_freq = unigram_freq.iloc[:,1]
for words in unigram_freq:
    stpwds.add(words.lower())
print(stpwds)
#exit(0)
no_of_dir_done = 0
for directory in dirList:
    data = ""
    if(os.path.isdir(parentDir + "/" + directory) and parentDir + "/" + directory != "__pycache__"):
        no_of_dir_done+=1
        print(str(no_of_dir_done) + ". Directory found: " + directory)
        
        fobject = open(parentDir + "/" + directory + "/" + directory + "_bodyContentWithoutTags.txt")
        while True:
            line = fobject.readline()
            if line == "":
                break

            #Housekeeping
            tokenizer = RegexpTokenizer(r'\w+') #\w+ only allow [a-zA-Z0-9_] i.e remove punctuation
            lineSplit = tokenizer.tokenize(line)
            #print(lineSplit)
            
            for word in lineSplit:
                word = word.lower()
                if (word not in stpwds and word.isalpha() and len(word)>2):
                    word = lemitizer.lemmatize(word)
                    try:
                        if word not in wordCounter:
                            wordCounter[word] = 1
                        else:
                            wordCounter[word]+=1
                        data+=word+" "
                    except Exception as e:
                        print("Exception due to word: " + str(word) + "\nError: " + str(e))

        fobject.close()
        #print(data)

        #Sort the dictionary in decending order
        wordCounter = dict(sorted(wordCounter.items(), key=lambda x: x[1], reverse=True))   #sorted fun returns tuple so dict is used to convert it back to dictionary
        i=0
        
        for key in wordCounter:
            if i > topWordsTaken:
                break
            print(key + ": " + str(wordCounter[key]))
            i+=1
        
            #print(data)
        print("*******************************************")

i=0
fobject = open("TopWords.csv", "w")
for key in wordCounter:
    if i > topWordsTaken:
        break
    fobject.write(key + ",")
    i+=1

fobject.write("\n")

i=0
for key in wordCounter:
    if i > topWordsTaken:
        break
    fobject.write(str(wordCounter[key]) + ",")
    i+=1
print("Dataset created in: " + os.path.abspath("./"))
        