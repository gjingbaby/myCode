import abc
import numpy as np
from typing import Callable
from Msgalert import SMA,crossover,alert_message

class Strategy(metaclass = abc.ABCMeta):
    
    def __init__(self,broker,data):
        self._indicators = []
        self._broker = broker
        self._data = data
        self._tick = 0

    def I(self,func:Callable,*args) -> np.array:

        value = func(*args)
        value = np.asarray(value)
        alert_message(value.shape[-1] == len(self._data.Close),'指示器长度必须和data长度相同')
        self._indicators.append(value)
        return value

    @property
    def tick(self):
        return self._tick

    @abc.abstractmethod
    def __init(self):
        pass

    @abc.abstractmethod
    def next(self,tick):
        pass

    def buy(self):
        self._broker.buy()

    def sell(self):
        self._broker.sell()

    @property
    def data(self):
        return self._data

class Smacross(Strategy):
    fast = 10
    slow = 20
    def init(self):
        self.sma1 = self.I(SMA,self.data.Close,self.fast)
        self.sma2 = self.I(SMA,self.data.Close,self.slow)

    def next(self.tick):
        if crossover(self.sma1[:tick],self.sma2[:tick]):
            self.buy()
        elif crossover(self.sma2[:tick],self.sma1[:tick]):
            self.sell()
        else:   
            pass

class ExchangeAPI:
    def __init__(self,data,cash,commission):
        alert_message(0<cash,'初始现金大于0，输入现金数量：{}'.format(cash))
        alert_message(0 <= commission <= 0.05,'合理的手续费率一般不超过5%，输入的费率：{}'.format(commission))
        self._inital_cash = cash
        self._data = data
        self._commission = commission
        self._position = 0
        self._cash = cash
        self._i = 0
    
    @property
    def cash(self):
        return self._cash
    
    @property
    def position(self):
        return self._position

    @property
    def inital_cash(self):
        return self._inital_cash

    @property
    def market_value(self):
        return self._cash + self._position*self.current_price

    @property
    def current_price(self):
        return self._data.Close[self._i]

    def buy(self):
        self._position = float


