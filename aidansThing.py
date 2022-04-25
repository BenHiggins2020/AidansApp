from re import T
import bs4 as bs #beautiful soup
import pickle
import requests


#price data imports
import datetime as dt
import os
import pandas_datareader as pdr
from yfinance import Tickers
def run():
        print('RUNNGINS')
        html = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        print('HTML request')


        #api reaquest
        soup = bs.BeautifulSoup(html.text, 'lxml') #soup object parses 
        table = soup.find('table', {'class': 'wikitable sortable'}) #finding table in wiki
        print('soup & table setup')

        #

        tickers = []
        for row in table.findAll('tr')[1:]:
                ticker = row.findAll('td')[0].text
                ticker = ticker[:-1]
                tickers.append(ticker)

        print('creating tickers')

        with open("sp500tickers.pickle", "wb") as f:   
                pickle.dump(tickers, f)

        print('creating pickle file')
        # get price data 


        with open("sp500tickers.pickle", "rb") as f:
                tickers = pickle.load(f)
                #print("tickers : "+tickers)
                
        print('using pickle file')


        if not os.path.exists('stock_dfs'):
                os.makedirs('stock_dfs')

        print('making stock_dfs directory')


        # end = dt.datetime.now()
        # start = dt.datetime(end.year-5, end.month, end.day) # 5 years
        
        print("setting date time")

        print("Modifying tickers for yahoo...(for loop)")

        #fix tickers to work with yahoo
        print(tickers)
        # for ticker in tickers:
        #         # ticker.replace('.', '-')
        #         # ticker.find("-")
        # #         # if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
        #         # df = pdr.DataReader(ticker.replace('.', '-'), 'yahoo', start, end)
        #         df = pdr.DataReader(ticker.replace('.', '-'), 'yahoo', start, end)

        #                 # # print(df)
        #                 # df.reset_index(inplace=True)
        #                 # df.set_index("Date", inplace=True)
        #                 # df.to_csv('stock_dfs/{}.csv'.format(ticker))

        # print("Loop finished")
        # print(df)
        #     else:
                # print()
        # print(tickers)
        # def sendFinishedNotification(t):
        #         return t

        # sendFinishedNotification()
        # print("[FINISHED]: tickers")

        # tickers = df.get('tickers')
        
        return tickers

