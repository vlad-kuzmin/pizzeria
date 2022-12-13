from pizza import PepperoniPizza, SeafoodPizza, BarbecuePizza
from beverages import Cola, Sprite, Fanta
from seller import Seller
from order import Order
from prettytable import PrettyTable


class Terminal:
	def __init__(self):
		self.order = None
		self.order_number = 1
		self.completed_orders = list()
		self.active_orders = list()
		self.opened = False

	@staticmethod
	def print_menu() -> None:
		menu = PrettyTable()
		foods = [
			PepperoniPizza(),
			SeafoodPizza(),
			BarbecuePizza(),
			Cola(),
			Sprite(),
			Fanta(),
		]
		menu.title = "МЕНЮ"
		menu.field_names = ["Номер", "Наименование", "Стоимость"]
		for food_index in range(len(foods)):
			menu.add_row([food_index + 1, foods[food_index].title, foods[food_index].price])

		print(menu)

	def create_order(self) -> None:
		self.order = Order(self.order_number)
		self.order_number += 1

	def check_menu(self, food_number) -> None:
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
				self.order.add_food(Fanta())
			case _:
				print("Непредвиденная ошибка, повторите еще раз.")

	def bill(self):
		bill = PrettyTable()
		bill.title = "СЧЁТ"
		bill.field_names = ["Товар", "Количество", "Стоимость", "Итого"]
		total_amount = self.order.calculate_total_amount()
		for food, quantity in self.order.food_dict.items():
			bill.add_row([str(food), quantity, food.price, " - "])
		else:
			bill.add_row([" - ", " - ", " - ", total_amount])

		print(bill)

	def print_check(self, amount_of_payment):
		check = PrettyTable()
		check.title = f"ЧЕК  ЗАКАЗ #{self.order.order_number}"
		check.field_names = ["Товар", "Количество", "Стоимость", "Итого", "Внесено", "Сдача"]
		total_amount = self.order.calculate_total_amount()
		for food, quantity in self.order.food_dict.items():
			check.add_row([str(food), quantity, food.price, " - ", " - ", "-"])
		else:
			check.add_row([" - ", " - ", " - ", total_amount, amount_of_payment, amount_of_payment - total_amount])

		print(check)

	def accept_payment(self, amount_of_payment):
		total_amount = self.order.calculate_total_amount()
		if amount_of_payment == total_amount:
			self.order.status = "выполняется"
			self.active_orders.append(self.order)
			print("Оплата прошла успешно!")
			self.order.perform()
			self.print_check(amount_of_payment)
			self.order = None

		elif amount_of_payment < total_amount:
			print(
				"Не достаточно денег для оплаты!\n"
				f"Внесено: {amount_of_payment}; Сумма заказа: {total_amount}"
			)
		elif amount_of_payment > total_amount:
			self.order.status = "выполняется"
			self.active_orders.append(self.order)
			print(
				"Оплата прошла успешно !\n"
				f"Ваша сдача: {amount_of_payment - total_amount} р"
			)
			self.order.perform()
			self.print_check(amount_of_payment)
			self.order = None

		else:
			print("Непредвиденная ошибка, повторите попытку еще раз...")

	def check_order_status(self, order_number):
		for order_a in self.active_orders:
			if order_a.order_number == order_number:
				order_a.refresh_status()
				print(f"Статус заказа #{order_number}: {order_a.status}")
			else:
				for order_c in self.completed_orders:
					if order_c.order_number == order_number:
						order_c.refresh_status()
						print(f"Статус заказа #{order_number}: {order_c.status}")
					else:
						print(f"Заказ #{order_number} не найден...")

	def refresh_orders(self):
		if self.active_orders:
			for order in self.active_orders:
				if order.status == "готов":
					self.completed_orders.append(order)
					self.active_orders.remove(order)

	def get_total_check(self, seller):
		total_check = PrettyTable()
		total_check.title = f"ОБЩИЙ ЧЕК ЗА {seller.time_open.strftime('%m/%d/%Y')} "
		total_check.field_names = ["Заказ", "Сумма", "Итого", "Продавец", "Дата и время открытия и закрытия"]
		total_price_counter = 0
		for order in self.completed_orders:
			total_price_counter += order.total_amount
			total_check.add_row([str(order), order.total_amount, " - ", " - ", " - "])
		else:
			total_check.add_row([
					" - ", " - ",
					total_price_counter,
					seller.full_name,
					f"{seller.time_open.strftime('%m/%d/%Y | %H:%M')} - {seller.time_close.strftime('%m/%d/%Y | %H:%M')}"
				])

		print(total_check)


if __name__ == "__main__":
	print(
		"Кассы закрыты, терминал не работает.\n"
		"Для открытия кассы необходимо зарегистрировать продавца.\n"
	)
	# Регистрация продавца
	seller = Seller()
	registered = False
	while not registered:
		full_name = input("Введите ФИО: ")
		password_1 = input("Введите пароль: ")
		password_2 = input("Повторите пароль: ")
		if password_1 == password_2:
			seller.registrate(full_name, password_1)
			registered = True

	# Открытие кассы и терминала
	terminal = Terminal()
	seller.open(terminal) if input("Открыть кассу? (Y/n): ") in "Yy" else False

	# Вывод меню и обработка заказов
	while terminal.opened:
		console = None
		print(
			"Для подтверждения заказа введите 'confirm'.\n"
			"Для отмены - 'cancel'.\n"
		)
		terminal.print_menu()
		while console not in ("confirm", "cancel"):
			console = input("Введите номер пункта меню для добавления в заказ: ")
			if console == "cancel":
				terminal.order = None
				terminal.order_number -= 1
			elif console == "confirm":
				terminal.bill()
				terminal.accept_payment(int(input("Внесите деньги для оплаты заказа: ")))
				terminal.refresh_orders()
			else:
				terminal.check_menu(console)
				terminal.refresh_orders()

		# Проверка статуса заказа
		print("Хотите узнать статус заказ?")
		console = input("Введите (Y/n): ")
		if console in "Yy":
			console = None
			while console != "exit":
				console = input("Введите номер заказа (выход: exit): ")
				if console.isnumeric():
					terminal.refresh_orders()
					terminal.check_order_status(int(console))
		else:
			console = None
		# Закрытие кассы
		print("Закрыть кассу?")
		console = input("Введите (Y/n): ")
		if console in "Yy":
			authorized = False
			terminal.refresh_orders()
			if not terminal.active_orders:
				while not authorized:
					password = input("Введите пароль: ")
					if password == seller.password:
						authorized = True
						seller.close(terminal)
						terminal.get_total_check(seller)
			else:
				print("Мы не можем закрыться пока не выполним все заказы.")
		else:
			console = None

