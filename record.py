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
gui.geometry("800x500")
record_text = open('input.txt', encoding="utf-8").read()
text_array = nltk.sent_tokenize(record_text)
text = Text(gui)
index = 0
startTime = 0


def divide_sentence():
    lines = nltk.sent_tokenize(record_text)
    with open(r'news.txt', 'w', encoding="utf-8")  as file:
        count = 0
        for line in lines:
            file.write(str(count) + '.' + "wave\n")

            file.write(line + '\n')
            count = count + 1
        file.close()


def start_rec():
    global index
    global startTime
    startTime = time.time()
    text.delete(1.0, END)
    if text_array[index] is None:
        text.insert(INSERT, "End of file")
    else:
        text.insert(INSERT, text_array[index])
    text.pack()
    index = index + 1
    global recording
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    return startTime


btnRecord = Button(gui, text='Record', command=start_rec)
btnRecord.pack()


def stop_rec():
    text.delete(1.0, END)
    text.insert(INSERT, "Data has been save, press Record button to continue record")
    text.pack()
    sd.stop()
    duration = time.time() - startTime
    frame = int(duration * fs)
    write(path + '/' + str(len(os.listdir(path))) + '.' + 'wav', fs, recording[:frame])


btnSave = Button(gui, text='Save', command=stop_rec)
btnSave.pack()

divide_sentence()
gui.mainloop()
