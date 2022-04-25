#AidansApp
from asyncio.windows_events import NULL
from cProfile import run
from cgitb import text
from doctest import master
from pydoc import visiblename
import textwrap
import threading
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from turtle import title
from typing import Literal

from numpy import NaN
import WebScraper
import aidansThing

##PUBLIC VAL 
tickers = []

def doIt():
    WebScraper.multipleTickers(loadTickers(),'1mo')

def txboxListener(val):
    textBox.delete(0,END)
    textBox.insert([0],tickerList.get(tickerList.curselection()[0]))

    

def searchTicker():
    t = textBox.get()
    val = WebScraper.getHist(t,'1mo')
    #Display Data
    
    # i = 0
    
    adjCloseLabel['text'] =t+': Adj Close Data ' 
    adjCloseLabel['text'] =t+': Adj Close Data ' 

    adjCloseLabel.grid(column = 4, row = 6)
    b = bensTable()

    b.SharpeData.grid(column=4,row=8)
    b.AdjCloseData.grid(column=4,row=7)
    
    b.scrollbar.grid(row=0, column=1, sticky='ns')
    if(b.AdjCloseData.state == DISABLED):
        # print("initial condition",val[0])

        b.AdjCloseData.state = ACTIVE
        b.SharpeData.state = ACTIVE
        b.SharpeData.insert("",END,values = val[0])
        for v in val[1]:
            # i+=1
            # print(v)
            b.AdjCloseData.insert("",END,values = v)
        
    else:
        b.SharpeData.destroy()
        b.AdjCloseData.destroy()
        b = bensTable()   
        b.AdjCloseData.grid(column=4,row=7)
        b.scrollbar.grid(row=0, column=1, sticky='ns')
        b.SharpeData.grid(column=4,row=8)
        for v in val[1]:
            # i+=1
            print(v)
            b.AdjCloseData.insert("",END,values = v)
            # print(v)
        b.SharpeData.insert("",END,values = val[0])


    print("Displaying Data")


        # messagebox.showwarning("Error","Process failed, No Ticker Found. MAKE SURE ITS ALL CAPS")

def loadTickers():
    tickers = aidansThing.run()
    i = 0
    for ticker in tickers:
        i+=1
        tickerList.insert(i,str(ticker))
    runAllTickerBtn['state'] = ACTIVE
    return tickers

#creating app

root = Tk()
gui = ttk.Frame(root,padding = 100)
gui.grid()
gui.master.title("Aidans app")

#TextBox 
textBox = Entry(gui)
textBox.grid(column = 0, row =1,padx=50)
textBox.anchor

#Buttons

enterBtn = ttk.Button(gui,text="Search Ticker",command = searchTicker)
# enterBtn.grid(column=0,row=2)
enterBtn.place(x=30,y=115)

quitBtn = ttk.Button(gui,text = "Quit",command = root.destroy)
quitBtn.grid(column=2,row = 5)
quitBtn.place(x=75,y=140)
quitBtn.anchor

imporTickerBtn = ttk.Button(gui,text = "Import Tickers",command=loadTickers)
imporTickerBtn.grid(column=4,row=2)
imporTickerBtn.anchor

runAllTickerBtn = ttk.Button(gui,text="Run all Tickers",state=DISABLED,command = doIt)
# runAllTickerBtn.grid(column=0,row=3)
runAllTickerBtn.place(x=110,y=115)
runAllTickerBtn.anchor


tickerList = Listbox(gui)
tickerList.grid(column = 4, row = 1)
tickerList.anchor
# tickerList.place(x=150,y=-25)

#Labels
tickerList_lbl = ttk.Label(gui,text="List of Tickers")
tickerList_lbl.grid(column = 4, row = 0)
tickerList_lbl.anchor

adjCloseLabel = ttk.Label(gui)


class bensTable():
    def __init__(self):
        self.AdjCloseData = ttk.Treeview(gui, column="Adj Close",show="headings")
        self.AdjCloseData.heading(0, text='Adj Close')
        self.AdjCloseData.state = DISABLED
        self.scrollbar = ttk.Scrollbar(root, orient=tkinter.VERTICAL, command=self.AdjCloseData.yview)
        self.AdjCloseData.configure(yscroll=self.scrollbar.set)

        self.SharpeData =ttk.Treeview(gui, column="Sharpe Data",show="headings")
        self.SharpeData.heading(0, text ="Sharpe Data")
        self.SharpeData.state = DISABLED

     
## Binding 
tickerList.bind('<Button-1>',txboxListener)

gui.mainloop()

#Methods and Button commands









