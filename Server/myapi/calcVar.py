import datetime as dt
import math

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm, t

from .stockData import get_stock_data


class data_initialise:

    def __init__(self, Stock_historical_data_df,portfolio_weights=np.array([1])):
        self.Stock_historical_data_df = Stock_historical_data_df
        self.portfolio_weights = portfolio_weights

    def portfolioPerformance(self,weights, meanReturns, covMatrix, Time):
        returns = np.sum(meanReturns*weights)*Time
        std = np.sqrt( np.dot(weights.T, np.dot(covMatrix, weights)) ) * np.sqrt(Time)
        return returns, std


    def Calculating_daily_portfolio_Returns(self):

        portfolio_closing_price_df = self.Stock_historical_data_df.copy()
        # print(portfolio_closing_price_df.columns)

        for ticket_symbol in portfolio_closing_price_df.columns:
            portfolio_closing_price_df[str(ticket_symbol)] = portfolio_closing_price_df[str(ticket_symbol)].pct_change()
            
        portfolio_closing_price_df = portfolio_closing_price_df.dropna()

        return (portfolio_closing_price_df)



    def add_Portfolio_columns_to_df(self,Stock_historical_data_df_with_returns:pd.DataFrame):

        temp_df = Stock_historical_data_df_with_returns.copy()

        portfolio_weights = self.portfolio_weights

        # print(portfolio_weights)

        if len(portfolio_weights) == 1:
            # print("only one stock")
            temp_df.rename({f'{temp_df.columns[0]}' : 'Portfolio'},axis=1, inplace=True)

        else:
            temp_df['Portfolio'] = temp_df.dot(portfolio_weights)

        # print(temp_df.head())
        return temp_df

class Historical_Simulation(data_initialise):

    def Calculating_VaR_by_Historical_Simulation(self,Stock_historical_data_df_with_returns:pd.DataFrame,confidence_level:int):
        """
        Read in a pandas dataframe of returns / a pandas series of returns 
        Output the percentile of the distribution at the given alpha confidence level
        """
        
        if isinstance(Stock_historical_data_df_with_returns,pd.Series):
            return np.percentile(Stock_historical_data_df_with_returns ,confidence_level)

        elif isinstance(Stock_historical_data_df_with_returns,pd.DataFrame):
            return Stock_historical_data_df_with_returns.aggregate(self.Calculating_VaR_by_Historical_Simulation,axis=0,confidence_level = confidence_level)

        else:
            raise TypeError("Expected returns to be dataframe ot series")


    def Calculating_CVaR_by_Historical_Simulation(self,Stock_historical_data_df_with_returns:pd.DataFrame,confidence_level:int):
        """
        Read in a pandas dataframe of returns / a pandas series of returns 
        Output the CVaR for dataframe and series
        """
        
        if isinstance(Stock_historical_data_df_with_returns,pd.Series):
            belowVaR = Stock_historical_data_df_with_returns <= self.Calculating_VaR_by_Historical_Simulation(Stock_historical_data_df_with_returns,confidence_level)

            return Stock_historical_data_df_with_returns[belowVaR].mean()

        elif isinstance(Stock_historical_data_df_with_returns,pd.DataFrame):
            return Stock_historical_data_df_with_returns.aggregate(self.Calculating_CVaR_by_Historical_Simulation,axis=0,confidence_level = confidence_level)

        else:
            raise TypeError("Expected returns to be dataframe ot series")

class parametric_method(data_initialise):
    
    def Calculating_VaR_by_parametric_method(self,Stock_historical_data_df_with_returns,confidence_level):
        Stock_historical_data_df_with_returns = Stock_historical_data_df_with_returns.copy()

        print(Stock_historical_data_df_with_returns)
        # Estimate the average daily return
        mu = np.mean(Stock_historical_data_df_with_returns['Portfolio'])
        # print(mu)
        
        # # Estimate the daily volatility => also = Standard Deviation
        vol = np.std(Stock_historical_data_df_with_returns['Portfolio'])
        # print(vol)

        VaR = norm.ppf(confidence_level/100 , mu,vol)
        # print(VaR)

        return VaR


class Monte_Carlo_Simulation_method(data_initialise):

    def Monte_Carlo_Simulation(self,Stock_historical_data_df_with_returns):


        Stock_historical_data_df_with_returns = Stock_historical_data_df_with_returns.copy()
        InitialInvestment = 10000
        weights = self.portfolio_weights

        # number of simulation
        mc_sims = 1000
        # timeframes in days
        T = 1
        InitialInvestment = 10000

        # print(Stock_historical_data_df_with_returns)

        mean_portfolio_historical_return_df = Stock_historical_data_df_with_returns.mean()

        # print(mean_portfolio_historical_return_df)

        covMatrix_portfolio_historical_return_df = Stock_historical_data_df_with_returns.cov()
        # print(covMatrix_portfolio_historical_return_df)

        MeanM = np.full(shape=(T,len(weights)) ,fill_value=mean_portfolio_historical_return_df)

        MeanM = MeanM.T

        portfolio_sims = np.full(shape=(T,mc_sims) , fill_value=0.0)
        # print(np.random.normal(size=(T,len(weights))))
        
        # Monte Carlo loop
        for m in range(0,mc_sims):
            Z = np.random.normal(size=(T,len(weights)))
            L = np.linalg.cholesky(covMatrix_portfolio_historical_return_df)

            daily_returns = MeanM + np.inner(L,Z)
            portfolio_sims[:,m] = np.cumprod(np.inner(weights,daily_returns.T) + 1 )*InitialInvestment  


        # plt.plot(portfolio_sims)
        # plt.show()

        return pd.Series(portfolio_sims[-1,:])


        
    def Calculating_VaR_by_Monte_Carlo_Simulation(self,Stock_historical_data_df_with_returns:pd.DataFrame,confidence_level:int):
        """
        Read in a pandas dataframe of returns / a pandas series of returns 
        Output the CVaR for dataframe and series
        """
        
        if isinstance(Stock_historical_data_df_with_returns,pd.Series):
            return np.percentile(Stock_historical_data_df_with_returns ,confidence_level)

        elif isinstance(Stock_historical_data_df_with_returns,pd.DataFrame):
            return Stock_historical_data_df_with_returns.aggregate(self.Calculating_VaR_by_Historical_Simulation,axis=0,confidence_level = confidence_level)

        else:
            raise TypeError("Expected returns to be dataframe ot series")


    def Calculating_CVaR_by_Monte_Carlo_Simulation(self,Stock_historical_data_df_with_returns:pd.DataFrame,confidence_level:int):
        """
        Read in a pandas dataframe of returns / a pandas series of returns 
        Output the CVaR for dataframe and series
        """
        
        if isinstance(Stock_historical_data_df_with_returns,pd.Series):
            belowVaR = Stock_historical_data_df_with_returns <= self.Calculating_VaR_by_Monte_Carlo_Simulation(Stock_historical_data_df_with_returns,confidence_level)

            return Stock_historical_data_df_with_returns[belowVaR].mean()

        elif isinstance(Stock_historical_data_df_with_returns,pd.DataFrame):
            return Stock_historical_data_df_with_returns.aggregate(self.Calculating_VaR_by_Monte_Carlo_Simulation,axis=0,confidence_level = confidence_level)

        else:
            raise TypeError("Expected returns to be dataframe ot series")




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from .stockData import get_stock_data as Get_the_stock_data

period = 501

# * weight of the portfolio 
# portfolio_weights = np.random.random(len(portfolio_historical_return_df.columns))
# Normalizing it 
# portfolio_weights /= np.sum(portfolio_weights)

# print(portfolio_historical_return_df.head())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def portfolio_Monte_Carlo_Simulation(InitialInvestment,US_STOCK_LIST, portfolio_weights):

    # InitialInvestment = 10000
    # * Testing for portfolio

    # US_STOCK_LIST = ["TSM","GOOGL","TSLA","MSFT","AAPL"]
    # portfolio_weights = np.array([0.2,0.15,0.15,0.3,0.2])

    portfolio_stock_data = Get_the_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,period)

    # print(portfolio_stock_data.head())

    portfolio_stock_object = Monte_Carlo_Simulation_method(Stock_historical_data_df = portfolio_stock_data,portfolio_weights=portfolio_weights)

    portfolio_historical_return_df = (portfolio_stock_object.Calculating_daily_portfolio_Returns())

    portReturns = (portfolio_stock_object.Monte_Carlo_Simulation(portfolio_historical_return_df))
    # print(portReturns)

    quantile_95_for_VaR =portfolio_stock_object.Calculating_VaR_by_Monte_Carlo_Simulation(portReturns,5)
    # print(quantile_95_for_VaR)

    quantile_95_for_CVaR =portfolio_stock_object.Calculating_CVaR_by_Monte_Carlo_Simulation(portReturns,5)
    # print(quantile_95_for_CVaR)
    
    VaR = InitialInvestment - quantile_95_for_VaR
    # print(VaR)

    CVaR = InitialInvestment - quantile_95_for_CVaR
    # print(CVaR)

    print(f'For portfolio : {US_STOCK_LIST}')
    print('Value at Risk 95th CI    :      ', round(-VaR,2))
    print('Conditional VaR 95th CI  :      ', round(-CVaR,2))

    return VaR,CVaR

# portfolio2()


def single_stock_parametric_method():
    # * Testing for single stock

    US_STOCK_LIST = ["TSLA"]
    portfolio_stock_data = Get_the_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,period)

    TSLA_stock_object = parametric_method(portfolio_stock_data)

    TSLA_historical_return_df = (TSLA_stock_object.Calculating_daily_portfolio_Returns())

    TSLA_df_with_weights = TSLA_stock_object.add_Portfolio_columns_to_df(TSLA_historical_return_df)
    # print(portfolio_df_with_weights.head())

    Time = 1
    InitialInvestment = 10000

    VaR =(TSLA_stock_object.Calculating_VaR_by_parametric_method(TSLA_df_with_weights,5))

    portfolio_weights = np.array([1])
    print(f'VaR = {VaR}')
    hVaR = VaR*np.sqrt(Time) 

    mean_portfolio_historical_return_df = TSLA_historical_return_df.mean()
    covMatrix_portfolio_historical_return_df = TSLA_historical_return_df.cov()

    
    pRet, pStd = TSLA_stock_object.portfolioPerformance(portfolio_weights, mean_portfolio_historical_return_df, covMatrix_portfolio_historical_return_df, Time) 

    print(f'For single stock : {US_STOCK_LIST}')
    print('Expected Portfolio Return:      ', round(InitialInvestment*pRet,2))
    print('Value at Risk 95th CI    :      ', round(InitialInvestment*hVaR,2))

# single_stock_parametric_method()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def single_stock():
    # * Testing for single stock

    US_STOCK_LIST = ["TSLA"]
    portfolio_stock_data = Get_the_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,period)

    # print(portfolio_stock_data.head())
    portfolio_weights = np.array([1])

    TSLA_stock_object = Historical_Simulation(portfolio_stock_data)

    TSLA_historical_return_df = (TSLA_stock_object.Calculating_daily_portfolio_Returns())


    mean_portfolio_historical_return_df = TSLA_historical_return_df.mean()
    covMatrix_portfolio_historical_return_df = TSLA_historical_return_df.cov()


    TSLA_df_with_weights = TSLA_stock_object.add_Portfolio_columns_to_df(TSLA_historical_return_df)
    # print(portfolio_df_with_weights.head())

    # 100 days Time Horizon
    Time = 1
    InitialInvestment = 10000


    VaR = (TSLA_stock_object.Calculating_VaR_by_Historical_Simulation(TSLA_df_with_weights['Portfolio'],5))

    CVaR = (TSLA_stock_object.Calculating_CVaR_by_Historical_Simulation(TSLA_df_with_weights['Portfolio'],5))

    print(f'VaR = {VaR}')

    hVaR = VaR*np.sqrt(Time)

    hCVaR = CVaR*np.sqrt(Time)

    pRet, pStd = TSLA_stock_object.portfolioPerformance(portfolio_weights, mean_portfolio_historical_return_df, covMatrix_portfolio_historical_return_df, Time)


    print(f'For single stock : {US_STOCK_LIST}')

    print('Expected Portfolio Return:      ', round(InitialInvestment*pRet,2))
    print('Value at Risk 95th CI    :      ', round(InitialInvestment*hVaR,2))
    print('Conditional VaR 95th CI  :      ', round(InitialInvestment*hCVaR,2))

# single_stock()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def portfolio(US_STOCK_LIST, portfolio_weights, period):
    # * Testing for portfolio
    portfolio_weights = np.array(portfolio_weights)

    portfolio_stock_data = Get_the_stock_data.Get_the_stock_portfolio_historical_data_in_the_given_time(US_STOCK_LIST,period)


    # print(portfolio_stock_data.head())

    portfolio_stock_object = Historical_Simulation(Stock_historical_data_df = portfolio_stock_data,portfolio_weights=portfolio_weights)

    portfolio_historical_return_df = (portfolio_stock_object.Calculating_daily_portfolio_Returns())
    # print(portfolio_historical_return_df.head())

    mean_portfolio_historical_return_df = portfolio_historical_return_df.mean()
    covMatrix_portfolio_historical_return_df = portfolio_historical_return_df.cov()


    # print(portfolio_historical_return_df.head())

    portfolio_df_with_weights = portfolio_stock_object.add_Portfolio_columns_to_df(portfolio_historical_return_df)
    # print(portfolio_df_with_weights.head())


    # 100 days Time Horizon
    Time = 1
    InitialInvestment = 10000


    VaR = (portfolio_stock_object.Calculating_VaR_by_Historical_Simulation(portfolio_df_with_weights['Portfolio'],5))

    CVaR = (portfolio_stock_object.Calculating_CVaR_by_Historical_Simulation(portfolio_df_with_weights['Portfolio'],5))


    hVaR = VaR*np.sqrt(Time)

    hCVaR = CVaR*np.sqrt(Time)

    pRet, pStd = portfolio_stock_object.portfolioPerformance(portfolio_weights, mean_portfolio_historical_return_df, covMatrix_portfolio_historical_return_df, Time)

    # print(f'For portfolio : {US_STOCK_LIST}')
    # print('Expected Portfolio Return:      ', round(InitialInvestment*pRet,2))
    # print('Value at Risk 95th CI    :      ', round(InitialInvestment*hVaR,2))
    # print('Conditional VaR 95th CI  :      ', round(InitialInvestment*hCVaR,2))

    return [round(InitialInvestment*pRet,2), round(InitialInvestment*hVaR,2), round(InitialInvestment*hCVaR,2)]

# portfolio()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_weight(number_of_share, closing_price): 
    weight = []
    for i in range(len(number_of_share)):
        weight.append(number_of_share[i] * closing_price[i])
    weight = [round(i/sum(weight), 3) for i in weight]

    return weight