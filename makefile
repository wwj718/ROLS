echo :
	echo "hello"

grep :
	ps aux |grep Python

test-pub :
	python pub_sub_tool.py topic_pub
test-sub :
	python pub_sub_tool.py topic_sub
test-js-sub:
	node subber.js