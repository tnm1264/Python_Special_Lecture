#Server 20103323 Kim tae wook
from socketserver import ThreadingTCPServer, StreamRequestHandler
PORT = 2000

class MyRequestHandler(StreamRequestHandler):
	def handle(self):
		conn = self.request
		print('connection from', self.client_address)
		while True:
			self.data = self.rfile.readline().strip()
			if self.data and self.data is not 'quit':
				output = str(self.data) #Convert Byte to String
				print (output[2:-1])
			else:
				print('Connection terminated')
				self.request.close()
				break;

server = ThreadingTCPServer(('127.0.0.1',2000), MyRequestHandler)
print('listening on port',PORT)
server.serve_forever()
