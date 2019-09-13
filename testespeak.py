'''
import os
os.system('espeak -v pt -s 145 "olá, Vlademir. "')

import os
os.system('espeak -v pt -s 145 " primeira vez, sou. o. maknno,'
          'o seu assistente de voz. "')

from subprocess import call

minhafala = "Third time, welcome. vlademir"

call(['espeak ', minhafala])

import pyttsx3
en = pyttsx3.init()
en.setProperty('rate', 165)#Uso do tempo da fala deve posto antes
en.setProperty('volume', 1)#Uso do volume da fala deve posto antes e vai de 0-1
en.say("Olá, sou a Jennifer, a sua assistete de voz seja bem vindo ao shóopiim tambiá,"
       " valide seu tikete em um dos caixas, e boas compras.")
en.setProperty('voice', b'brasil')

en.runAndWait()



import pyttsx3
en = pyttsx3.init()
en.setProperty('rate', 160)#Uso do tempo da fala deve posto antes
en.setProperty('volume', 1)#Uso do volume da fala deve posto antes e vai de 0-1
en.say("quarta vez.... Olá VLADEMIR, seja bem vindo peço mil desculpas"
       " mas vou ter que fazer alguns testes de volume e de  velocidade da voz antes de começar, certo, então vamos lá.")
en.setProperty('voice', b'brasil')

en.runAndWait()


import pyttsx3
en = pyttsx3.init()
novo_volume = 0.1
while novo_volume <=1:
    en.setProperty('rate', 140)#Uso do tempo da fala deve posto antes
    en.setProperty('volume', novo_volume)#Uso do volume da fala deve posto antes e vai de 0-1
    en.say("testando o volume,,, a, a, oi, oi, som, som, oquei, oqueissom..")
    en.setProperty('voice', b'brasil')
    en.runAndWait()
    novo_volume = novo_volume + 0.25


import pyttsx3
en = pyttsx3.init()
controle_velocidade = 50
while controle_velocidade <= 250:
    en.setProperty('rate', controle_velocidade)#Uso do tempo da fala deve posto antes
    en.setProperty('volume', 0.80)#Uso do volume da fala deve posto antes e vai de 0-1
    en.say("testando a velocidade com um, dois, tres, quatro, cinco,, teste,, um, dois, tres, quatro, cinco,.")
    en.setProperty('voice', b'brasil')
    en.runAndWait()
    controle_velocidade = controle_velocidade + 50

from subprocess import call
import pyttsx3
from datetime import datetime
import os

now = datetime.now()
nome = "Jennifer"
horas = now.hour
minutos = now.minute
dizer = str("se liga O nome dela é " + nome + " ouviu amigo vlademir, e Agora, é ou são, "
            + str(horas) + " horas i, " +str(minutos)+ " minutos,, na capital paraibana. ")
print(dizer)
#a = dizer
#call(['espeak', dizer])
#os.system('espeak -v pt -s 135'+ a)
en = pyttsx3.init()
controle_velocidade = 140
novo_volume = 1
en.setProperty('rate', controle_velocidade)#Uso do tempo da fala deve posto antes
en.setProperty('volume', novo_volume)#Uso do volume da fala deve posto antes e vai de 0-1
en.say(dizer)
en.setProperty('voice', b'brasil')
en.runAndWait()

from gtts import gTTS
from datetime import datetime
import os
now = datetime.now()

print(now)
fala = gTTS("pronto o teste foi bem sucedido certo VLADEMIR  peço mil desculpas,"
       " mas foi necessario para fazeralguns testes antes de começar o programa da nuvem do google. uma boa noite e fica com Jesus", lang=('pt'))
fala.save("fala.mp3")

os.system("fala.mp3")

'''

print("-------------- TESTE RECOGNATION com som gravado---------------")
#from gtts import gTTS
import speech_recognition as sr
#import os
#os.system('espeak -v pt -s 130 "olá, Vlademir. "')
#fala = gTTS(" hello welcome vlademir ok ok test")
#fala.save("Foi.wav")
#os.system("fala4.mp3")
rec = sr.Recognizer()
PATH = 'Fala.wav'
with sr.AudioFile(PATH) as fonte:
    audio = rec.record(fonte)
    print(rec.recognize_sphinx(audio))

print("-------------- TESTE RECOGNATION COM GOOGLE---------------")

import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone()as fonte:
    print("Fale algo")
    som = rec.listen(fonte)
    x = rec.recognize_google(som, language='pt')
print(x)



print("-------------- TESTE RECOGNATION COM Sim ou Nao---------------")
import speech_recognition as sr
import os

rec = sr.Recognizer()
with sr.Microphone()as fonte:
    print("Sim")
    som = rec.listen(fonte)
resposta = rec.recognize_google(som, language='pt')
if resposta == "sim":
    print("Abrindo arquivo")
    os.system(r'Fala.wav')
elif resposta == "nao":
    print("Fechando o programa")
else:
    print("Fechando o programa voce nao falou nada")


print("-------------- TESTE RECOGNATION para multiplicar---------------")
import speech_recognition as sr
rec = sr.Recognizer()
with sr.Microphone()as fonte:
    while True:
        print("Informe a multiplicaçao:")
        som = rec.listen(fonte)
        junta = rec.recognize_google(som, language='pt')
        if junta == "fechar":
            break
        print("Multiplicando: " + str(junta))
        print("Resultado:" + str(int(junta[0]) * int(junta[4])))



'''
print("-------------- TESTE RECOGNATION ---------------")

import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone()as fonte:
    print("Fale algo")
    audio = rec.listen(fonte)
    x = rec.recognize_sphinx(audio)
print(x)

print("-------------- TESTE RECOGNATION-2 ---------------")

import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone()as fonte:
    while True:
        rec.adjust_for_ambient_noise(fonte, duration=3)
        print("Fale algo")
        audio = rec.listen(fonte)
        x = rec.recognize_sphinx(audio)
        print(x)


print("-------------- TESTE RECOGNATION em ingles---------------")

from pocketsphinx import LiveSpeech

for frase in LiveSpeech():
    print("Voce Disse: ", str(frase))

'''