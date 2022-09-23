import playsound as ps
import glob
import random
import datetime
import keyboard
from tkinter import *

root = Tk()
root.title('Bardic Dice Roller')
root.iconbitmap()
root.geometry("500x500")

#Get the dice number
def get_number(x):
    if x == "\u2680":
        return(1)
    elif x == "\u2681":
        return(2)
    elif x == "\u2682":
        return(3)
    elif x == "\u2683":
        return(4)
    elif x == "\u2684":
        return(5)
    elif x == "\u2685":
        return(6)

#Roll the dice
def roll_dice():
    #roll random dice
    d1 = random.choice(dice_list)

    #determine dice number
    sd1 = get_number(d1)

    #update labels
    dice_label1.config(text = d1)

    #Update sub dice labels
    sub_dice_label1.config(text=sd1)

    #Update total label
    total = sd1
    total_label.config(text = f"You rolled: {total}")

#Create a Dice List
dice_path = glob.glob(r"C:\Users\agn_a\Desktop\Projects\Soundboard\Dice" + "/*.jpg", recursive=True)
dice_list = []
for i in dice_path:
    dice_list.append(i)
print(dice_list)

#my_dice = ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]

#Create a frame
my_frame = Frame(root)
my_frame.pack(pady = 20)

#create dice labels
dice_label1 = Label(my_frame, text = '', font = ("Helvetica", 100), fg = "black")
dice_label1.grid(row = 0, column = 0, padx = 5)
sub_dice_label1 = Label(my_frame, text = "")
sub_dice_label1.grid(row = 1, column = 0)

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
