from abc import *
import socket
import time


class baseSocket(metaclass=ABCMeta):
    def __init__(self, _ip = 'localhost', _port=8089):
        self.ip = _ip
        self.port = _port
        self.socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def disconnect(self):
        self.socketObj.close()
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
        self.socketObj.bind((self.ip, self.port))
        print('server established') 
    
    def listen(self):
        self.socketObj.listen(1)
        print('connection waiting') 
        self.clientSocket, self.clientAdd = self.socketObj.accept()
        print('connected with ' + str(self.clientAdd))
        
    def sendMsg(self, _msg):
        sendData = _msg
        self.clientSocket.send(sendData.encode('utf-8'))
        print('send msg :', sendData)
        
    def receiveMsg(self, _byte = 1024):
        recvData = self.clientSocket.recv(_byte)
        print('recv msg :', recvData.decode('utf-8'))        

  
class clientSocket(baseSocket):        
    def connect(self):
        self.socketObj.connect((self.ip, self.port))
        print('connection established')     
    
    def sendMsg(self, _msg):
        sendData = _msg
        self.socketObj.send(sendData.encode('utf-8'))
        print('send msg :', sendData)
        
    def receiveMsg(self, _byte = 1024):
        recvData = self.socketObj.recv(_byte)
        print('recv msg :', recvData.decode('utf-8'))


if __name__ == '__main__':
    client = clientSocket()
    client.connect()
    client.sendMsg('I am python')
    client.receiveMsg()
    client.disconnect()

    