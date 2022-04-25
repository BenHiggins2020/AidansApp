from re import T
import bs4 as bs #beautiful soup
import pickle
import requests


#price data imports
import datetime as dt
import os
import pandas_datareader as pdr
def run():
        # print("_________________________________________________")
        # print("Running aidans web scraper")

        # 5 year historical data from stock
        # given name of the stock
        # do calculation
        html = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')


        #api reaquest
        soup = bs.BeautifulSoup(html.text, 'lxml') #soup object parses 
        table = soup.find('table', {'class': 'wikitable sortable'}) #finding table in wiki

        #

        tickers = []
        for row in table.findAll('tr')[1:]:
                ticker = row.findAll('td')[0].text
                ticker = ticker[:-1]
                tickers.append(ticker)


        with open("sp500tickers.pickle", "wb") as f:   
                pickle.dump(tickers, f)

        # get price data 


        with open("sp500tickers.pickle", "rb") as f:
                tickers = pickle.load(f)
                #print("tickers : "+tickers)
                
        if not os.path.exists('stock_dfs'):
                os.makedirs('stock_dfs')


        start = dt.datetime(2017, 1, 1) # 5 years
        end = dt.datetime.now()


        #fix tickers to work with yahoo
        for ticker in tickers:
                if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
                        df = pdr.DataReader(ticker.replace('.', '-'), 'yahoo', start, end)
                        # print(df)
                        df.reset_index(inplace=True)
                        df.set_index("Date", inplace=True)
                        df.to_csv('stock_dfs/{}.csv'.format(ticker))
        #     else:
                # print()
        # print(tickers)
        # def sendFinishedNotification(t):
        #         return t

        # sendFinishedNotification()
        # print("[FINISHED]: tickers")


        
        return tickers