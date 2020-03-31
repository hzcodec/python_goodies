import time
import threading

class HeartBeatProducer:
	def __init__(self, network):
		self.network = network
		self.id = None
		self.period = None
		self.transmit_thread = None
		self.stop_event = threading.Event()
		print(self.stop_event)

	def transmit(self):
		print('Send - id={}'.format(self.id))

	def start(self, id ,period):
		self.id = id
		self.period = period
		print('OK')

		if not self.transmit_thread or not self.transmit_thread.is_alive():
			self.stop_event.clear()
			self.transmit_thread = threading.Thread(target=self._periodic_transmit)
			self.transmit_thread.deamon = True
			self.transmit_thread.start()

	def stop(self):
		self.stop_event.set()
		self.transmit_thread = None
		print('Stopped')

	def _periodic_transmit(self):
		while not self.stop_event.is_set():
			start = time.time()
			self.transmit()
			time_left = self.period - (time.time() - start)
			self.stop_event.wait(max(time_left, 0.0))


def main():
	hp = HeartBeatProducer(1)
	hp.start(2, 0.5)

	c = 0
	
	while(True):
		time.sleep(2)
		print('---')
		c = c + 1
		if (c == 4):
			hp.stop()

if __name__ == "__main__":
	main()


