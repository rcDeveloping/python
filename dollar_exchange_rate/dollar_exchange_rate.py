import requests
from tkinter import *


# get dollar and other coins exchange rate from web
get_rate = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')


'''
exchage labels
bid = compra
ask = venda
varBid = variacao
pctChange = Porcentagem de Variacao
high = Maximo
low = Minimo
'''


# function to print the exchange rate
def get_exchange_rate():
        request_url = get_rate

        request_dict = request_url.json()

        dollar_exchange = request_dict['USDBRL']['bid']
        euro_exchange = request_dict['EURBRL']['bid']
        btc_exchange = request_dict['BTCBRL']['bid']

        text_rate = f'''
        Dolar: {round(float(dollar_exchange), 3)}
        Euro: {round(float(euro_exchange), 3)}
        BitCoin: {round(float(btc_exchange), 3)}
        '''

        # print(text_rate)
        txt_exchange['text'] = text_rate


# call function
# get_exchange_rate()

# convert real to dollar
def real_to_dollar():
        request_url = get_rate

        request_dict = request_url.json()

        dollar_exchange = request_dict['USDBRL']['bid']
        euro_exchange = request_dict['EURBRL']['bid']
        btc_exchange = request_dict['BTCBRL']['bid']

        text_convert_out = f'''
        Dollar: {round(float(dollar_exchange),2) * float(real.get())}
        '''

        txt_convert['text'] = text_convert_out

# Build GUI #
main_window = Tk()

main_window.title('Cotação Atual de moedas')
#main_window.geometry("400x150")

txt_position = Label(main_window, text='Click no botão para ver as cotações das moedas')
txt_position.grid(column=0, row=0, padx=10, pady=10)

button = Button(main_window, text='Buscar Cotações Dólar/Euro/BTC', command=get_exchange_rate)
button.grid(column=0, row=1)

txt_exchange = Label(main_window, text='')
txt_exchange.grid(column=0, row=2)

# converting between coins
text_position = Label(main_window, text='Converter um valor em Real para Dólar')
text_position.grid(column=0, row=4, padx=10, pady=10)

text_position = Label(main_window, text='Informe o Valor em Real')
text_position.grid(column=0, row=5)
real = Entry(main_window)
real.place(width=200, height=50)
real.grid(column=0, row=6)

button_convert = Button(main_window, text='Real para Dólar', command=real_to_dollar)
button_convert.grid(column=0, row=7)

txt_convert = Label(main_window, text='')
txt_convert.grid(column=0, row=8)

main_window.mainloop()
