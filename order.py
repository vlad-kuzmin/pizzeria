from datetime import datetime
from pizza import AbstractPizza


class Order:
	def __init__(self, order_number):
		self.order_number = order_number
		self.food_dict = dict()
		self.time = None
		self.total_amount = 0
		self.status = None

	def add_food(self, food):
		if food not in self.food_dict:
			self.food_dict[food] = 1
		else:
			self.food_dict[food] += 1

	def calculate_total_amount(self):
		temp = 0
		for food, quantity in self.food_dict.items():
			temp += food.price * quantity
		self.total_amount = temp

		return self.total_amount

	def perform(self):
		if self.food_dict:
			self.time = datetime.now()
			return (
				"Ваш заказ передан на выполнение.\n",
				f"Номер вашего заказа : {self.order_number}"
					)
		else:
			return "Вы ничего не заказали, список заказов пуст."

	def refresh_status(self):
		if self.food_dict and self.time:
			is_complete = all([food.time(self.time) for food, _ in self.food_dict.items() if isinstance(food, AbstractPizza)])
			self.status = "готов" if is_complete else "выполняется"
			return is_complete
		else:
			return "Список заказов пуст или заказ еще не оплачен."

	def __str__(self):
		return f"Заказ {self.order_number}"
