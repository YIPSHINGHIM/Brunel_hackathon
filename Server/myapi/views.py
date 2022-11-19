from django.http import JsonResponse
from django.shortcuts import render

from .VaR.Stock_data import get_stock_data


def getRoutes(request):

    US_STOCK_LIST = ["TSM","GOOGL","TSLA","MSFT","AAPL"]
    
    print(get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,100))

    return JsonResponse("123",safe=False)

