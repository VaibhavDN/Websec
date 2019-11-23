import os
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from importlib.machinery import SourceFileLoader
from nltk.stem import WordNetLemmatizer

lemitizer = WordNetLemmatizer()
def makeGamingDataset(pathToModels, option):
    dirList = []
    selectedFolder = ""
    datasetFile = ""

    #option = int(input("Choose:\n1. GamingSites.txt\n2. TestSites.txt: "))
    if option == 1:
        fobjectLinks = open(pathToModels + '/' + "TrainSites.txt", "r")
        selectedFolder = pathToModels + '/' + "Training"
        dirList = os.listdir(pathToModels + '/' + "Training")
        datasetFile = pathToModels + '/' + "GamingTopWordsDataset.csv"
    else:
        fobjectLinks = open(pathToModels + '/' + "TestSites.txt", "r")
        selectedFolder = pathToModels + '/' + "Testing"
        dirList = os.listdir(pathToModels + '/' + "Testing")
        datasetFile = pathToModels + '/' + "TestDataset.csv"


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
    addStpwdsList = ['jan','january','feb','february','mar','march','aug','august','sep','september','oct','october','nov','november','dec','december']
    for stpword in addStpwdsList:
        stpwds.add(stpword)
    #print(stpwds)

    fobject = open(pathToModels + '/' + "Gaming/GamingTopWords.csv", "r")   #!Don't Change this
    features = fobject.readline()
    fobject.close()

    fobject = open(datasetFile, "w")    #To reset the file
    fobject.write("Site Links,"+features.replace("\n","GamingSite\n"))
    fobject.close()

    features = features.split(',')
    print(features)

    featuresList = []
    featureValue = [0]*len(features)

    no_of_dir_done = 0
    for directory in dirList:
        data = ""
        wordCounter = dict(zip(features, featureValue))
        print(wordCounter)
        if(os.path.isdir(selectedFolder + "/" + directory) and (selectedFolder + "/" + directory != "__pycache__")):
            no_of_dir_done+=1
            print(str(no_of_dir_done) + ". Directory found: " + directory)

            fobject = open(selectedFolder + "/" + directory + "/" + directory + "_SiteLink.txt")
            siteLink = fobject.readline()
            fobject.close()
            
            fobject = open(selectedFolder + "/" + directory + "/" + directory + "_bodyContentWithoutTags.txt")
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
                            if word in features:
                                wordCounter[word]+= 1
                        
                            data+=word+" "
                        except Exception as e:
                            print("Exception due to word: " + str(word) + "\nError: " + str(e))

            fobject.close()
            #print(data)
            
            i=0
            
            #print(wordCounter)
            fobject = open(datasetFile, "a")
            fobject.write(siteLink.replace("\n" ,","))
            for key in wordCounter:
                if i > topWordsTaken:
                    break
                print(key + ": " + str(wordCounter[key]))
                fobject.write(str(wordCounter[key])+",")
                i+=1
            if option == 1:
                fobject.write("1,")
            fobject.write("\n")
                #print(data)
            fobject.close()
            print("*******************************************")

    model = SourceFileLoader("ModelModule", pathToModels + '/' + "Gaming/Gaming_Model_run.py").load_module()
    prediction = model.runModel(pathToModels)
    return prediction


#*********Testing***********
#makeGamingDataset("/home/vaibhav/Prog/Minor/Models",2)
