from tkinter import *
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='J2UFWPNGL1UNQ748')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')

print(data)
# window = Tk()

# window.title("Welcome to will's stock app")

# window.geometry('350x200')

# lbl = Label(window, text="Get stock quotes")

# lbl.grid(column=0, row=0)

# stock = Entry(window,width=10)

# stock.grid(column=1, row=0)

# def clicked():

#     res = "Quote for " + stock.get()

#     lbl.configure(text= res)
#     print(stock.get())

# btn = Button(window, text="Click Me", command=clicked)

# btn.grid(column=2, row=0)

# window.mainloop()