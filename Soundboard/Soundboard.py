from multiprocessing.connection import wait
import playsound as ps
import glob
import random
from tkinter import *
from tkvideo import tkvideo


global defaultFileArr, soundsPlayed, test, d1
defaultFileArr, soundsPlayed, test, d1 = [], [], [], ''

path = r'C:\Users\agn_a\Desktop\Projects\Soundboard\bardMusicalDiceRoller\Soundboard'
roll_one = path + '\One'
roll_twenty = path + '\Twenty'
roll_default = path + '\Default'

defaultFiles = glob.glob(roll_default + "/*.mp3", recursive=True)

for file in defaultFiles:
    defaultFileArr.append(file)
    test.append(file)

root = Tk()
root.title('Bardic Dice Roller')
root.iconbitmap()
root.geometry("500x500")

def get_number(x):
    path = "C:\\Users\\agn_a\\Desktop\\Projects\\Soundboard\\bardMusicalDiceRoller\\Soundboard\\Dice\\"
    if x == path + '1.mp4':
        return(1)
    if x == path + '2.mp4':
        return(2)
    if x == path + '3.mp4':
        return(3)
    if x == path + '4.mp4':
        return(4)
    if x == path + '5.mp4':
        return(5)
    if x == path + '6.mp4':
        return(6)
    if x == path + '7.mp4':
        return(7)
    if x == path + '8.mp4':
        return(8)
    if x == path + '9.mp4':
        return(9)
    if x == path + '10.mp4':
        return(10)
    if x == path + '11.mp4':
        return(11)
    if x == path + '12.mp4':
        return(12)
    if x == path + '13.mp4':
        return(13)
    if x == path + '14.mp4':
        return(14)
    if x == path + '15.mp4':
        return(15)
    if x == path + '16.mp4':
        return(16)
    if x == path + '17.mp4':
        return(17)
    if x == path + '18.mp4':
        return(18)
    if x == path + '19.mp4':
        return(19)
    if x == path + '20.mp4':
        return(20)

def playRiff(d1):
    if(get_number(d1) == 1):
        pass
    elif(get_number(d1) == 20):
        pass
    else:
        print(random.choice(range(len(test))))
        i = random.choice(range(len(defaultFileArr)))
        riff = defaultFileArr[i]
        ps.playsound(riff, False)
        soundsPlayed.append(riff)
        if(len(defaultFileArr) == 1):
            for i in soundsPlayed:
                defaultFileArr.append(i)
            del defaultFileArr[0]
            for i in range(len(soundsPlayed)):
                try:
                    del soundsPlayed[i]
                except:
                    break
            print("Deleted: ", str(riff))
            print("Reset sounds")
        else:
            del defaultFileArr[i]
            print("Deleted:", str(riff)) 

#Roll the dice
def roll_dice():
    #roll random dice
    d1 = random.choice(my_dice)

    #update labels
    player = tkvideo(d1, dice_label1, loop = 0, size = (1280,720))
    player.play()

    #Update total label
    
    total_label.config(text = f"You rolled a {get_number(d1)}!!!")

def perform_roll():
    roll_dice()
    playRiff(d1)

#Create a Dice List
dicevids = glob.glob(r"C:\Users\agn_a\Desktop\Projects\Soundboard\bardMusicalDiceRoller\Soundboard\Dice" + "/*.mp4", recursive=True)
my_dice = []
for vid in dicevids:
    my_dice.append(vid)


#Create a frame
my_frame = Frame(root)
my_frame.pack(pady = 20)

#create dice labels
dice_label1 = Label(my_frame, text = '', font = ("Helvetica", 100), fg = "black")
dice_label1.grid(row = 0, column = 0, padx = 5)

#create Roll button
my_button = Button(root, text = "Roll Dice", command = perform_roll, font = ("Helvetica", 24))
my_button.pack(pady = 20)

#create totals label
total_label = Label(root, text = "", font = ("Helvetica", 24), fg="grey")
total_label.pack(pady = 40)

#roll the dice
roll_dice()
root.mainloop()


# path = r'C:\Users\agn_a\Desktop\Projects\Soundboard'
# roll_one = path + '\One'
# roll_twenty = path + '\Twenty'
# roll_default = path + '\Default'
# defaultFiles = glob.glob(roll_default + "/*.mp3", recursive=True)
# defaultFileArr = []
# for file in defaultFiles:
#     defaultFileArr.append(file)

# soundsPlayed = []

# while True:
#     if keyboard.is_pressed('q'):
#         dice_roll = random.randint(2, 19)
#         print("You rolled a " + str(dice_roll) + "!!!")

#         if(dice_roll == 1):
#             pass
#         elif(dice_roll == 20):
#             pass
#         else:
#             pass
#             i = random.choice(range(len(defaultFileArr)))
#             riff = defaultFileArr[i]
#             ps.playsound(riff)
#             soundsPlayed.append(riff)
#             if(len(defaultFileArr) == 1):
#                 defaultFileArr = soundsPlayed
#                 soundsPlayed = []
#                 print("Deleted: ", str(riff))
#                 print("Reset sounds")
#             else:
#                 del defaultFileArr[i]
#                 print("Deleted:", str(riff))    
