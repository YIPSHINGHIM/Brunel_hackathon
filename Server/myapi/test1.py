import requests
url = 'http://127.0.0.1:8000/prediction'
obj = {'AAPL': '2',
        'TSLA':"3",
        'MSFT':"4",
        'GOOGL':"3",
        'method':"Historical_method"
}

x = requests.post(url,data=obj)
print(x.text)