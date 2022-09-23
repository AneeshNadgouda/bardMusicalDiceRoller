import PySimpleGUI as sg
import playsound as ps
import glob
import random
from collections import defaultdict

sg.theme(new_theme="Topanga")   #this is the GUI
def makelayout():
    Layout=[[sg.Text("Soundboard!")],
        [sg.Text("")],
        [sg.Text("Press j to roll a d20")],
        [sg.Text("", key="_DICEROLLSTATUS_",)],
        [sg.Text("")],
        [sg.Quit()]]
    return Layout

path = r'C:\Users\agn_a\Desktop\Projects\Soundboard'
roll_one = path + '\One'
roll_twenty = path + '\Twenty'
roll_default = path + '\Default'
defaultFiles = glob.glob(roll_default + "/*.mp3", recursive=True)
defaultFileArr = []
for file in defaultFiles:
    defaultFileArr.append(file)

soundsPlayed = []

win = sg.Window("SB", layout=makelayout(), return_keyboard_events=True)
soundboardon=False
while True:
    event,values=win.read(timeout=100)
    if event in ("Quit", None):
        break
    if event == 'j':
        dice_roll = random.randint(2, 19)
        print("You rolled a:", dice_roll)
        win.Element('_DICEROLLSTATUS_').update(f"You rolled a: {dice_roll}")
        win.refresh()
        if(dice_roll == 1):
            pass
        elif(dice_roll == 20):
            pass
        else:
            i = random.choice(range(len(defaultFileArr)))
            riff = defaultFileArr[i]
            ps.playsound(riff)
            soundsPlayed.append(riff)
            if(len(defaultFileArr) == 1):
                defaultFileArr = soundsPlayed
                soundsPlayed = []
                print("Deleted: ", str(riff))
                print("Reset sounds")
            else:
                del defaultFileArr[i]
                print("Deleted:", str(riff))        
win.close()