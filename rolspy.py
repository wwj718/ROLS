import time
import zmq
from zmq.asyncio import Context
from zmq.utils.strtypes import asbytes



'''
使用协程
'''

class BaseMessage:
    def __init__(self):
        context = Context()
        self.pub = context.socket(zmq.PUB)
        self.sub = context.socket(zmq.SUB)
        self.pub.bind('tcp://127.0.0.1:2000')
        self.sub.connect('tcp://127.0.0.1:2000')
        time.sleep(0.5) # 确保连接完成

class Publisher(BaseMessage):
    def __init__(self,topic,msg_type):
        super().__init__() # 得到self.pub, self.sub
        self.topic = topic
        self.msg_type = msg_type
    def __repr__(self):
        return f'name:{self.name} ;msg_type:{self.msg_type}'

    def publish(self,message):
        self.pub.send_multipart([asbytes(self.topic),asbytes(message)])

class Rate:
    def __init__(self,rate):
        self.rate = rate
    def sleep(self):
        time.sleep(1 / self.rate) # 这样并不精确，翻ROS源码


def is_shotdown():
    return False


