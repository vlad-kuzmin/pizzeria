import time
from datetime import datetime, timedelta


class AbstractPizza:
    """Базовый класс пиццы от которого наследуются все остальные"""

    def __init__(self):
        """
        Этот метод срабатывает тогда когда, создается экземпляр класса, он объявляет
        переменные которые относятся к классу, далее доступ к ним осуществляется через .self
        """

        self.title = ''
        self.dough = ''
        self.sauce = ''
        self.filing = ''
        self.price = 0
        self.cooking_time = 0

    def time(self, start_time):
        now = datetime.now()
        delta = now - start_time
        if delta.seconds / 60 > self.cooking_time:
            return True
        else:
            return False

    def __str__(self):
        """Метод представления экземпляра класса в строковом типе данных."""
        # объявляем его в родительском классе далее переиспользуем в дочерних.

        return self.title


class PepperoniPizza(AbstractPizza):

    def __init__(self):
        super().__init__()  # тут мы вызываем родительский метод __init__ что бы
        # в дочерний класс передались переменные и методы родительского
        # super() - это обращение к классу от которого наследуемся
        self.title = 'Пепперони'
        self.dough = 'Дрожжевое'
        self.sauce = 'Томатный'
        self.filing = 'Помидоры, оливки, колбаса, перец'
        self.price = 400
        self.cooking_time = 1


class BarbecuePizza(AbstractPizza):

    def __init__(self):
        super().__init__()  # опять достаем все из класса от которого наследуемся
        self.title = 'Барбекю'
        self.dough = 'Дрожжевое'
        self.sauce = 'Барбекю '
        self.filing = 'Помидоры, оливки, куриная грудка'
        self.price = 450
        self.cooking_time = 2


class SeafoodPizza(AbstractPizza):

    def __init__(self):
        super().__init__()  # опять достаем все из класса от которого наследуемся
        self.title = 'Дары моря'
        self.dough = 'Слоёное'
        self.sauce = 'Майонез'
        self.filing = 'Помидоры, осьминог, креветки, мидии'
        self.price = 450
        self.cooking_time = 25

