import requests

try:
    s=input("Stock Symbol: ").upper()
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{s}"
    d=requests.get(u).json()
    p=d["chart"]["result"][0]["meta"]["regularMarketPrice"]
    print("Current Price:",p)
except Exception as e:
    print("Error:",e)
