import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
import requests
import urllib.request
import ssl



class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='ru') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Tatiana: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file
#activation phrase
WAKE = 'hey tatiana'

def respond(voice_data):
        #greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    #name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Tatiana")
        else:
            speak("my name is Tatiana. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) #remember name in person object

        #greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

        #time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
            minutes = time[1]
            time = f'{hours} {minutes}'
            speak(time)

        #search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    #search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
    
    #google maps location   
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('here is the location of ' + location)
    #Slav mode
    if there_exists(['tripaloski', 'slave mode','три полоски']): #'slave mode' beacuse it picks up Slav as slave
        speak(f'You are a true СЛАВ, сука блять')
        slavMusic = ['https://www.youtube.com/watch?v=QiFBgtgUtfw',
        'https://www.youtube.com/watch?v=QIjKijhv1OU',
        'https://www.youtube.com/watch?v=BnTW6fZz-1E']
        url = random.choice(slavMusic)
        webbrowser.get().open(url)
    #Mother Russia
    if there_exists(['play something classic']):
        speak(f'Now playing for mother RUSSIA!!')
        url = 'https://www.youtube.com/watch?v=U06jlgpMtQs'
        webbrowser.get().open(url)

    if there_exists(['play my playlist']):
        speak(f'playing {person_obj.name}s playlists')
        url = 'https://open.spotify.com/playlist/7dnbdUqqdb5h9ZjcfowpcV?si=uhYjNtZ2TAaPKcgkWgj-vw'
        webbrowser.get().open(url)
        if there_exists(['stop']):
            speak(f'Stopping')
            os.system("taskkill /im chrome.exe /f")
        
    if there_exists(['tell me a joke']):
        speak(f'Capitalism is the best economic system')
    
    # Current city or region
    if there_exists(["where am i"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        speak(f"You must be somewhere in {loc}")    
   
    #Current location as per Google maps
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        speak("You must be somewhere near here, as per Google maps")
     
    


    #exits the program
    if there_exists(["exit", "quit", "goodbye"]):
        speak("собирается в ГУЛАГ")
        exit()








time.sleep(1)
person_obj = person()
speak('I am Back online, твоя сука готова')
while (1):
    voice_data = record_audio()
    respond(voice_data)

