from bs4 import BeautifulSoup
import datetime
import requests
import urllib.request 
import time 
from gtts import gTTS
import os

print ("\nVerse of the Day: ")
res = requests.get('https://www.verseoftheday.com/en/')
soup = BeautifulSoup(res.content, 'lxml')
script_list=soup.find(class_='scripture').text 
print (script_list)
tts=gTTS(script_list,'en')
tts.save("myaudio.mp3")
print ("Reading verse ...")
os.system("wrun ffplay.exe -nodisp -autoexit -loglevel panic" + " myaudio.mp3")
time.sleep (2)
print ("Downloading verse of the day image...")
my_img=soup.find("div", {"id": "tv-image-wrapper"})
ex_img=my_img.find('img')
link_img=ex_img['src']
filen="verseoftheday.jpg"
urllib.request.urlretrieve(link_img, filen)
os.system("wstart "+filen)
print ("See you tomorrow.")
