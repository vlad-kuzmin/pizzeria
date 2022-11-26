from datetime import datetime


class Pizza:
	def __init__(self):
		self.price = 25

	def __str__(self):
		return "Pizza"


class Order:
	def __init__(self, order_number: int):
		self.order_number = order_number
		self.food_dict = dict()
		self.time = datetime.now()
		self.total_amount = 0
		self.status = None

	def add_food(self, food):
		if food not in self.food_dict:
			self.food_dict[food] = 1
		else:
			self.food_dict[food] += 1

		print(self.food_dict)

	def calculate_total_amount(self):
		for food, quantity in self.food_dict.items():
			self.total_amount += food.price * quantity
			print(food, quantity)

		return self.total_amount


pizza = Pizza()
order = Order(1)
order.add_food(pizza)
order.add_food(pizza)
print(order.calculate_total_amount())
