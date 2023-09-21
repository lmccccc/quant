from pytdx.hq import TdxHq_API
import pymysql as sql
import matplotlib.pyplot as plt
import pandas as pd

def test1():
    api = TdxHq_API()
    if api.connect('119.147.212.81', 7709):
        # ... same codes...
        # data = api.get_security_bars(9, 0, '000001', 0, 10)  # 返回普通list
        # (类别，市场代码，股票代码str，起始偏移量0为最新，获取数量)
        data = api.get_security_bars(9, 0, '000001', 0, 800)  # 返回DataFrame
        data2 = api.get_security_bars(9, 0, '000001', 800, 800)  # 返回DataFrame
        data = data2 + data
        data = api.to_df(data)
        # data = api.to_df(api.get_security_bars(9, 0, '000001', 0, '20200901', '20200930'))  # 返回DataFrame
        close = pd.to_numeric(data["close"])
        date = data["datetime"].to_list()
        print(len(close))
        plt.plot(range(len(close)), close)
        print('start date ', date[0], ' last date ', date[-1])
        plt.show()

        api.disconnect()
        return data
    return None

def mysqltest():
    conn = sql.connect(host='localhost', port=3306, database='quant', user='root', password='lmc123456', charset='utf8')
    cs1 = conn.cursor()


if __name__ == '__main__':
    test1()
    mysqltest()

