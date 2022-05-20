from Order import Order
from User import User
from numpy import double

class Customer(User):

    __Address:str
    __AcountBalance:double
    __Order:Order

    def __init__(self, order:Order):

        self.__Order = order

    def Register(self):
        pass

    def Purchase(self):
        pass