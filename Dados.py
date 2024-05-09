from tkinter import*
from PIL import ImageTk, Image
import random

window=Tk()
window.title("Dados")
window.geometry("500x500")

img = ImageTk.PhotoImage(Image.open("dice.jpg"))

lbl1 = Label( window , text="Jugador 1", fg="red")
lbl1.place(relx= 0.1 , rely= 0.3, anchor = CENTER)

player_1_score_label = Label(window , bg ="red", fg ="white")
player_1_score_label.place(relx= 0.1 , rely= 0.4 , anchor= CENTER)

random_dice_label = Label(window , bg = "chocolate1" , fg ="white")
random_dice_label.place(relx= 0.5 , rely= 0.5 , anchor= CENTER)

player1_score = 0
def player1():

    global player1_score

    random_no = random.randint(1,6)
    random_dice_label["text"] = random_no

    player1_score = player1_score + random_no
    player_1_score_label["text"] = str(player1_score)

player_1_btn = Button(window, image = img, command = player1)
player_1_btn.place(relx= 0.1 , rely= 0.7 , anchor = CENTER)


lbl2 = Label( window , text="Jugador 2", fg="blue")
lbl2.place(relx= 0.9 , rely= 0.3, anchor = CENTER)

player_2_score_label = Label(window , bg ="blue", fg ="white")
player_2_score_label.place(relx= 0.9 , rely= 0.4 , anchor= CENTER)

player2_score = 0
def player2():

    global player2_score

    random_no = random.randint(1,6)
    random_dice_label["text"] = random_no

    player2_score = player2_score + random_no
    player_2_score_label["text"] = str(player2_score)

player_2_btn = Button(window, image = img, command = player2)
player_2_btn.place(relx= 0.9 , rely= 0.7 , anchor = CENTER)

Ganador1 = Label( window ,bg="white", fg="black", font=20)
#Ganador1.place(relx= 0.2 , rely= 0.2, anchor = CENTER)


def Ganador():
    if player1_score > player2_score:
        Ganador1["text"]="Jugador1 Ganaste¡¡¡"
        print("jugador 1 ganaste¡¡¡", player1_score)
    elif player2_score > player1_score:
        Ganador1["text"]="Jugador2 Ganaste¡¡¡"
        print("jugador 2 ganaste¡¡¡", player2_score)
    else:
        Ganador1["text"]="Empate???"
        print("EMPATE???")

Ganador1.place(relx= 0.5 , rely= 0.2, anchor = CENTER)

btn = Button(window, text="Ganador??", command=Ganador)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

window.mainloop()