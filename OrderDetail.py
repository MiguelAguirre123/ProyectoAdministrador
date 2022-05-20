from datetime import date
from numpy import double

class OrderDetail:

    __OrderId:str
    __ProductId:str
    __ProductName:str
    __quantify:int
    __UnitCost:double
    __Total:double

    def CalculateTotal(self):
        pass