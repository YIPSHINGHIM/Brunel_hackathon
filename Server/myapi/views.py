from django.http import JsonResponse
from django.shortcuts import render

84


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import calcVar
from .stockData import get_stock_data

US_STOCK_LIST = ["TSM","GOOGL","TSLA","MSFT","AAPL"]
number_of_share = [1, 2, 3, 4, 5]
closing_price = [300,400,500,600,700]


def getRoutes(request):

    get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,100)

    portfolio_weights = calcVar.get_weight(number_of_share, closing_price)
    period = 501
    Time = 1
    InitialInvestment = 10000
    
    print('\n\n', calcVar.portfolio(US_STOCK_LIST, portfolio_weights, period,Time ,InitialInvestment), '\n')
    # calcVar.single_stock_parametric_method()

    # print(f'\n\nnumber of share: {number_of_share}')
    # print(f'closing price: {closing_price}')
    # weight = calcVar.get_weight(number_of_share, closing_price)
    # print(f'weight: {weight}\n')

    # pfl = calcVar.portfolio(US_STOCK_LIST, weight, 501)

    # print(f'For portfolio : {US_STOCK_LIST}')
    # print('Expected Portfolio Return:      ', pfl[0])
    # print('Value at Risk 95th CI    :      ', pfl[1])
    # print('Conditional VaR 95th CI  :      ', pfl[2])

    # calcVar.portfolio(US_STOCK_LIST, weight, 501)
    # calcVar.portfolio_Monte_Carlo_Simulation(10000,US_STOCK_LIST,weight)

    return JsonResponse("123",safe=False)

@csrf_exempt
def test_post_request(request):
    if request.method == "POST":
        print("is post request")
        print(request.POST.get('somekey'))


    return JsonResponse("qweqweqwe",safe=False)

