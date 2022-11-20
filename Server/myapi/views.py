from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import calcVar
from .stockData import get_stock_data

# US_STOCK_LIST = ["TSM","GOOGL","TSLA","MSFT","AAPL"]
# number_of_share = [1, 2, 3, 4, 5]
# closing_price = [300,400,500,600,700]


def getRoutes(request):

    US_STOCK_LIST = ["TSM","GOOGL","TSLA","MSFT","AAPL"]
    number_of_share = [1, 2, 3, 4, 5]
    closing_price = [300,400,500,600,700]

    get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,100)

    portfolio_weights = calcVar.get_weight(number_of_share, closing_price)
    period = 501
    Time = 1

    InitialInvestment = calcVar.get_initial(number_of_share, closing_price)
    

    data = calcVar.portfolio(US_STOCK_LIST, portfolio_weights, period,Time ,InitialInvestment)

    print('\nportfolio weights: ', portfolio_weights, '\n')
    print('\nInitial investment: ', InitialInvestment, '\n')
    print('\n\n',data , '\n')

    return JsonResponse([('portfolio weights: ', portfolio_weights), ('Initial investment: ', InitialInvestment),data], safe=False)

def passing_data(request):
    data = (request.POST.items())

    stock_list = []
    number_of_share = []

    for key,value in data:
        # print(f'key = {key}')
        stock_list.append(key)
        # print(f'value = {value}')
        number_of_share.append(value)

    method = number_of_share[-1]
    stock_list = stock_list[:-1]
    number_of_share = number_of_share[:-1]



    df = get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(stock_list,1)  

    closing_price = (df.iloc[0].tolist())

    return stock_list ,number_of_share,closing_price,method


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

    if request.method == "POST":
        print("is post request")
        stock_list ,number_of_share,closing_price ,method= passing_data(request)
        # print(request.POST.get('somekey'))
        # data = (request.POST.items())
        print(method)
        print(stock_list)
        print(type(number_of_share[0]))
        print(type(closing_price[0]))

        get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(stock_list,100)

        portfolio_weights = calcVar.get_weight(number_of_share, closing_price)
        period = 501
        Time = 1
        InitialInvestment = calcVar.get_initial(number_of_share,closing_price)
        print(InitialInvestment)

        data = calcVar.portfolio(stock_list, portfolio_weights, period,Time ,InitialInvestment)

        print(data)

    return JsonResponse(data,safe=False)

# * Historical_Simulation
@csrf_exempt
def prediction(request):

    if request.method == "POST":
        print("is post request")
        stock_list ,number_of_share,closing_price,method= passing_data(request)
        # print(request.POST.get('somekey'))
        # data = (request.POST.items())

        # print(stock_list)
        # print(type(number_of_share[0]))
        # print(type(closing_price[0]))

        # get_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(stock_list,100)

        portfolio_weights = calcVar.get_weight(number_of_share, closing_price)
        period = 501
        Time = 1
        InitialInvestment = calcVar.get_initial(number_of_share,closing_price)
        # print(InitialInvestment)

        if method == "Historical_method":
            data = calcVar.portfolio(stock_list, portfolio_weights, period,Time ,InitialInvestment)
        
        elif method == "parametric_method":
            data = calcVar.single_stock_parametric_method(stock_list,period,Time,InitialInvestment)
            data['CVaR'] = None

        elif method == "Monte_Carlo_method":
            data = calcVar.portfolio_Monte_Carlo_Simulation(stock_list, portfolio_weights, period,InitialInvestment)
            data['Expected_return'] = None

        print(data)

    return JsonResponse(data,safe=False)