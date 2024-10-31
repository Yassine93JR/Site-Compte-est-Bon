# Créé par YassineHABA, le 10/01/2022 en Python 3.7
from random import*
liste=[1,2,3,4,5,6,7,8,9,10,25,50,75,100]
liste1=[]
for i in range(6):
    liste1.append(choice(liste))
print("Plaquettes=",liste1,end=' ')

nb=randrange(101,1000)

#fenetre pricipale de l'interface graphique
import tkinter as tk
fenetre=tk.Tk()
fenetre.title("LE COMPTE EST BON")
fenetre.configure(bg= 'blue')
fenetre.geometry("700x300+210+210")

def ajouta():
    #global lis
    lis.append(int(btna["text"]))
    btna["bg"]="red"
def ajoutb():
    lis.append(int(btnb["text"]))
    btnb["bg"]="red"
def ajoutc():
    lis.append(int(btnc["text"]))
    btnc["bg"]="red"
def ajoutd():
    lis.append(int(btnd["text"]))
    btnd["bg"]="red"
def ajoute():
    lis.append(int(btne["text"]))
    btne["bg"]="red"
def ajoutf():
    lis.append(int(btnf["text"]))
    btnf["bg"]="red"
def ajoutA():
    lis.append(int(btnA["text"]))
    btnA["bg"]="red"
def ajoutB():
    lis.append(int(btnB["text"]))
    btnB["bg"]="red"
def ajoutC():
    lis.append(int(btnC["text"]))
    btnC["bg"]="red"
def ajoutD():
    lis.append(int(btnD["text"]))
    btnD["bg"]="red"
def ajoutE():
    lis.append(int(btnE["text"]))
    btnE["bg"]="red"

def ajout1():
    #global lis
    lis.append((btn1["text"]))
def ajout2():
    lis.append((btn2["text"]))
def ajout3():
    lis.append((btn3["text"]))
def ajout4():
    lis.append((btn4["text"]))

def calc():
    global lis
    if lis[2]=="+":
        d=(lis[0]+lis[1])
    if lis[2]=="X":
        d=(lis[0]*lis[1])
    if lis[2]=="-":
        d=(lis[0]-lis[1])
    if lis[2]=="/":
        d=(lis[0]/lis[1])
    if d==nb:
        texte1["text"]="bravo!!"
    if btnA["text"]=="":
        btnA["text"]=str(d)
    elif btnB["text"]=="":
        btnB["text"]=str(d)
    elif btnC["text"]=="":
        btnC["text"]=str(d)
    elif btnD["text"]=="":
        btnD["text"]=str(d)
    elif btnE["text"]=="":
        btnE["text"]=str(d)
        texte1["text"]="dommage tu  !n' est pas loin"

    lis=[]

lis=[]

texte1=tk.Label(fenetre,text="Bienvenue dans le compte est bon",bg="blue",fg="white",font=("Arial",16,"bold"))
texte1.pack()

btn0 = tk.Button(fenetre,text=str(nb),bg="yellow",font=("Arial",26,"bold"),padx = 30,pady = 10)
btn0.pack(side=tk.TOP)



btna = tk.Button(fenetre,text=str(liste1[0]),padx = 10,pady = 10,command=ajouta)
btnb = tk.Button(fenetre,text=str(liste1[1]),padx = 10,pady = 10,command=ajoutb)
btnc = tk.Button(fenetre,text=str(liste1[2]),padx = 10,pady = 10,command=ajoutc)
btnd = tk.Button(fenetre,text=str(liste1[3]),padx = 10,pady = 10,command=ajoutd)
btne = tk.Button(fenetre,text=str(liste1[4]),padx = 10,pady = 10,command=ajoute)
btnf = tk.Button(fenetre,text=str(liste1[5]),padx = 10,pady = 10,command=ajoutf)
btnA = tk.Button(fenetre,text="",padx = 10,pady = 10,command=ajoutA)
btnB = tk.Button(fenetre,text="",padx = 10,pady = 10,command=ajoutB)
btnC = tk.Button(fenetre,text="",padx = 10,pady = 10,command=ajoutC)
btnD = tk.Button(fenetre,text="",padx = 10,pady = 10,command=ajoutD)
btnE = tk.Button(fenetre,text="",padx = 10,pady = 10,command=ajoutE)

btna.pack(side=tk.LEFT)
btnb.pack(side=tk.LEFT)
btnc.pack(side=tk.LEFT)
btnd.pack(side=tk.LEFT)
btne.pack(side=tk.LEFT)
btnf.pack(side=tk.LEFT)
btnA.pack(side=tk.LEFT)
btnB.pack(side=tk.LEFT)
btnC.pack(side=tk.LEFT)
btnD.pack(side=tk.LEFT)
btnE.pack(side=tk.LEFT)


#Button
btn1 = tk.Button(fenetre,text = "+",padx = 15,pady =15,command=ajout1)
btn2 = tk.Button(fenetre,text = "-",padx = 15,pady = 15,command=ajout2)
btn3 = tk.Button(fenetre,text = "/",padx = 15,pady = 15,command=ajout3)
btn4 = tk.Button(fenetre,text = "X",padx = 15,pady =15,command=ajout4)
btn6 = tk.Button(fenetre,text = "Calculer",command= calc,padx = 10,pady = 10)
btn5 = tk.Button(fenetre,text = "Quitter",command= fenetre.destroy,padx = 10,pady = 10)




btn1.pack(side=tk.RIGHT)
btn2.pack(side=tk.RIGHT)
btn3.pack(side=tk.RIGHT)
btn4.pack(side=tk.RIGHT)
btn5.pack(side=tk.BOTTOM)
btn6.pack(side=tk.BOTTOM)

fenetre.mainloop()
