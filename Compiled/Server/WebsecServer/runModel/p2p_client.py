import socket
import os

def run_helper_server(link, username):
    #****For accessing models.py (In Login) by external python script****
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","WebsecServer.settings")
    from Login.models import ModelsActiveStatus
    #print(ModelsActiveStatus.objects.all())
    #********************************************
    user = ModelsActiveStatus.objects.get(username = username)
    statusString = user.statusString

    s = socket.socket()
    port = 5000
    s.connect(("127.0.0.1", port))
    s.sendall(link.encode('utf-8'))
    s.sendall(statusString.encode('utf-8'))
    s.close()

    s2 = socket.socket()
    while True:
        host = ''
        port = 5001
        while True:
            try:
                s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s2.bind((host, port))
                break
            except:
                print("Trying to bind..")
        s2.listen(10)

        c, addr = s2.accept()
        print("Received connection from: " + str(addr))
        receivedData = c.recv(10240).decode('utf-8').split(',')
        print(receivedData)
        s2.close()
        return int(receivedData[0]), int(receivedData[1]), int(receivedData[2]), int(receivedData[3]), int(receivedData[4]), int(receivedData[5]), int(receivedData[6])

#run_helper_server(b"https://www.tutorialspoint.com/index/sort/popular")
