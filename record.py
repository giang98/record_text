import sounddevice as sd
from scipy.io.wavfile import write
import os
import nltk
from tkinter import *
import time

path = r"save_record"
fs = 44100
seconds = 60
gui = Tk(className='Record')
gui.geometry("500x500")

record_text = open('input.txt', encoding="utf-8").read()
text_array = nltk.sent_tokenize(record_text)
text = Text(gui)
index = 0
startTime = 0

# function to record
def Rec_sentence():
    global index
    index = index + 1
    global startTime
    startTime = time.time()
    text.delete(1.0, END)
    text.insert(INSERT, text_array[index])
    text.pack()
    global myrecording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    return startTime


btnRecord = Button(gui, text='Record', command=Rec_sentence)
btnRecord.pack()


def Stop_rec():
    text.delete(1.0, END)
    text.insert(INSERT, "Data has been save, press Record button to continue record")
    text.pack()
    sd.stop()
    duration = time.time() - startTime
    frame = int(duration * fs)
    write(path + '/' + str(len(os.listdir(path))) + '.' + 'wav', fs, myrecording[:frame])


btnSave = Button(gui, text='Save', command=Stop_rec)
btnSave.pack()

gui.mainloop()
