from datetime import datetime


class Seller:
	def __init__(self):
		self.full_name = None
		self.password = None
		self.time_open = None
		self.time_close = None

	def registrate(self, full_name, password):
		self.full_name = full_name
		self.password = password
		return f"Продавец: {full_name} зарегистрирован."

	def open(self, terminal):
		self.time_open = datetime.now()
		terminal.opened = True
		print("Кассы открыты, терминал работает.")

	def close(self, terminal):
		self.time_close = datetime.now()
		terminal.opened = False
		print("Кассы закрыты, терминал не работает.")

	def __str__(self):
		info = f"Продавец: {self.full_name}"
		return info







