from OrderDetail import OrderDetail
from datetime import date

class Order:

    __Date:date
    __CustomerName:str
    __CostumerId:str
    __OrderDetails:OrderDetail

    def __init__(self, orderdetail:OrderDetail):

        self.__OrderDetails = orderdetail

    def PlaceOrder(self):
        pass