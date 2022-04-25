import csv , itertools , operator
import os
import statistics
from numpy import NaN
import pandas

# class CsvManager:
#     def __init__(self,filename):
#         self.filename = filename

def calculateStuff(dataFrame,ticker):
    # print("[CSV PARSER]")
    dataFrame = dataFrame.dropna()

    monthlyValues = dataFrame.get('Adj Close')
    if not os.path.exists('Tickers'):
        os.makedirs('Tickers')
    dataFrame.to_csv("Tickers/"+ticker+".csv")
    
    # print("\n",dataFrame,"\n\n\n\n\n\n")
    # print("=======================\n MONTHLY VALUES",monthlyValues,"\n===================")
    l = monthlyValues.size
    monthlyReturns = []
    prevVal = 0
    # print("LENGTH OF MONTHLY VALUE",l)

    for index in monthlyValues:
        # print(index)
        # print("[INDEX ]",type(index))

        
        if index == monthlyValues[0]:
            prevVal = index
            pass
        elif index == 0:
            prevVal = index
            pass
        else:
            monthlyReturns.append(index / prevVal - 1)
            # print(index,prevVal)
            prevVal = index
        if l -1 == index:
            break

    riskRate = 0.0009
    # try: 
    SharpeRate = statistics.mean(monthlyReturns) - riskRate / statistics.stdev(monthlyReturns)
    # except: 
        # SharpeRate = NaN
        # print("Ticker may be delisted")

    print("[CSV PARSER FINISHED] SharpeRate = ",SharpeRate)
    return SharpeRate , monthlyValues

        
