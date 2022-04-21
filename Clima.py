from distutils.cmd import Command
import requests
import json
from tkinter import *  



api_key = "cf924283a722cd9965398c18456f18c7"
 

def temperatura(): 
    cidade = entrada.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"
    requisicao = requests.get (link)
    requisicao.dic = requisicao.json()
    descricao = requisicao.dic['weather'][0]['description']
    temperatura1 = requisicao.dic['main']['temp'] - 273.15
    
    tempo['text'] = (descricao, f"{temperatura1:.2f}C")

janela = Tk()
janela.title("CLIMA")
janela.geometry("300x300")

texto = Label(janela, text="Clique no botão para saber a temperatura de hoje")
texto.grid(column=0, row=0, padx=12, pady=12)

city = Label(janela, text="Diga sua cidade")
city.grid(column=0, row=2)

entrada= Entry(janela, width=10)
entrada.grid(column=0, row=3)

botao = Button(janela, text="Tempo hoje", command=temperatura)
botao.grid(column=0, row= 5, padx=12, pady=12)

tempo = Label(janela, text='')
tempo.grid(column=0, row=6)



janela.mainloop()