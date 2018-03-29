// subber.js
// node subber.js
var zmq = require('zeromq')
  , sock = zmq.socket('sub');

sock.connect('tcp://127.0.0.1:5556');
sock.subscribe('test');
console.log('Subscriber connected to port 5556');

sock.on('message', function(topic, message) {
  // 解码 Convert Buffer to Utf-8 String: bufferOriginal.toString('utf8')
  console.log('received a message related to:', topic.toString('utf8'), 'containing message:', message.toString('utf8'));
});