import playsound as ps
import glob
import random
import datetime
import keyboard
from tkinter import *
from PIL import Image
from PIL import ImageTk

global defaultFileArr, soundsPlayed, test
defaultFileArr, soundsPlayed, test = [], [], []

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
    if x == 'C:\\Users\\agn_a\\Desktop\\Projects\\Soundboard\\bardMusicalDiceRoller\\Soundboard\\Dice\\1.png':
        return(1)
    elif x == 'C:\\Users\\agn_a\\Desktop\\Projects\\Soundboard\\bardMusicalDiceRoller\\Soundboard\\Dice\\2.png':
        return(2)
    elif x == 'C:\\Users\\agn_a\\Desktop\\Projects\\Soundboard\\bardMusicalDiceRoller\\Soundboard\\Dice\\3.png':
        return(3)
    elif x == 'C:\\Users\\agn_a\\Desktop\\Projects\\Soundboard\\bardMusicalDiceRoller\\Soundboard\\Dice\\4.png':
        return(4)
    elif x == 'C:\\Users\\agn_a\\Desktop\\Projects\\Soundboard\\bardMusicalDiceRoller\\Soundboard\\Dice\\5.png':
        return(5)


def playRiff(d1):
    if(get_number(d1) == 1):
        pass
    elif(get_number(d1) == 20):
        pass
    else:
        print(random.choice(range(len(test))))
        i = random.choice(range(len(defaultFileArr)))
        riff = defaultFileArr[i]
        ps.playsound(riff)
        soundsPlayed.append(riff)
        if(len(defaultFileArr) == 1):
            for i in soundsPlayed:
                defaultFileArr.append(i)
            del defaultFileArr[0]
            for i in range(len(soundsPlayed)):
                del soundsPlayed[i]
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
    image = Image.open(d1)
    image = image.resize((500,500))
    img =  ImageTk.PhotoImage(image)
    dice_label1.image = img
    dice_label1.config(image = img)

    #Update total label
    total_label.config(text = f"You rolled a {get_number(d1)}!!!")
    
    playRiff(d1)

#Create a Dice List
dicejpgs = glob.glob(r"C:\Users\agn_a\Desktop\Projects\Soundboard\bardMusicalDiceRoller\Soundboard\Dice" + "/*.png", recursive=True)
my_dice = []
for jpg in dicejpgs:
    my_dice.append(jpg)


#Create a frame
my_frame = Frame(root)
my_frame.pack(pady = 20)

#create dice labels
image = Image.open(r"C:\Users\agn_a\Desktop\Projects\Soundboard\bardMusicalDiceRoller\Soundboard\Dice\1.png")
image = image.resize((500,500))
img =  ImageTk.PhotoImage(image)

dice_label1 = Label(my_frame, image = img, text = '', font = ("Helvetica", 100), fg = "black")
dice_label1.grid(row = 0, column = 0, padx = 5)
dice_label1.image = img

#create Roll button
my_button = Button(root, text = "Roll Dice", command = roll_dice, font = ("Helvetica", 24))
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
