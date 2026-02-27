import pandas as pd
import MetaTrader5 as mt5

if not mt5.initialize():
    print("初始化失敗")
    mt5.shutdown()
    quit()
print("Mt5初始化成功")
account_money = mt5.account_info().balance
history = mt5.copy_rates_from_pos("USDJPY",mt5.TIMEFRAME_H1,0,1000)
df = pd.DataFrame(history)