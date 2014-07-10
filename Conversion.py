import urllib2
import json
import Tkinter
import tkMessageBox

# Functions
def Calculate():
    conversion = E1.get()
    calculate = float(conversion) * float(bitstamp)
    tkMessageBox.showinfo("Conversion", calculate)

# HTTP Request and JSON encoding

response = urllib2.urlopen('http://api.bitcoincharts.com/v1/markets.json')
http = response.read()
j = json.loads(http)

# Parsing data
# bitstamp
for x in j:
    symbol = x['symbol']
    if symbol == 'bitstampUSD':
        bitstamp = x['ask']


# GUI
gui = Tkinter.Tk()
B = Tkinter.Button(gui, text ="Calculate", command = Calculate)
var = Tkinter.StringVar()
varone = Tkinter.StringVar()
label = Tkinter.Label( gui, textvariable=var, underline=0)
bitstampprice = Tkinter.Label( gui, textvariable=varone, underline=0)
E1 = Tkinter.Entry(gui, bd =4)
var.set("Bitcoin to USD Converter")
bitstamplabel = 'Bitstamp', bitstamp
varone.set(bitstamplabel)
E1.pack(side = Tkinter.RIGHT)
label.pack()
B.pack()
bitstampprice.pack()
gui.mainloop()
