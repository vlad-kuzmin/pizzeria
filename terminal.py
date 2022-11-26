from .pizza import PepperoniPizza, SeafoodPizza, BarbecuePizza
from .beverages import Cola, Sprite, Fanta
from .seller import Seller
from order import Order
from prettytable import PrettyTable


class Terminal:
	def __init__(self):
		self.menu = (
			"1 - Пицца 'Пепперони'",
			"2 - Пицца 'Дары Моря'",
			"3 - Пицца 'Барбекю'",
			"4 - Cola",
			"5 - Sprite",
			"6 - Fanta",
		)
		self.order = None
		self.order_number = 1
		self.completed_orders = list()
		self.active_orders = list()

	def print_menu(self) -> None:
		for food in self.menu:
			print(food, end="\n")

	def create_order(self) -> None:
		self.order = Order(self.order_number)
		self.order_number += 1

	def check_menu(self, food_number: int) -> None:
		if not self.order:
			self.create_order()
		match food_number:
			case "1":
				self.order.add_food(PepperoniPizza())
			case "2":
				self.order.add_food(SeafoodPizza())
			case "3":
				self.order.add_food(BarbecuePizza())
			case "4":
				self.order.add_food(Cola())
			case "5":
				self.order.add_food(Sprite())
			case "6":
				self.order.add_food(Sprite())
			case _:
				print("Непредвиденная ошибка, повторите еще раз.")

	def print_check(self, total_amount, amount_of_payment):
		check = PrettyTable()
		check.field_names = ["Товар", "Количество", "Стоимость", "Внесено", "Сдача"]
		for food, quantity in self.order.food_dict.items():
			check.add_row([str(food), quantity, food.price, "", ""])
		else:
			check.add_row(["", "", "", amount_of_payment, total_amount - amount_of_payment])

		print(check)

	def accept_payment(self, amount_of_payment):
		total_amount = self.order.calculate_total_amount()
		if amount_of_payment == total_amount:
			self.order.status = "выполняется"
			self.active_orders.append(self.order)
			print("Оплата прошла успешно! Заказ передан в исполнение :)")
			self.print_check(total_amount, amount_of_payment)
			self.order = None

		elif amount_of_payment < total_amount:
			print(
				"Не достаточно денег для оплаты!"
				f"Внесено: {amount_of_payment}; Сумма заказа: {total_amount}"
			)
		elif amount_of_payment > total_amount:
			self.order.status = "выполняется"
			self.active_orders.append(self.order)
			print(
				"Оплата прошла успешно! Заказ передан в исполнение :)"
				f"Ваша сдача: {total_amount - amount_of_payment} р"
			)
			self.print_check(total_amount, amount_of_payment)
			self.order = None

		else:
			print("Непредвиденная ошибка, повторите попытку еще раз...")

	def check_order_status(self, order_number):
		for order in self.active_orders:
			if order.order_number == order_number:
				print(f"Статус заказа #{order_number}: {order.status}")
			else:
				print(f"Заказа #{order_number} не найден...")

	def change_order_status(self, order_number):
		for order in self.active_orders:
			if order.order_number == order_number:
				order.status = "готов"
				print(f"Статус заказа #{order_number} изменён с 'выполняется' на 'готов'")
			else:
				print(f"Заказа #{order_number} не найден...")








terminal = Terminal()
terminal.print_menu()
