import keyboard
import time
import datetime
import pyttsx3
tts = pyttsx3.init()
on = True
rate = tts.getProperty('rate')
tts.setProperty('rate', 200)
now = datetime.datetime.now()


def tell_time():
    tts.say(str(time.localtime().tm_hour)+":"+str(time.localtime().tm_min))
    tts.runAndWait()


def day_watcher():
    letters = list("ay")
    if word_maker(letters):
        tts.say(now.strftime("%A"))
        tts.runAndWait()


def year_watcher():
    letters = list("ear")
    if word_maker(letters):
        tts.say(now.strftime("%Y"))
        tts.runAndWait()


def word_maker(letters):
    compare = []
    for l in letters:
        start_time = time.time()
        while time.time() - start_time < 1:
            if keyboard.is_pressed(l):
                compare.append(l)
                break
    if compare == letters:
        return True
    else:
        return False


while on:
    if keyboard.is_pressed("/"):
        tell_time()
    if keyboard.is_pressed("d"):
        day_watcher()
    if keyboard.is_pressed("y"):
        year_watcher()

