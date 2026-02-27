import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

if not mt5.initialize():
    print("初始化失敗")
    print(mt5.last_error())  
    mt5.shutdown()
    quit()

print("初始化成功")


