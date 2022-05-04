import csv , itertools , operator
import os
import statistics
from tkinter import END
from numpy import NaN
import pandas

# class CsvManager:
#     def __init__(self,filename):
#         self.filename = filename

def calculateStuff(dataFrame,ticker):
    # print("[CSV PARSER]")
    path =  os.path.realpath(__file__)
    dataFrame = dataFrame.dropna()

    monthlyValues = dataFrame.get('Adj Close')

    # dataFrame.to_csv("Tickers/"+ticker+".csv")
    
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
    print("MEAN ; ", statistics.mean(monthlyReturns))
    print("standard deviation: ",statistics.stdev(monthlyReturns))
    try: 
        SharpeRate = (statistics.mean(monthlyReturns) - riskRate )/ statistics.stdev(monthlyReturns)
    except:
        print("Issue with calculation... ticker may be wrong or delisted. ")
    # except: 
        # SharpeRate = NaN
        # print("Ticker may be delisted")

    print("[CSV PARSER FINISHED] SharpeRate = ",SharpeRate)

    if not os.path.exists('Tickers'):
        print("NO FILE FOUND CREATING DIRECTORY")
        os.makedirs('Tickers')
    else:
        print("file found "+os.path.dirname(os.path.abspath('Ticker'))+" ... directory not made")

    # df = pandas.DataFrame(SharpeRate,columns='Sharpe for '+ticker)
    # print("new file created with Sharpe: Tickers/"+ticker+".csv")
    # c = df.to_csv("Tickers/"+ticker+".csv")
    sharpeDF = pandas.DataFrame([ticker,SharpeRate])
    sharpeDF.to_csv("Tickers/"+ticker+"_Sharpe.csv")
    dataFrame.to_csv("Tickers/"+ticker+"_MonthlyData"+".csv")
    # dataFrame
    # p = "Tickers/"+ticker+".csv"
    # f = open(p, 'w')
    # reader = csv.reader(f)
    # writer = csv.writer(f)
    # for row in reader:
    #     rows = row.copy()
    #     print(row)
    #     for i in range(rows)+1:
    #         rows.append()
    # writer.writerow()
    # writer.writerow(END,["SharpeRate", SharpeRate, SharpeRate, SharpeRate, SharpeRate])
    # f.close()
    # fpath = "Tickers/"+ticker+".csv"
    # with open (fpath,'w',encoding='UTF8') as f:
        # writer = csv.writer(f)
        # writer.writerows(SharpeRate)

    return SharpeRate , monthlyValues

        
