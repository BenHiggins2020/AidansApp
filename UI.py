from email import parser
import tkinter
from tkinter import ttk
from typing import Text
import CsvParser

root = tkinter.Tk()
root.geometry("300x300") #size of window
root.wm_title("Aidans App")
frame = ttk.Frame(root,width = 250,height = 250)
frame.grid()

textBox = tkinter.Text(frame,height=1,width=5)
textBox.grid(column = 0, row = 1)
#arser = CsvParser.CsvManager('eggs.csv')

def caclulateSharpe():
    path = "stock_dfs/"
    ticker = textBox.get(1.0, "end-1c").upper()
    filename = path+ticker+".csv"
    print(filename)
    parser = CsvParser.CsvManager(filename)
    parser.run()
    print("[Sharpe method finished]")
    # parser.run()
    # print(parser)


label = ttk.Label(frame, text = "Type Ticker")
label.grid(column=0, row = 0)
QuitBtn = ttk.Button(frame, text="Quit",command=root.destroy)
QuitBtn.grid(column = 0 , row = 3)

EnterBtn = ttk.Button(frame,text="Enter",command=caclulateSharpe)
EnterBtn.grid(column =0, row = 2)




frame.bind('<Enter>','calculateSharpe')

root.mainloop()



def getTyped():
    input = textBox.get("1.0","end-1c")
    print(input)
    parser = CsvParser.CsvManager('eggs.csv')
    return input