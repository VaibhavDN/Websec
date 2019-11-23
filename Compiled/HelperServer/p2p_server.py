import socket
import os
from importlib.machinery import SourceFileLoader

s = socket.socket()
host = ''
port = 5000
s.bind((host, port))

s.listen(10)

while True:
    c, addr = s.accept()
    print("Received connection from: " + str(addr))
    receivedData = c.recv(10240).decode('utf-8').split('|')

    print(receivedData) #link | statusString
    path_HelperServer = os.path.abspath("./")
    path_ModelsHelperServer = path_HelperServer.split('/')
    path_ModelsHelperServer.pop()
    path_ModelsHelperServer.append("Models_Helper_Server")
    path_ModelsHelperServer = '/'.join(path_ModelsHelperServer)
    
    testSitesPath = path_ModelsHelperServer + '/' + "TestSites.txt"
    fobject = open(testSitesPath, "w")
    fobject.write(receivedData[0])
    fobject.close()
    
    parser = SourceFileLoader('ParserModule', path_ModelsHelperServer+"/HTMLParser.py").load_module()
    prediction1, prediction2, prediction3, prediction4, prediction5, prediction6, prediction7 = parser.startParser(path_ModelsHelperServer, 3, receivedData[1])
    print("Prediction1: "+str(prediction1[0]))
    returnString = ""
    returnString+= (str(prediction1).replace('[', '')).replace(']', '') + ","
    returnString+= (str(prediction2).replace('[', '')).replace(']', '') + "," 
    returnString+= (str(prediction3).replace('[', '')).replace(']', '') + "," 
    returnString+= (str(prediction4).replace('[', '')).replace(']', '') + "," 
    returnString+= (str(prediction5).replace('[', '')).replace(']', '') + "," 
    returnString+= (str(prediction6).replace('[', '')).replace(']', '') + "," 
    returnString+= (str(prediction7).replace('[', '')).replace(']', '')
    print(returnString)
    s2 = socket.socket()
    port = 5001
    s2.connect(("127.0.0.1", port))
    s2.sendall(returnString.encode('utf-8'))
    s2.close()
    
s.close()
    

    
    
