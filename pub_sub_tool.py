import zmq
import fire
import time
from zmq.utils.strtypes import asbytes

context = zmq.Context()

# bytes问题: https://codinglonglong.github.io/posts/zeromqde-san-chong-ji-ben-tong-xin-mo-xing/

class Helper:
    '''
    usage:
        pub:
            python pub_and_sub_tool.py topic_pub
            python pub_and_sub_tool.py topic_pub --port=1234
            python pub_and_sub_tool.py topic_pub --data=hahaha
            python pub_and_sub_tool.py topic_pub --topic=newtopic

        sub:
            python pub_and_sub_tool.py topic_sub 
    '''
    def topic_pub(self, port=5556, topic="test", data="test data"):
        '''
        usage:
            python pub_and_sub_tool.py topic_pub --data=hahah
        '''
        pub = context.socket(zmq.PUB)
        pub.bind(f"tcp://127.0.0.1:{port}")
        time.sleep(0.5)
        # import IPython;IPython.embed()
        pub.send_multipart([asbytes(topic),asbytes(data)])
        print("topic: {} ; msg: {}".format(topic,data))

    def topic_sub(self,port=5556):
        '''
            python pub_and_sub_tool.py topic_sub 
        '''
        sub = context.socket(zmq.SUB)
        sub.connect(f"tcp://127.0.0.1:{port}")
        topics = ["test"]
        if not topics:
            print("Receiving messages on ALL topics...")
            sub.setsockopt_string(zmq.SUBSCRIBE,'')
            # sub.setsockopt(zmq.SUBSCRIBE,b'')
        else:
            print("Receiving messages on topics: %s ..." % topics)
            for t in topics:
                sub.setsockopt_string(zmq.SUBSCRIBE,t)
                # sub.setsockopt(zmq.SUBSCRIBE,t)
        try:
            while True:
                topic, msg = sub.recv_multipart()
                print('Topic: %s, msg:%s' % (topic, msg))
        except KeyboardInterrupt:
            pass
        print("Done.")    

if __name__ == '__main__':
  fire.Fire(Helper)
