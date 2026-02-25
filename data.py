import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

if not mt5.initialize():
    print("初始化失敗")
    mt5.shutdown()
    quit()

