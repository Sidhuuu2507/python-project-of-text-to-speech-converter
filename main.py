from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
import pyttsx3

BACKGROUND_COLOR = '#28BC9C'

class Home:
    def __init__(self, root):
        image = PhotoImage(file = 'ldrp.gif')
        root.iconphoto(True, image)
        root.title("LDRP")
        self.f = Frame(root, height=350, width=500, bg = BACKGROUND_COLOR)
        self.f.propagate(0)
        self.f.pack()
        Label(self.f, text="WELCOME", font="arial 20 bold", bg=BACKGROUND_COLOR).pack(pady=15)
        Label(self.f, text="Created by: Siddharth Trivedi", font='arial 8 bold', bg=BACKGROUND_COLOR, width='30').pack(side='bottom')
        text_to_speech_btn = Button(self.f, text="Text to Speech", font = 'arial 12 bold', command=self.TexttoSpeech,
                                    width=18, height=2, bg='royal blue', activebackground='sky blue').pack(pady=15)

        speech_to_text_btn = Button(self.f, text="Speech to Text", font = 'arial 12 bold', command=self.SpeechtoText,
                                    width=18, height=2, bg='royal blue', activebackground='blue').pack(pady=15)

        translate_btn = Button(self.f, text="Language Translator", font = 'arial 12 bold', command=self.languageTranslator,
                               width=18, height=2, bg='royal blue', activebackground='sky blue').pack(pady=15)

    def TexttoSpeech(self):
        newwindow = Toplevel(self.f)
        newwindow.title("Text to Speech")
        newwindow.geometry('1080x400')
        newwindow.config(bg=BACKGROUND_COLOR)
        Label(newwindow, text="Created by: Siddharth Trivedi", font='arial 8 bold', bg=BACKGROUND_COLOR,
              width='30').pack(side='bottom')

        self.input_text = Text(newwindow,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
        self.input_text.place(x = 320, y = 100)

        text_to_speech_btn = Button(newwindow, text="Text to Speech", font = 'arial 12 bold', command=self.Speak,
                                    width=18, height=2, bg='black', activebackground='sky blue').pack(side = TOP, pady = 20)

    def SpeechtoText(self):
        newwindow = Toplevel(self.f)
        newwindow.title("Speech to Text")
        newwindow.geometry('1080x400')
        newwindow.config(bg=BACKGROUND_COLOR)
        Label(newwindow, text="Created by: Siddharth Trivedi", font='arial 8 bold', bg=BACKGROUND_COLOR,
              width='30').pack(side='bottom')

        self.output_text = Text(newwindow, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
        self.output_text.place(x=320, y=100)
        speech_to_text_btn = Button(newwindow, text="Speak", font='arial 12 bold', command=self.Listen,
                                    width=18, height=2, bg='royal blue', activebackground='sky blue').pack(side=TOP,
                                                                                                           pady=20)
    def Listen(self):
        # initialize the recognizer
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            self.output_text.insert(END, "Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            text = r.recognize_google(audio, language='en-in')
            self.output_text.delete(1.0, END)
            self.output_text.insert(END, text)

        except:
            self.output_text.delete(1.0, END)
            self.output_text.insert(END, "Could not request result")


    def Speak(self):
        text_speech = pyttsx3.init()
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        input_text = self.input_text.get(1.0, END)
        text_speech.setProperty('voice', voice_id)
        text_speech.setProperty("rate", 120)
        text_speech.setProperty("volume", 10)
        text_speech.say(input_text)
        text_speech.runAndWait()

    def languageTranslator(self):
        input_lang = ["English", "gujarati", "hindi", "korean", "arabic", "french", "malayalam", "punjabi", "telugu"]

        # create a display window
        newwindow = Toplevel(self.f)
        newwindow.title("Language Translator")
        newwindow.geometry('1080x400')
        newwindow.config(bg=BACKGROUND_COLOR)  # 856ff8

        # create window
        newwindow.title("Language Translator")
        Label(newwindow, text="Created by: Siddharth Trivedi", font='arial 8 bold', bg=BACKGROUND_COLOR, width='30').pack(side='bottom')

        # create input and output widget
        Label(newwindow, text="Enter Text", font='arial 13 bold', bg=BACKGROUND_COLOR).place(x=100, y=60)
        self.input_text = Text(newwindow, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
        self.input_text.place(x=30, y=100)

        Label(newwindow, text="Output", font='arial 13 bold', bg=BACKGROUND_COLOR).place(x=700, y=60)
        self.output_text = Text(newwindow, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
        self.output_text.place(x=600, y=100)

        # Combobox to select language
        language = list(LANGUAGES.values())
        self.src_lang = ttk.Combobox(newwindow, values=input_lang, width=25)
        self.src_lang.place(x=250, y=60)
        self.src_lang.set('english')

        self.dest_lang = ttk.Combobox(newwindow, values=input_lang, width=25)
        self.dest_lang.place(x=800, y=60)
        self.dest_lang.set('english')

        # Create translate button
        trans_btn = Button(newwindow, text='Translate', font='arial 12 bold', pady=5,
                           command=self.Translate, bg='royal blue', activebackground='sky blue')

        trans_btn.place(x=490, y=180)

    def Translate(self):
        translator = Translator()
        translated = translator.translate(text=self.input_text.get(1.0, END), src=self.src_lang.get(), dest=self.dest_lang.get())

        self.output_text.delete(1.0, END)
        self.output_text.insert(END, translated.text)


root = Tk()
home = Home(root)
root.mainloop()