# from email import parser
# import tkinter
# from tkinter import ttk
# from tkinter import *
# from typing import Text
# import CsvParser
# import WebScraper
# import urllib
# from tkinterhtml import *




# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel
 
# Create Object
root = Tk()
 
# Set Geometry
root.geometry("400x400")
 
# Add label

my_label = HTMLLabel(root, html="""
    <a href='https://www.geeksforgeeks.org/'>GEEKSFORGEEKS</a>

<div class="D(ib) Mend(20px)"><fin-streamer class="Fw(b) Fz(36px) Mb(-4px) D(ib)" data-symbol="PFE" data-test="qsp-price" data-field="regularMarketPrice" data-trend="none" data-pricehint="2" value="49.15" active=""><span class="_11248a25 c916dce9">49.21</span></fin-streamer><fin-streamer class="Fw(500) Pstart(8px) Fz(24px)" data-symbol="PFE" data-test="qsp-price-change" data-field="regularMarketChange" data-trend="txt" data-pricehint="2" value="0.8100014" active=""><span class="_11248a25 _96166592 _8e5a1db9">+0.87</span></fin-streamer> <fin-streamer class="Fw(500) Pstart(8px) Fz(24px)" data-symbol="PFE" data-field="regularMarketChangePercent" data-trend="txt" data-pricehint="2" data-template="({fmt})" value="0.016756337" active=""><span class="_11248a25 _96166592 a13cb817">(+1.80%)</span></fin-streamer><fin-streamer class="D(n)" data-symbol="PFE" changeev="regularTimeChange" data-field="regularMarketTime" data-trend="none" value="" active="true"><span class="_11248a25 b2e85843">12:28PM EDT</span></fin-streamer><fin-streamer class="D(n)" data-symbol="PFE" changeev="marketState" data-field="marketState" data-trend="none" value="" active="true"><span class="_11248a25">REGULAR</span></fin-streamer><div id="quote-market-notice" class="C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm Whs(n)"><span>As of  12:28PM EDT. Market open.</span></div></div>


""")


# my_label = HTMLLabel(root, html="""
#     <a href='https://www.geeksforgeeks.org/'>GEEKSFORGEEKS</a>
     
 
# <p>Free Tutorials, Millions of Articles, Live, Online and Classroom Courses ,Frequent Coding Competitions ,Webinars by Industry Experts, Internship opportunities and Job Opportunities.</p>
 
 
#     <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20220408165312/image-15.png">
#     """)
    
 
# Adjust label
my_label.pack(pady=20, padx=20)
 
# Execute Tkinter
root.mainloop()





""" root = tkinter.Tk()
root.geometry("300x300") #size of window
root.wm_title("Aidans App")
frame = ttk.Frame(root,width = 250,height = 250)
frame.grid()

textBox = tkinter.Text(frame,height=1,width=5)
textBox.grid(column = 0, row = 1)
#arser = CsvParser.CsvManager('eggs.csv')

# def caclulateSharpe():
#     path = "stock_dfs/"
#     ticker = textBox.get(1.0, "end-1c").upper()
#     filename = path+ticker+".csv"
#     print(filename)
#     parser = CsvParser.CsvManager(filename)
#     parser.run()
#     print("[Sharpe method finished]")
#     # parser.run()
#     # print(parser)


##HTML DATA 
frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.set_content(urllib.request.urlopen("https://duckduckgo.com").read().decode())

##HTML DATA end

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
    return input """