import rolspy
from msg import Int32, String

# rolspy.init_node("topic_publisher")
pub = rolspy.Publisher('counter',String)
rate = rolspy.Rate(2)
count = 0
while not rolspy.is_shotdown():
    pub.publish(str(count))
    count += 1
    rate.sleep()

# 监听 python pub_sub_tool.py topic_sub --port=2000 --topic=counter