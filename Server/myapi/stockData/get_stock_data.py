import datetime as dt

import numpy as np
import pandas as pd
import yfinance as yf


def list_to_string_with_space(list):
    """
    transfer a list to a string with space
    """
    
    my_str = ' '.join(list)
    return(my_str)


def Get_the_time_frame(how_many_day:int):
    """
    getting the date from today to the day given 
    """
    # getting stock data 
    today = dt.date.today()
    
    historical_data_time_frame = today - dt.timedelta(days=how_many_day)
    # print(today)
    return historical_data_time_frame

One_hundred_day_before = Get_the_time_frame(100)


def create_stock_object(stock_list:list[str]):
    stock_list_str = list_to_string_with_space(stock_list)
    tickers = yf.Tickers(stock_list_str)

    return tickers


def Get_the_single_stock_historical_data_in_the_given_time(stock_ticket:str ,period:int):
    """
    Get the single stock historical data in the given time 
    """

    Stock_ticket = create_stock_object([stock_ticket])
    closing_price_df = Stock_ticket.tickers[stock_ticket].history(period = f'{period}d')[["Close"]]
    
    return (closing_price_df)



TSLA_100day_data =  Get_the_single_stock_historical_data_in_the_given_time("TSLA",732)



def Get_the_stock_portfolio_historical_data_in_the_given_time(stock_list:list[str],period:int):

    portfolio_stock_ticket = create_stock_object(stock_list)
    
    single_closing_price_df = portfolio_stock_ticket.tickers[str(stock_list[0])].history(period=f'{period}d')['Close']

    # print(single_closing_price_df)

    portfolio_closing_price_df = pd.DataFrame
    for ticket_symbol in stock_list:

        single_closing_price_df = portfolio_stock_ticket.tickers[ticket_symbol].history(period=f'{period}d')[['Close']]


        if ticket_symbol == stock_list[0]:
            # print('1st')
            portfolio_closing_price_df = single_closing_price_df.copy()
            portfolio_closing_price_df = portfolio_closing_price_df.rename({'Close' : ticket_symbol},axis='columns')

        else:
            # print(ticket_symbol)
            portfolio_closing_price_df = pd.concat([portfolio_closing_price_df,single_closing_price_df],axis=1)
            portfolio_closing_price_df = portfolio_closing_price_df.rename({'Close' : ticket_symbol},axis='columns')


    # print(portfolio_closing_price_df)


    return portfolio_closing_price_df

US_STOCK_LIST = ["TSM","GOOGL","TSLA","MSFT","AAPL"]
    
Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,100)








    
