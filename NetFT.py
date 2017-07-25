import socket
import struct
import numpy as np
from threading import Thread
from time import sleep

class NetFT:
	def __init__(self, ip):
		self.ip = ip
		self.port = 49152
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.mean = {'fx': 0, 'fy': 0, 'fz': 0, 'tx': 0, 'ty': 0, 'tz': 0}

	def send(self, command, count = 0):
		header = 0x1234
		message = struct.pack('!HHI', header, command, count)
		self.sock.sendto(message, (self.ip, self.port))

	def recieve(self):
		rawdata = self.sock.recv(1024)
		data = struct.unpack('!IIIiiiiii', rawdata)
		self.data = {
			'fx': data[3] - self.mean['fx'],
			'fy': data[4] - self.mean['fy'],
			'fz': data[5] - self.mean['fz'],
			'tx': data[6] - self.mean['tx'],
			'ty': data[7] - self.mean['ty'],
			'tz': data[8] - self.mean['tz']}

	def tare(self, n = 10):
		self.mean = {'fx': 0, 'fy': 0, 'fz': 0, 'tx': 0, 'ty': 0, 'tz': 0}
		self.getMeasurements(n = n)
		mean = {'fx': 0, 'fy': 0, 'fz': 0, 'tx': 0, 'ty': 0, 'tz': 0}
		for i in range(n):
			self.recieve()
			for key in mean.keys():
				mean[key] += self.data[key] / float(n)
		self.mean = mean

	def recieveHandler(self):
		while True:
			self.recieve()
			if not self.async:
				break

	def getMeasurement(self):
		self.send(2, count = 1)
		self.recieve()
		return np.array([self.data['fx'], self.data['fy'], self.data['fz']]) / 1000000, \
			np.array([self.data['tx'], self.data['ty'], self.data['tz']]) / 1000000

	def getForce(self):
		self.send(2, count = 1)
		self.recieve()
		return np.array([self.data['fx'], self.data['fy'], self.data['fz']]) / 1000000

	def getTorque(self):
		self.send(2, count = 1)
		self.recieve()
		return np.array([self.data['tx'], self.data['ty'], self.data['tz']]) / 1000000

	def startStreaming(self, async = False):
		self.send(2, count = 0)
		if async:
			self.async = True
			self.thread = Thread(target = self.recieveHandler)
			self.thread.start()

	def getMeasurements(self, n):
		self.send(2, count = n)

	def stopStreaming(self):
		self.async = False
		sleep(0.1)
		self.send(0)
