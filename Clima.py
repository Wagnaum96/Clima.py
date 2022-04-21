import requests
import json
from tkinter import *



api_key = " - cole sua chave aqui - "


def temperatura():
    cidade = entrada.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"
    requisicao = requests.get (link)
    requisicao.dic = requisicao.json()
    descricao = requisicao.dic['weather'][0]['description']
    temperatura1 = requisicao.dic['main']['temp'] - 273.15

    tempo['text'] = (descricao, f"{temperatura1:.2f}°C")

janela = Tk()
janela.title("CLIMA")
janela.geometry("510x300")
janela.configure(bg="#2F4F4F")
texto = Label(janela, text="Clique no botão para saber o clima de hoje",
              font="Verdana 15 bold",
              bg="#2F4F4F", fg="#B0C4DE")
texto.grid(column=0, row=0, padx=12, pady=12)

city = Label(janela, text="Diga sua cidade", font="Verdana 10 bold",
             bg="#2F4F4F", fg="#B0C4DE")
city.grid(column=0, row=2)

entrada= Entry(janela, width=10)
entrada.grid(column=0, row=3)

botao = Button(janela, text="Buscar",
               font="Verdana 15 bold",
               command=temperatura,
               bg="#2F4F4F", fg="#B0C4DE")
botao.grid(column=0, row= 4, padx=12, pady=12)

tempo = Label(janela, text='',bg="#2F4F4F", fg="#B0C4DE", font="Verdana 10 bold")
tempo.grid(column=0, row=6)



janela.mainloop()
