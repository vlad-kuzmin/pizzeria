class AbstractBeverage:
	def __init__(self):
		self.price = 0
		self.title = None

	def __str__(self):

		return self.title


class Cola(AbstractBeverage):
	def __init__(self):
		super().__init__()
		self.price = 50
		self.title = "Cola"


class Sprite(AbstractBeverage):
	def __init__(self):
		super().__init__()
		self.price = 60
		self.title = "Sprite"


class Fanta(AbstractBeverage):
	def __init__(self):
		super().__init__()
		self.price = 80
		self.title = "Fanta"
