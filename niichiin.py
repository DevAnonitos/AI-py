import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os

# modun 1: tạo voice nam or nữ
Niichin=pyttsx3.init()
voice=Niichin.getProperty('voices')
Niichin.setProperty('voice', voice[1].id)

# modun 2: tạo hàm speak để máy nói và in ra màn hình
def speak(audio):
    print('Niichin: ' + audio)
    Niichin.say(audio)
    Niichin.runAndWait()

# modun 3: thiết lập time để gọi time
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

# modun 4: thiết lập điều kiện giờ để gọi lệnh
def welcome():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak(" Good morning sir! ")
    elif hour >=12 and hour < 18:
        speak(" Good Afternoon sir! ")
    elif hour >=18 and hour < 24:
        speak(" Good Night sir! ")
    speak(' How can I help you ')

# modun 5: tạo gia tri để đưa giọng nói vào bot
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Tony Bảo: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query=str(input('Your oder is: '))
    return query

# modun 6: tạo liên kết trình duyệt để tìm kiếm
if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak(" What should U search boss")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f' Here is your {search} on google')
        if "youtube" in query:
            speak(" What should U search boss")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f' Here is your {search} on youtube')
        if "facebook" in query:
            speak(" What should U search boss")
            search=command().lower()
            url=f"https://www.facebook.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f' Here is your {search} on facebook')
        if "instagram" in query:
            speak(" What should U search boss")
            search=command().lower()
            url=f"https://www.instagram.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f' Here is your {search} on instagram')
        if "spotify" in query:
            speak(" What should U search boss")
            search=command().lower()
            url=f"https://open.spotify.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f' Here is your {search} on spotify')
        if "twitter" in query:
            speak(" What should U search boss")
            search=command().lower()
            url=f"https://twitter.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f' Here is your {search} on twitter')
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Niichin is quitting sir. Goodbye boss")
            quit()