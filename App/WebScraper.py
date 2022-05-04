from datetime import date, datetime
import math
from pickletools import long1
from urllib import request as _requests
import requests
import bs4
from numpy import NaN
import requests
import yfinance
import pandas
import dataHandler
import CsvParser
import bs4 as bs #beautiful soup
# import aidansThing

# a = yfinance.Ticker("A")
sharpes = pandas.DataFrame()
period = "5y"
interval = '1mo'
interval = '1d'


def getPriceUI(ticker):
    BASE_URL = str("https://finance.yahoo.com/quote/")
    url_string = str(BASE_URL)
    qs = "?p="
    queryString = str(qs)
    

    print("ticker ",(type(ticker)))
    print("base url ",type((BASE_URL)))
    print("url string",type(url_string))

    yahoo_URL = url_string + ticker + queryString + ticker

    print(yahoo_URL)

    html = requests.get(yahoo_URL)
    soup = bs.BeautifulSoup(html.text,"lxml")
    divName = soup.find('div',{'class':'D(ib) Mt(-5px) Maw(38%)--tab768 Maw(38%) Mend(10px) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})
    # print(divName)
    modified_name = soup.find('h1',{'class':'D(ib) Fz(18px)'})
    m = str(modified_name).replace('h1','h4')
    # print(m)
    divPrice = soup.find('div',{'class':'D(ib) Mend(20px)'})
    p = str(divPrice) #find value = ""
    print("\n original string \n"+p)
    # i = p.find('value="')
    # p[i:end]
    # print("\n index = "+i)
    p2 = p.split('value="')
    print("\n\n")
    print("new string\n"+p2[1])
    i = p2[1].find('"')
    p2 = p2[1]
    p = p2[0:i]
    print("\n\nfinal price = "+p2)
    # print("This is the div with the prices!" + str(div))
    return m,divPrice,p
    
getPriceUI("MMM")

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

    sharpes = pandas.DataFrame()

    print("\n SHARPES?? = "+sharpes)

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