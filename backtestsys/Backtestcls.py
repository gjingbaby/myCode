
from Msgalert import alert_message
import pandas as pd
import numpy as np
from Strategycls import Strategy

class backtest():
    
    def __init__(self,
        data:pd.DataFrame,
        strategy_type:type(Strategy),
        broker_type:type(ExchangeAPI),
        cash:float = 10000,commission: 
        float = .0):
        
        alert_message(issubclass(strategy_type,Strategy),'strategy_type不是Strategy类型')
        alert_message(issubclass(broker_type,ExchangeAPI),'broker_type不是ExchangeAPI类型')
        alert_message(issubclass(commission,Number),'commission不是float类型')

        data = data.copy(False)

        if 'Volumn' not in data:
            data['Volumn'] = np.nan

        alert_message(len(data.columns & {'Open','High','Low','Close','Volumn'}) == 5,
                    ('输入的data格式不正确，至少需要包含列OHLCV'))
        alert_message(not data[['Open','High','Low','Close','Volumn']].max().isnull().any(),'部分OHLC包含缺失值，请处理')

        if not data.index.is_monotonic_increasing:
            data = data.sort_index()
        
        self._data = data
        self._broker = broker_type(data,cash,commission)
        self._strategy = strategy_type(self._broker,self._data)
        self._results = None 
    

    def run(self):
        strategy = self._strategy
        broker = self._broker

        strategy.init()

        start = 100
        end = len(self._data)

        for i in range(start,end):
            broker.next(i)
            strategy.next(i)

        self._results = self._compute_result(broker)
        return self._results

    def _compute_result(self,broker):
        s = pd.Series()
        s['初始市值'] = broker.initial_cash
        s['结束市值'] = broker.market_value
        s['收益'] = broker.market_value - broker.initial_cash
        return s






