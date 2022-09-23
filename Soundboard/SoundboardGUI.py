from operator import index
import PySimpleGUI as sg
import playsound as ps
import glob
import random
from collections import defaultdict
import datetime

sg.theme(new_theme="Topanga")   #this is the GUI
column1 = [[sg.Text('column1')]]
dice_roll_disp = "Your dice rolls will appear here"
def makelayout():
    
    Layout=[[sg.Text("Soundboard!")],
        [sg.Text("")],
        [sg.Text("Press j to roll a d20")],
        [sg.Text(dice_roll_disp)],
        [sg.Text("")],
        [sg.Column(column1, scrollable=True,  vertical_scroll_only=True, key="_PREVIOUSROLLS_")],
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
diceRolls = []
diceTimes = []
while True:
    event,values=win.read(timeout=100)
    if event in ("Quit", None):
        break
    if event == 'j':
        print(diceRolls)
        dice_roll = random.randint(2, 19)
        diceRolls.append(dice_roll)
        now = datetime.datetime.now()
        diceTimes.append(str(now.time()).split('.')[0])
        #win.Element('_DICEROLLSTATUS_').update(f"You rolled a: {dice_roll}")
        #"at " + now.time() "you rolled a: " + dice_roll
        #win.Element('_PREVIOUSROLLS_').update([[sg.Text(f'{i}')] for i in diceRolls])

        #{diceTimes[index(i)]}
        i = 0
        column1Arr = []
        #while i < len(diceRolls):
        #    column1Arr.append()

        for i in diceRolls:
            column1Arr.append([sg.Text(f'at time  you rolled a: {i}')])

        column1 = [[sg.Text(f'at time  you rolled a: {i}')] for i in diceRolls]
        dice_roll_disp = f"You rolled a: {dice_roll}"
        win = sg.Window("SB", layout=makelayout(), return_keyboard_events=True)
        #win.refresh()
        if(dice_roll == 1):
            pass
        elif(dice_roll == 20):
            pass
        else:
            pass
            """
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
            """       
win.close()