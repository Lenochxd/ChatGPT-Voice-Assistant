import pyttsx3
import json
import speech_recognition as sr
import os, sys, re
import shutil
import openai
from pathlib import Path

#os.remove("settings/settings.json")

firstTime = False
my_file = Path("settings/settings.json")
if not my_file.is_file():
    firstTime = True
    path = shutil.copyfile(r"settings/settings_default.json", r"settings/settings.json")
    
    
settings = json.load(open("settings/settings.json"))
settings["audio devices"] = {}
settings["voices"] = {}

openai.api_key = settings["api-key"]

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    settings["audio devices"][f"{index}"] = f"{name}"
json.dump(settings, open("settings/settings.json", 'w', encoding='utf8', errors='replace'), indent=4)
settings = json.load(open("settings/settings.json"))
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
count = 0
for i in voices:
    i=str(i)
    result = re.search(r'Voice id=(.+?)\n', f"{i}").group(1)
    settings["voices"][f"{count}"] = f"name={i.replace(result, '')}".replace('>','').replace('<',' ').replace("          ", "  |  ")
    
    count += 1
engine.setProperty('voice', voices[int(settings["voice selected"])].id)
    
    
def reload_settings(settings):
    try:
        json.dump(settings, open("settings/settings.json", 'w', encoding='utf8', errors='replace'), indent=4)
    except Exception as e:
        print(e)
        settings = json.load(open("settings/settings.json"))
        
    settings = json.load(open("settings/settings.json"))

reload_settings(settings)

def reload_words(words):
    try:
        json.dump(words, open("settings/words.json", 'w', encoding='utf8', errors='replace'), indent=4)
    except:
        pass
    words = json.load(open("settings/words.json"))
    
def speak(audio, text):
    
    engine.say(audio)
    engine.runAndWait()
    if text == "" or text.lower() == "none" or text == None:
        print(audio)
    else:
        print(text)
 
def takeCommand():
    
    reload_settings(settings)
    words = json.load(open("settings/words.json"))
    
    r = sr.Recognizer()
    
    device_selected = int(settings["device selected"])
    with sr.Microphone(device_index=device_selected) as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language=settings["language"])
        try:
            for key, value in words["default"].items():
                query = query.replace(f"{key}",f'{words["default"][key]}')
        except Exception as e:
            print(e)
            pass
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    
        
    try:
        for key, value in words["added"].items():
            query = query.replace(f"{key}",f'{value}')
    except Exception as e:
        print(e)
        pass
    
    return query


if __name__ == '__main__':
    if firstTime == True:
        sys.exit(
                 "\n"
                 "==========================================================\n"
                 "You can now change your settings in settings/settings.json\n"
                 "==========================================================\n"
                 )
    
    clear = lambda: os.system('cls')
    
    words = json.load(open("settings/words.json"))
    
    
    while True:
         
        query = takeCommand().lower()

        reload_settings(settings)
        
        if settings["prefix"].lower() in query:
            
            reload_settings(settings)
            before, sep, prompt = query.partition(settings["prefix"].lower())
            
            completion = openai.Completion.create(
                engine=settings["engine"],
                prompt=prompt,
                max_tokens=int(settings["max_tokens"]),
                n=1,
                stop=prompt,
                temperature=float(settings["temperature"])
            )
            final_chatgpt_response = completion.choices[0].text
            speak(final_chatgpt_response, final_chatgpt_response)