from django.http import JsonResponse
from django.shortcuts import render

from .stockData import get_stock_data
from . import calcVar
from . import tests

def getRoutes(request):

    US_STOCK_LIST = ["TSM","GOOGL","TSLA","MSFT","AAPL"]
    number_of_share = [1, 2, 3, 4, 5]
    closing_price = [300,400,500,600,700]

    get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,100)
    calcVar.single_stock_parametric_method()

    print(f'\n\nnumber of share: {number_of_share}')
    print(f'closing price: {closing_price}')
    weight = tests.get_weight(number_of_share, closing_price)
    print(f'weight: {weight}\n')

    calcVar.portfolio(US_STOCK_LIST, weight, 501)
    
    return JsonResponse("123",safe=False)

