import os
import pyttsx3
import speech_recognition as sr
import webbrowser

en = pyttsx3.init()
en.setProperty('rate', 130)#Uso do tempo da fala deve posto antes
en.setProperty('volume', 1)#Uso do volume da fala deve posto antes e vai de 0-1
en.say("Olá senhor vlademir deseja  SABER ALGO ")
en.setProperty('voice', b'brasil')
en.runAndWait()

#webbrowser.open('www.google.com.br')#abre e executa uma url
#os.startfile('C:/') #abre e executa um diretorio ou pasta


rec = sr.Recognizer()
with sr.Microphone()as fonte:
       som = rec.listen(fonte)
       resposta = rec.recognize_google(som, language='pt')

if resposta == "sim":
       en.setProperty('rate', 150)
       en.setProperty('volume', 1)
       en.say("ok tudo certo, vou executar,")
       en.setProperty('voice', b'brasil')
       en.runAndWait()
       #os.system("Fala.wav")
       webbrowser.open('www.google.com.br')  # abre e executa uma url
       
elif resposta == "não":
       en.setProperty('rate', 150)
       en.setProperty('volume', 1)
       en.say("ok tudo certo, vou entrar no youtube,")
       en.setProperty('voice', b'brasil')
       en.runAndWait()
       webbrowser.open('https://www.youtube.com/watch?v=Tr89Na6TvBo')
else:
       en.setProperty('rate', 150)
       en.setProperty('volume', 1)
       en.say("Nao entendi nada, tenho que Sair,agoramesmo")
       en.setProperty('voice', b'brasil')
       en.runAndWait()
       os.startfile('C:/')



'''

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')

'''        
