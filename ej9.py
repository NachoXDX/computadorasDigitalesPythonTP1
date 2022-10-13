from gtts import gTTS
from playsound import playsound

txt = input("Texto: ")
s = gTTS(txt,lang="es")
name = "decir"+txt.replace(" ","")+".mp3"
s.save(name)
playsound("./"+name)