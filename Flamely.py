import ctypes
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initialize')\

voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

greeting_dict = {'hello':'hello','hi':'hi'}
open_launch_dict = {'open':'open','launch':'launch'}
thank_dict = {'thanks':'thanks','thank you':'thank you'}
Leave_dict = {'bye':'bye','goodbye':'goodbye','shutdown':'shutdown'}
google_searches_dict = {'what':'what','why':'why','who':'who','which':'which','how':'how'}
social_media_dict = {'instagram':'https://www.instagram.com','twitter':'https://www.twitter.com'}

def is_valid_google_search(phrase):
    if(google_searches_dict.get(phrase.split(' ')[0] )==phrase.split(' ')[0]):
        return True

def read_voice_cmd():

    voice_text = ''
    print('Listening...')

    with sr.Microphone() as source:
        audio = speech.listen(source=source,timeout=10,phrase_time_limit=5)

        try:
            voice_text = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print('Network error')
        except sr.WaitTimeoutError:
            pass
        return voice_text

def is_Valid_note(greet_dict,voice_note):
    for key, value in greet_dict.items():

        try:
            if value == voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break
        except IndexError:
            pass

    return False


if __name__ == '__main__':

    speak_text_cmd('Hello Mr.Goswami. This is your Artificial Intelligence as Flamey')

    hour = int(datetime.datetime.now().hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S")

    if hour>=6 and hour<12:
        speak_text_cmd("Good Morning Mr. Goswami")

    elif hour>=12 and hour<=18:
        speak_text_cmd("Good Afternoon Mr. Goswami")

    elif hour>=18 and hour<=24:
        speak_text_cmd("Good Evening Mr. Goswami")

    else:
        speak_text_cmd("Good Night Mr. Goswami")

    

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_Valid_note(greeting_dict, voice_note):
            print('In greeting...')
            speak_text_cmd('Yes, Mr.Goswami?')
            continue
        if is_Valid_note(thank_dict, voice_note):
            speak_text_cmd('no problem!')
            continue
        if 'how are you doing' in voice_note:
            speak_text_cmd('im doing great!')
            continue
        elif is_Valid_note(open_launch_dict, voice_note):
            print('In open...')
            speak_text_cmd('Sure!')
            if(is_Valid_note(social_media_dict,voice_note)):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\"{}"'.format(voice_note.replace('Open ', '').replace('launch ','')))
            continue

        elif is_valid_google_search(voice_note):
            print('In Google search...')
            speak_text_cmd('Here is what I found')
            webbrowser.open('https://www.google.com/search?q={}'.format(voice_note))
            continue
        elif 'lock it' in voice_note:
            for value in ['pc','system','windows']:
                ctypes.windll.user32.LockWorkStation()

        elif 'time' in voice_note:
            strftime = datetime.datetime.now().strftime("%I:%M:%S")
            speak_text_cmd(f"The Fucking time is {strftime}")

        elif 'date' in voice_note:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak_text_cmd("the current Date is")
            speak_text_cmd(month)
            speak_text_cmd(date)
            speak_text_cmd(year)


        elif is_Valid_note(Leave_dict, voice_note):
            speak_text_cmd('Bye Mr.Goswami. Have a good day.')
            exit()
