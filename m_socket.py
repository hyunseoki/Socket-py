from abc import *
import socket
import time


class baseSocket(metaclass=ABCMeta):
    def __init__(self, ip = 'localhost', port=8089):
        self._ip = ip
        self._port = port
        self._socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def disconnect(self):
        self._socketObj.close()
        print('connection disconnected')
    
    @abstractmethod
    def sendMsg(self):
        pass

    @abstractmethod
    def receiveMsg(self):
        pass

  
class serverSocket(baseSocket):
    def bindAndListen(self):
        self.bind()
        self.listen()

    def bind(self):
        self._socketObj.bind((self._ip, self._port))
        print('server established') 
    
    def listen(self):
        self._socketObj.listen(1)
        print('connection waiting') 
        self.clientSocket, self.clientAdd = self._socketObj.accept()
        print('connected with ' + str(self.clientAdd))
        
    def sendMsg(self, _msg):
        sendData = _msg
        self.clientSocket.send(sendData.encode('utf-8'))
        print('send msg :', sendData)
        
    def receiveMsg(self, _byte = 1024):
        receivedData = self.clientSocket.recv(_byte)
        print('recv msg :', receivedData.decode('utf-8'))

  
class clientSocket(baseSocket):        
    def connect(self):
        try:
            self._socketObj.connect((self._ip, self._port))
            print('connection established')     
            return True
        except:
            return False

    def sendMsg(self, msg):
        try:
            self._socketObj.send(msg.encode('utf-8'))
            print('send msg :', msg)
            return True
        except:
            print('fail to sending')
            return False

    def receiveMsg(self, byte = 1024):
        try:
            msg = self._socketObj.recv(byte)
            self._msg = msg.decode('utf-8')
            print('recv msg :', self._msg)
            return True
        except:
            print('receiving fail')
            return False


if __name__ == '__main__':
    server = serverSocket()
    server.bindAndListen()
    import pdb
    pdb.set_trace()