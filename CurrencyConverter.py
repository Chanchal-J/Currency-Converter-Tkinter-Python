from tkinter import Tk, ttk
from tkinter import *
import requests
import json
from PIL import Image, ImageTk
from currency_symbols import CurrencySymbols

def getSupportedCurrencies():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"

    headers = {
        "X-RapidAPI-Key": "d317b65ed9msh8bf8eff9997dd96p10c7d8jsn76e166961575",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    symbols = [ d['symbol'] for d in data ]

    return symbols

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    from_currency = combo1.get()
    to_currency = combo2.get()
    amount = value.get()
    querystring = {"from":from_currency,"to":to_currency,"amount":amount}
    
    headers = {
        "X-RapidAPI-Key": "d317b65ed9msh8bf8eff9997dd96p10c7d8jsn76e166961575",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    convertedAmount = data['result']['convertedAmount']
    result['text'] = CurrencySymbols.get_symbol(to_currency) + " " + str(round(convertedAmount,2))


# colors
cor0 = "#FFFFFF"    # white
cor1 = "#333333"    # black
cor2 = "#EB5D51"    # red

currency = getSupportedCurrencies()

window = Tk()
window.geometry('300x320')
window.title('Converter')
window.configure(bg=cor0)
window.resizable(height = FALSE, width = FALSE)

#frames
top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

# top frame
icon = Image.open("D:\Resume Projects\Currency Convertor - Tkinter - Python\icon.png")
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app_name = Label( top, image=icon, compound=LEFT, text='Currency Converter', height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_name.place(x=0,y=0)

# main frame
result = Label( main, text=' ', width=16, height=2, pady=7, relief='solid', anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
result.place(x=50, y=10)

fromLabel = Label( main, text='From', width=8, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
fromLabel.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

toLabel = Label( main, text='To', width=8, height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
toLabel.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50,y=155)

button = Button(main, text='Converter', width=19, padx=5, height=1, bg=cor2, fg=cor0, font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=210)

window.mainloop()