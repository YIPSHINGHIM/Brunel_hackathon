from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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
    

    data = calcVar.portfolio(US_STOCK_LIST, portfolio_weights, period,Time ,InitialInvestment)

    print('\n\n',data , '\n')

    return JsonResponse(data,safe=False)

def passing_data(request):
    data = (request.POST.items())

    stock_list = []
    number_of_share = []

    for key,value in data:
        # print(f'key = {key}')
        stock_list.append(key)
        # print(f'value = {value}')
        number_of_share.append(value)

    df = get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(stock_list,1)  

    closing_price = (df.iloc[0].tolist())

    return stock_list ,number_of_share,closing_price


@csrf_exempt
def test_post_request(request):
    if request.method == "POST":
        print("is post request")
        stock_list ,number_of_share,closing_price = passing_data(request)
        # print(request.POST.get('somekey'))
        # data = (request.POST.items())

        print(stock_list)
        print(number_of_share)
        print(closing_price)


    return JsonResponse("asd",safe=False)



# * Historical_Simulation
@csrf_exempt
def Historical_Simulation_view(request):
    pass