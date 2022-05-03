#AidansApp
from asyncio.windows_events import NULL
from cProfile import run
from cgitb import text
from doctest import master
import math
from pydoc import visiblename
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from turtle import title
from typing import Literal

from numpy import NaN, pad
import WebScraper
import aidansThing
from art import *

##PUBLIC VAL 
tickers = []

Art = text2art("Aidans App by Ben Higgins",font ="univers")
Art2 = text2art("Aidans App by Ben Higgins",font ="tengwar")
Art3 = text2art("Aidans App by Ben Higgins",font ="varsity")
Art4 = text2art("Aidans App by Ben Higgins",font ="sub-zero")

print("\n\n\n\n\n\n\n\n\n")
print(Art)
print("\n\n\n\n\n\n\n\n\n")
print(Art2)
print("\n\n\n\n\n\n\n\n\n")
print(Art3)
print("\n\n\n\n\n\n\n\n\n")
print(Art4)



def doIt():
    WebScraper.multipleTickers(loadTickers(),'1mo',loadingBar,root)

def txboxListener(val):
    print("text box listener running")
    textBox.delete(0,END)
    textBox.insert([0],tickerList.get(tickerList.curselection()[0]))

    if(type(val) == list):
        pass
    else: 
        if tickerList.curselection() == NaN:
            textBox.delete(0,END)
            textBox.insert([0],tickerList.get(tickerList.curselection()[0]))
        else:
            pass 

def createBensTable(): 
        adjCloseLabel['text'] =t+': Adj Close Data ' 

        adjCloseLabel.grid(column = 4, row = 6)
        b = bensTable()
        
        b.SharpeData.grid(column=4,row=8)
        b.AdjCloseData.grid(column=4,row=7)
        # b.modifiedSharpe.grid(column=4,row=9)
        b.scrollbar.grid(row=0, column=1, sticky='ns')
        if(b.AdjCloseData.state == DISABLED):
            print("initial condition",val[0])

            b.AdjCloseData.state = ACTIVE
            b.SharpeData.state = ACTIVE
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
            for v in val[1]:
                # i+=1
                print(v)
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
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
            b.AdjCloseData.columnconfigure(1,pad=0)

        b = bensTable()

        b.SharpeData.grid(column=4,row=8)
        b.AdjCloseData.grid(column=4,row=7)
        # b.modifiedSharpe.grid(column=4,row=9)
        b.scrollbar.grid(row=0, column=1, sticky='ns')
        if(b.AdjCloseData.state == DISABLED):
            print("initial condition",val[0])

            b.AdjCloseData.state = ACTIVE
            b.SharpeData.state = ACTIVE
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
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
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
            b.AdjCloseData.columnconfigure(1,pad=0)
    

def searchTicker(ranall = False):
    if(ranall):
        t = textBox.get()
        val = WebScraper.getHist(t,'1mo')
        #Display Data
        # i = 0
        
        # adjCloseLabel['text'] =t+': Adj Close Data ' 
        adjCloseLabel['text'] =t+': Adj Close Data ' 

        adjCloseLabel.grid(column = 4, row = 6)
        b = bensTable()

        b.SharpeData.grid(column=4,row=8)
        b.AdjCloseData.grid(column=4,row=7)
        # b.modifiedSharpe.grid(column=4,row=9)
        b.scrollbar.grid(row=0, column=1, sticky='ns')
        if(b.AdjCloseData.state == DISABLED):
            print("initial condition",val[0])

            b.AdjCloseData.state = ACTIVE
            b.SharpeData.state = ACTIVE
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
            for v in val[1]:
                # i+=1
                print(v)
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
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
            b.AdjCloseData.columnconfigure(1,pad=0)
    else:

        t = textBox.get()
        val = WebScraper.getHist(t,'1mo')

        b = bensTable()

        b.SharpeData.grid(column=4,row=8)
        b.AdjCloseData.grid(column=4,row=7)
        # b.modifiedSharpe.grid(column=4,row=9)
        b.scrollbar.grid(row=0, column=1, sticky='ns')
        if(b.AdjCloseData.state == DISABLED):
            print("initial condition",val[0])

            b.AdjCloseData.state = ACTIVE
            b.SharpeData.state = ACTIVE
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
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
            b.SharpeData.insert("",END,values = (val[0],(val[0]*math.sqrt(12))))
            b.AdjCloseData.columnconfigure(1,pad=0) 

    print("Displaying Data")


        # messagebox.showwarning("Error","Process failed, No Ticker Found. MAKE SURE ITS ALL CAPS")

def loadTickers():
    print("[IMPORTING TICKERS]")
    tickers = aidansThing.run()
    i = 0
    yahooTickers = []
    for ticker in tickers:
        i+=1
        if '.' in ticker:
            print("BEFORE",ticker)
            ticker = ticker.replace('.','-')
            print("AFTER",ticker)

        yahooTickers.append(ticker)
        tickerList.insert(i,str(ticker))
        # print(tickerList)
        
    runAllTickerBtn['state'] = ACTIVE
    return yahooTickers #tickerList.get(0,END)[:]#tickers

#creating app

root = Tk()
gui = ttk.Frame(root,padding = 100)
gui.grid()
gui.master.title("Aidans app")

#TextBox 
textBox = Entry(gui)
textBox.grid(column = 0, row =1,padx=50)
w = textBox.winfo_width
print("     width",w)
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

#Loading Bar 

loadingBar = ttk.Progressbar(root,orient=HORIZONTAL,length=125,mode="determinate",takefocus=True,maximum=500)
# loadingBar.grid(column=4, row = 9)
loadingBar.place(x=150,y=140)

#Labels
tickerList_lbl = ttk.Label(gui,text="List of Tickers")
tickerList_lbl.grid(column = 4, row = 0)
tickerList_lbl.anchor

adjCloseLabel = ttk.Label(gui)


class bensTable():
    def __init__(self):
        print("INITIALIZING BENS TABLE!!!!")
        self.AdjCloseData = ttk.Treeview(gui, columns=1,show="headings")
        self.AdjCloseData.heading(0, text='Adj Close')
        self.AdjCloseData.state = DISABLED
        self.scrollbar = ttk.Scrollbar(root, orient=tkinter.VERTICAL, command=self.AdjCloseData.yview)
        self.AdjCloseData.configure(yscroll=self.scrollbar.set)

        self.SharpeData =ttk.Treeview(gui, columns=(0,1),show="headings",height=1)
        self.SharpeData.heading(0, text ="Sharpe Data")
        self.SharpeData.heading(1, text= "Modified Sharpe x sqrt(12)")
        self.SharpeData.state = DISABLED

        # self.modifiedSharpe =ttk.Treeview(gui, columns=1,show="headings",height=1)
        # self.modifiedSharpe.heading(0, text ="Aidans Modified Sharpe = Sharpe x sqrt(12)")
        # self.modifiedSharpe.state = DISABLED

     
## Binding 
tickerList.bind('<Button-1>',txboxListener)

gui.mainloop()

#Methods and Button commands









