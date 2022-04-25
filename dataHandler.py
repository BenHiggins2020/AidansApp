from datetime import date, timedelta
import datetime
import pandas


print("===================================")
print("concatonating dateTimeIndex")
time_index = '2022-03-09'
yTens = '2'
yOnes = '2'

year = '20'+yTens+yOnes
mTens = '0'
mOnes = '3'
month = mTens+mOnes
dTens = "0"
dOnes = "9"
day = dTens+dOnes
#5 years ago ... 
# year_start = makeYear("7","1",True)

# d = makeDay("0","3")


#goal get the first and last day of the month... 
#check year - month -01 and year month 31 if no 31, 30 if no 30, 28 
#increment month... 
data = []

def last_day_of_month(any_day):
    # print(any_day)
    return (any_day.replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1)

def first_day_of_month2(any_day,month):
    days_in_month = []
    for date in any_day:
        if date.month == month:
            days_in_month.append(date)
    first_day_of_month = days_in_month[0]
    return first_day_of_month

def first_day_of_month(any_day,month):
    days_in_month = []
    for date in any_day:
        if date.month == month:
            days_in_month.append(date)
    first_day_of_month = days_in_month[0]
    return first_day_of_month

    # print(any_day.replace(day=1))
    # print(timedelta(days=31).replace(day=1))
    # print(- timedelta(days=1))
    # return (any_day.replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1)

# data = {}

# dates = hist.loc['Date']
# dates = hist.index[:] #get the dates

def getData(hist):
    # print("incrementing date")

    beans = []
    preVal = 0
    lastval = hist.shape[0]
    i = 0
    for date in hist.index:
        i+= 1
        val = date
        if preVal == 0: 
            #Initial condition
            # print("initial condition... ",val)
            beans.append({"date":val,"YEAR":[val.year]})
            preVal = val
            pass
        else:
            #Main Loop
            if val.month == preVal.month:
                #SAME MONTH
                preVal = val
                pass
            else:
                #DIFFERENT MONTH

                beans.append({"date":preVal,"YEAR":[preVal.year]}) 
                # ^ Previous value of the last month! 
                beans.append({"date":val,"YEAR":[val.year]})
                # ^ get the first value of the new month! 
                preVal = val

        if(i == lastval):
            beans.append({"date":date,"YEAR":[date.year]})
            # print("The final Condition! ",date)

    # print("=================BEANS=================================")
    BEANS = pandas.DataFrame()
    for line in beans:
        # print(line)
        d = line['date']
        date = pandas.Timestamp.to_pydatetime(d)
        v = hist.loc[date][4]
        row = pandas.DataFrame({
            'Date': [date],
            "Adj Close":[v]
        })
        BEANS=pandas.concat([BEANS,row],ignore_index=True).reset_index(drop=True)
    # print("==================BEANS DATAFRAME================================")
    # print(type(BEANS))
    BEANS.to_csv("data.csv")
    # print("==================================================")
    # print("FINISHED")
    return BEANS

# data = incrementDate()
# data.to_csv("data.csv")
