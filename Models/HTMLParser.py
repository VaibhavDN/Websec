from selenium import webdriver
from bs4 import BeautifulSoup, Comment
import os, shutil
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from importlib.machinery import SourceFileLoader
import requests
#import isGameSite

def startParser(pathToModels, option):
    #***************Housekeeping*****************
    fobject = open("score.txt", "w")  # Emptying the score file
    fobject.close()
    #********************************************

    testingFolder = pathToModels + '/' + "Testing"
    if(os.path.isdir(testingFolder)):
        shutil.rmtree(testingFolder)

    folder = ""
    #option = int(input("Choose:\n1. TrainSites.txt\n2. TestSites.txt: "))
    if option == 1:
        fobjectLinks = open(pathToModels + '/' + "TrainSites.txt", "r")
        folder = pathToModels + '/' + "Training"
    else:
        fobjectLinks = open(pathToModels + '/' + "TestSites.txt", "r")
        folder = pathToModels + '/' + "Testing"

    if not os.path.exists(folder):
        os.makedirs(folder)

    while True:
        inputLink = fobjectLinks.readline()
        print(inputLink.replace('\n', ''))
        if inputLink == '':
            break

        hostname = inputLink.split('/')
        try:
            finalDomain = hostname[2].replace('.', '_')
        except:
            finalDomain = hostname[1].replace('.', '_')
        print(finalDomain)

        # Make new directory if it doesn't exist.
        dirName = folder + "/" + finalDomain
        if not os.path.exists(dirName):
            os.makedirs(dirName)

#*******Requests**********
#! *******************************************************    
        try:    
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
            html = requests.get(inputLink, headers=headers).text
            soup = BeautifulSoup(html, 'lxml')
            bodyContent = soup.body
            # Remove all script and style elements
            for script in bodyContent(["script", "style"]):
                script.decompose()
            bodyContentTxt = bodyContent.get_text()
            bodyContentStr = str(bodyContentTxt)
            bodyWithoutSpaces = bodyContentStr.replace(" ","")
            bodyWithoutSpaces = bodyContentStr.replace("\n","")
            bodyContentLength = len(bodyWithoutSpaces)
            print(bodyWithoutSpaces)
            print(bodyContentLength)
        except Exception as e:
            print("Exception: " + str(e))
            #return 0
#! ******************************************************* 
#********Selenium**********
        if(bodyContentLength<1000):
            print("************Running selenium**************")
            try:
                driver = webdriver.Firefox()
                driver.get(inputLink)
                print(driver.title + '\n')
                html = driver.page_source
                driver.close()
                soup = BeautifulSoup(html, 'lxml')
                # Extract entire body's content
                bodyContent = soup.body
                # print(bodyContent)
            except Exception as e:
                print("Error: " + str(e))

        # Write the sites link in a file
        try:
            fobject = open(dirName+"/"+finalDomain+"_SiteLink.txt", "w")
            fobject.write(inputLink+"\n")
            fobject.close()
        except Exception as e:
            print("Error occurred: " + str(e))

        # Extract all the scripts in body
        try:
            scripts = soup.find_all('script')
            fobject = open(dirName+"/"+finalDomain+"_scripts.txt", "w")
            for i in range(0, len(scripts)):
                fobject.write(str(scripts[i].get("src"))+"\n")
            fobject.close()
        except Exception as e:
            print("Error: " + str(e))

        try:
            fobject = open(dirName+"/"+finalDomain+"_bodyContent.txt", "w")
            for text in bodyContent:
                fobject.write(str(text))
            fobject.close()
        except Exception as e:
            print("Error: " + str(e))

        # Extract all the links in body
        try:
            linksInBody = bodyContent.find_all('a')
            fobject = open(dirName+"/"+finalDomain+"_linksInBody.txt", "w")
            for i in range(0, len(linksInBody)):
                fobject.write(str(linksInBody[i])+"\n")
            fobject.close()
        except Exception as e:
            print("Error: " + str(e))

        # Extract entire body content without tags
        try:
            garbageCounter = 0

            # Remove all script and style elements
            for script in bodyContent(["script", "style"]):
                script.decompose()

            bodyContentWithoutTags = bodyContent.get_text()
            fobject = open(dirName+"/"+finalDomain +
                           "_bodyContentWithoutTags.txt", "w")
            for text in bodyContentWithoutTags:
                if text == '\n' or text == ' ':
                    garbageCounter += 1
                else:
                    garbageCounter = 0

                if garbageCounter <= 1:
                    fobject.write(str(text))
            fobject.close()
        except Exception as e:
            print("Error: " + str(e))

    #!Ignore the code below (Don't delete)
    '''
            #********************************************
            try:
                fobject = open(dirName+"/"+finalDomain+"_bodyContentWithoutTags.txt", "r")
                counter = 0
                no_of_words_to_scan = 1000
                loopCounter = 0
                while loopCounter < no_of_words_to_scan:
                    line = fobject.readline()
                    if line == '':
                        break
                    text = word_tokenize(line)
                    pos = pos_tag(text)
                    print(pos)
                    for i in range(0, len(pos), 1):
                        loopCounter+=1
                        if pos[i][1][0] == 'N': #Send for check if NOUN
                            if len(pos[i][0]) != 1: #To skip only 1 letter words
                                returnVal = isGameSite.find_in_database(pos[i][0])

                            if returnVal == 0:
                                counter+=1
                                print("No of hits: " + str(counter))
                    
                fobject = open("score.txt", "a+")
                fobject.write("Site Link: " + inputLink)
                fobject.write("No of hits: " + str(counter) + "\n")
                fobject.write("No of iterations: " + str(no_of_words_to_scan) + "\n")
                fobject.write("Score: " + str((counter/no_of_words_to_scan)*100) + "\n\n")
                fobject.close()

            except Exception as e:
                print(e)
        '''
    fobjectLinks.close()
    #**************Making category specific dataset*************
    prediction1=0
    prediction2=0
    prediction3=0
    prediction4=1
    prediction5=1
    prediction6=0
    #makeDataset = SourceFileLoader("DatasetMakerModule", pathToModels + '/' + "Gaming/MakeGamingDataset.py").load_module()
    #prediction1 = makeDataset.makeGamingDataset(pathToModels, option)
    #makeDataset = SourceFileLoader("DatasetMakerModule", pathToModels + '/' + "Shopping/MakeShoppingDataset.py").load_module()
    #prediction2 = makeDataset.makeShoppingDataset(pathToModels, option)
    #makeDataset = SourceFileLoader("DatasetMakerModule", pathToModels + '/' + "Payment/MakePaymentDataset.py").load_module()
    #prediction3 = makeDataset.makePaymentDataset(pathToModels, option)
    #makeDataset = SourceFileLoader("DatasetMakerModule", pathToModels + '/' + "Movie/movie_model_run.py").load_module()
    #prediction4 = makeDataset.cral(pathToModels,bodyContentWithoutTags)
    #makeDataset = SourceFileLoader("DatasetMakerModule", pathToModels + '/' + "VideoStreaming/stream_model_run.py").load_module()
    #prediction5 = makeDataset.cral(pathToModels,bodyContentWithoutTags)
    #makeDataset = SourceFileLoader("DatasetMakerModule", pathToModels + '/' + "Tech/app.py").load_module()
    #prediction6 = makeDataset.predict(pathToModels,soup)
    makeDataset = SourceFileLoader("DatasetMakerModule", pathToModels + '/' + "EntertainmentAndAdult/EntertainmentAndAdult.py").load_module()
    prediction7 = makeDataset.predict(pathToModels,bodyContentWithoutTags)
    '''if(prediction2 == 1):
        prediction2=2
    if(prediction3 == 1):
        prediction3=3
    if(prediction4 == 0):   #Ouch!!
        prediction4=4
    if(prediction5 == 0):   #Ouch!!
        prediction5=5
    if(prediction6 == 1):
        prediction6=6'''
    return prediction1,prediction2,prediction3,prediction4,prediction5,prediction6,prediction7
