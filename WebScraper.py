from datetime import date, datetime
import math
from pickletools import long1
import bs4
from numpy import NaN
import requests as _requests
import yfinance
import pandas
import dataHandler
import CsvParser
# import aidansThing

# a = yfinance.Ticker("A")
sharpes = pandas.DataFrame()
period = "5y"
interval = '1mo'
interval = '1d'
# ticker = "A"
# tickers = aidansThing.run()
# print(tickers)
# hist = a.history(period,interval)
# hist.to_csv("p.csv")

def getHist(ticker,interval):
    print('Ticker = ', ticker)
    print('Interval = ', interval)
    a = yfinance.Ticker(str(ticker))
    print("request = ",a)
    hist = a.history(period,interval)
    print("ARE THERE NANS IN HISTORICAL DATA", (NaN in hist))
    print("hist =",hist)
    if(interval == '1d'):
        df = dataHandler.getData(hist)
        sharpe = CsvParser.calculateStuff(df,ticker)[0]
    else:
        out = CsvParser.calculateStuff(hist,ticker)
        mData = out[1]
        sharpe = out[0]
    print("sharpe = ",sharpe)

    row = pandas.DataFrame({
        "Ticker":[ticker],
        "Sharpe":[sharpe]
        })

    sharpes = pandas.concat(
        [sharpes,row],
        ignore_index=True
        ).reset_index(drop=True)

    return sharpe ,mData

def multipleTickers(tickers,interval,loadingBar,root):
    sharpes = pandas.DataFrame()
    # tickers = ['A' ,'B']
    for ticker in tickers:
        print("=====================",ticker,"==========================")
        a = yfinance.Ticker(str(ticker))
        hist = a.history(period,interval)
        df = dataHandler.getData(hist)
        if(interval == '1d'):
            df = dataHandler.getData(hist)[0]
            sharpe = CsvParser.calculateStuff(df,ticker)[0]
        else:
            sharpe = CsvParser.calculateStuff(hist,ticker)[0]

        row = pandas.DataFrame({
            "Ticker":[ticker],
            "Sharpe":[sharpe],
            "Modifed Sharpe": [(sharpe * math.sqrt(12))]
        })
        sharpes = pandas.concat(
            [sharpes,row],
            ignore_index=True
            ).reset_index(drop=True)

        loadingBar.step()
        root.update()
        # loadingBar.
        
        # sharpes.append({"Ticker":ticker,"Sharpe":[sharpe]},ignore_index=True)

        # row = pandas.DataFrame({
        #     "Ticker": ticker,
        #     "Sharpe":float(sharpe)
        # })
        # sharpes.append({"Ticker":ticker,"Sharpe":[sharpe]},ignore_index=True)


    sharpes.to_csv("Tickers/_TickersNSharpes.csv")
    print("Added Tickers and Sharpes")

    print('COMPLETELY FINISHED')
    return sharpes


# def postProcessing(output):
#     print("SHARPES +++++++++++++++++++++++++++++++++ \n\n\n\n\n")
#     print(output,range(output))
#     with open("Tickers/TickersNSharpes.csv", "w",newline="") as f:
#         writer = csv.writer(f)
#         reader = csv.reader(f)
        


# getHist("BRK.B",'1mo')
# x = multipleTickers(tickers,'1mo')
# print(x)