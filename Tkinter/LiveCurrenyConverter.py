import tkinter as tk
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

root = tk.Tk()
root.title("Live Currency Calculator")
input1 = tk.StringVar()
input2 = tk.StringVar()
input3 = tk.StringVar()


def calculate():
    fromC = input1.get().upper()
    toC = input2.get().upper()
    am = input3.get()
    print("From Currency " + fromC)
    print("To Currency : " + toC)
    print("Amount : ", am)
    input1.set("")
    input2.set("")
    input3.set("")
    final_link = "https://www.x-rates.com/calculator/?from=" + fromC + "&to=" + toC + "&amount=" + am
    download = urlopen(final_link)
    fetchData = download.read()
    download.close()
    page_soup = soup(fetchData, "html.parser")
    fetched_result = page_soup.find("span", {"class": "ccOutputRslt"})
    print(fetched_result.text)
    formatted_result = f"Your entered amount {am} {fromC} is equivalent\n to {fetched_result.text} "
    global result
    result = tk.Label(frame, text=formatted_result, font=('calibre', 10), background='#82E0AA')
    result.place(relwidth=0.8, relheight=0.2, relx=0.09, rely=0.75)
    return fetched_result.text


canvas = tk.Canvas(root, height=400, width=400, bg='#566573')

frame = tk.Frame(root, bg='#5DADE2')
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
title = tk.Label(frame, text='Live Currency Converter', width=50, height=2, font=('calibre', 15, 'bold', 'underline'))
title.pack()
# From Currency Label
fromCurrency = tk.Label(frame, text='Select from currency : ', width=5, font=('calibre', 10, 'bold'))
fromCurrency.place(relwidth=0.4, relheight=0.08, relx=0.02, rely=0.25)
# From Currency input 1
user_input1 = tk.Entry(frame, textvariable=input1, width=5, font=('calibre', 10, 'normal'), bd=2)
user_input1.place(relwidth=0.4, relheight=0.08, relx=0.5, rely=0.25)

# To Currency Label
toCurrency = tk.Label(frame, text='Select to currency : ', width=5, font=('calibre', 10, 'bold'))
toCurrency.place(relwidth=0.4, relheight=0.08, relx=0.02, rely=0.35)
# To Currency input 2
user_input2 = tk.Entry(frame, textvariable=input2, width=5, font=('calibre', 10, 'normal'), bd=2)
user_input2.place(relwidth=0.4, relheight=0.08, relx=0.5, rely=0.35)

# Amount Label
amount = tk.Label(frame, text='Enter the amount : ', width=5, font=('calibre', 10, 'bold'))
amount.place(relwidth=0.4, relheight=0.08, relx=0.02, rely=0.45)
# Amount input
user_input3 = tk.Entry(frame, textvariable=input3, width=5, font=('calibre', 10, 'normal'), bd=2)
user_input3.place(relwidth=0.4, relheight=0.08, relx=0.5, rely=0.45)

# Calculate button
calc = tk.Button(frame, text='Calculate', command=calculate, width=5, font=('calibre', 10, 'bold'), bd=2)
calc.place(relwidth=0.4, relheight=0.08, relx=0.30, rely=0.60)

# Result Label
result = tk.Text(frame, width=10, font=('calibre', 10, 'bold'))
result.place(relwidth=0.8, relheight=0.2, relx=0.09, rely=0.75)

canvas.pack()
root.mainloop()
