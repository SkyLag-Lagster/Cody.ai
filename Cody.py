import pyaudio
import pyjokes.jokes_de
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
import pywhatkit
import pyautogui
from faker import Faker
import googlesearch
import customtkinter as ct
from translate import Translator
import pyjokes
import randfacts
import json
from tkinter import *


ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("dark")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

kum = input("Enter Username: ")
if kum == 'SkyLag':
    password = input("Enter password: ")
    if password == "password":
        speak("Welcome back boss!")
    else:
        speak("That is not a valid password!I will contine with another name.")
        kum = input("Enter another name: ")

    if kum == 'LagSky':
        passw = input("Enter password: ")
        if passw == 'sayar':
            speak("Hello! big brother of boss!")
        else:
            speak("That is not a valid password!I will contine with another name.")
            kum = input("Enter another name: ")



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning!{kum}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!{kum}")

    else:
        speak(f"Good Evening!{kum}")

    speak(f"I am Cody. Please tell me how may I help you,{kum}")
    print(f"Hello {kum}, How can I help you...")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(input("Enter Sender Email address: "), input("password: "))
    server.sendmail(input("Enter Reciever's Email address: "), to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = input('Whats your query: ')
        query = takeCommand().lower()
        if query == 'reply in voice':
            query = takeCommand().lower()

        # Logic for executing tasks based on query


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = os.listdir("HTML KUMUD/Music")
            songs =   os.startfile(os.path.join(music_dir, songs[0]))
            print(songs)
      

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{kum}, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:/Users/dell/HTML Kumud"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = input("Enter reciever's email: ")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("")

        elif 'visit' in query:
            speak(f"ok {kum}, please enter url")
            url = input("Enter URL: ")
            webbrowser.open (url)
    
        elif 'play song'in query:
            speak("what is the name of song and singer")
            p= input("Enter name of song - singer: ")
            pywhatkit.playonyt(p)
            break

        elif'my song' in query:
            pywhatkit.playonyt("Vivaldi Winter")

        elif 'quit' in query:
            speak(f"see you later {kum}!!")
            break

        elif 'hello' in query:
            speak("hi what you want me to do!")

        elif 'what can you do' in query:
            q= "I can open youtube,google and stackoverflow; play song;email to someone; visit websites,end chat!!"
            speak(q)
            a="I can open youtube(say open youtube),google(say open google) and stackoverflow(open stack); play song(say play);email to someone(first you have to login); visit websites(say website);end chat(say quit)..."
        
            print(a)  

        elif 'search'in query:
            ques = input("What is your query: ")
            link = f"https://google.com/search?q={ques}"
            webbrowser.open_new_tab(link)
            break

        elif 'google' in query:
            searchs=googlesearch.search(term=query)
            results=(searchs)

            for query in results:
               print(results)
               speak(results)
               
        elif 'repeat' in query:
            runnn = True
            while runnn:
                limit=int(input("Enter your limit\n"))
                msg=str(input("Enter your Message\n"))
                print("Enter the app where u want to repeat")
                speak("Enter the app where u want to repeat")
                i=0
                while i <int(limit):
                    pyautogui.typewrite(msg)
                    pyautogui.press('enter')
            
            
                i+=1
                if limit < i:
                    print("repeat done...")
                    runnn = False

        elif 'send message' in query:
         pywhatkit.sendwhatmsg_instantly(
            input("Enter number with country code in strating: "),input('Enter message: '),10,
            pyautogui.press("enter")
            )
       
        elif 'play game' in query:
            options = ["rock", "paper", "scissors"]
            running = True
            while running:
                player= None
                cody_choice = random.choice(options)

                while player not in options:

                    speak("Let's play rock, paper and scissors!!")
                    player = input("Enter your choice (rock, paper, scissors): ").lower()

                    if player not in options:
                        speak("That's not a valid choice, boss! Try again.")
                    else:
                        print(f"You chose {player}, I chose {cody_choice}.")
                        speak(f"You choose {player}, I choose {cody_choice}.")
                        if player == cody_choice:
                            speak("It's a tie!")
                            print("It's a tie...")
                        elif (player == "rock" and cody_choice == "scissors") or \
                            (player == "scissors" and cody_choice == "paper") or \
                            (player == "paper" and cody_choice == "rock"):
                            speak("I lost!...")
                            print("I lost...")
                        else:
                            speak("I won...")
                            print("That was my frist step in beating humanity...")

                    if not input("Want to play again?(yes or no): ").lower() == "yes":
                     running = False
                    speak("Ok Boss!")
                    break
        elif 'fake' in query:
            fake = Faker()

            print ("Name: ", fake.name_male())
            print ("Address: ", fake.street_address())
            print ("Number: ", fake.phone_number())
            print ("Email: ", fake.free_email())

        elif 'flappy' in query:
            speak("Launching Flappy Bird! Get ready, boss!")
            exec(open("flappy/flappy.py").read())  # Assuming you save the game as `flappy_bird.py`

        elif 'golf' in query:
            speak("Launching Mini Golf! Get ready,boss!")
            exec(open("golf/crazy_golf.py").read())

        elif 'calculate' in query:
            exec(open("calculator.py").read())

        elif 'donkey' in query:
            if input("Want to play donkey kong?(yes or no): ").lower() == "yes":
                exec(open("donkey_kong.py").read())

        elif 'space invaders' in query:
            if input("Want to play Space Invaders?(yes or no): ").lower() == "yes":
                exec(open("space_invaders.py").read())

        elif 'your fav song' in query:
            speak("playing my favourite song on youtube")
            pywhatkit.playonyt("rick - rick roll")

        elif 'change name' in query:
            kum = input("Enter new name: ")

        elif 'number' in query:
            
            no = random.randint(1,100)
            rules = "I will think of a number between 1-100 ! You have to guess it! I will give you hint by saying 'too high' and 'too low'."
            print(rules)
            speak(rules)

            

            

            guess = 0
            while guess<20:

                guess=guess+1

                int_guss = int(input("Enter your guess: "))

                if int_guss == no:
                        print(f"You won.., The number was: {no}")
                        speak("You won!!!")
                        break
                        
                elif int_guss > no:
                        print("Too high")
                        speak("too high!")

                elif int_guss < no:
                        print("Too low ")
                        speak("too low!")

                if guess>= 20:
                    print("You lost..,Attempts exeded.")
                    print(f"The number was: {no}")
                    speak("You lost..,Attempts exeded.")
                    speak(f"The number was: {no}")

        elif 'ip detail' in query:
            exec(open("unwanted/ii/ip add.py").read())

        elif 'my ip' in query:
            exec(open("unwanted/ii/my ip.py").read())

        elif 'ip map' in query:
            exec(open("unwanted/ii/ip map.py").read())

        
        elif 'encode'in query:
            mess1 = input("Enter text for encoding: ")
            print('Your encoded text is: ')
            print(mess1.encode('utf-16','strict'))

        elif 'translate' in query:
            text = input("Enter text: ")
            language = input("Enter language for translation: ")

            Translator = Translator(to_lang=language)
            translation = Translator.translate(text)
            print(translation)
            speak(translation)

        elif 'history' in query:
            pywhatkit.show_history()

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'fact' in query:
            fact = randfacts.get_fact()
            print(fact)
            speak(fact)

        elif 'password' in query:
            char = "1234567890qwertyuiop789aSDFGHJKLlQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm456zxcvbnm1"
            lenght = int(input("Enter lenght of Password: "))
            passwordd = ""

            for a in range(lenght):
                passwordd+=random.choice(char)
            print(f"Your Password is: {passwordd}")

        elif 'snake' in query:
            exec(open("snake.py").read())

