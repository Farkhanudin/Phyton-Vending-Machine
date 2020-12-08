import tkinter as tk
from tkinter import *
import random
import time
root = Tk()
root.geometry("1300x600+0+0")
root.title("ITB Vending Machine")
root.configure(bg='Navajo white')
lbl_title = tk.Label(root,text="Welcome to the ITB Vending Machine. Please input your balance and select your item.",font=('arial', 23, 'bold'),bg = 'Navajo white')
lbl_title.pack()

text_Input = IntVar()
operator = ""

#==================================Setting the Frame=======================================


Tops = Frame(root, width=1600, height=50, bg="Navajo White", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1200, height=700, bg="Navajo White", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bg="Navajo White",relief=SUNKEN)
f2.pack(side=RIGHT)

#==================================Time=======================================

localtime = time.asctime(time.localtime(time.time()))


#==================================System Information=======================================

lblInfo = Label(Tops, font=('simplifica', 50, 'bold'), text="ITB Vending Machine",bg="light salmon",fg="black", bd=16, anchor='w')
lblInfo.grid(row=0, column=0)


def Total():
    AmtOfFanta = (int(Fanta.get()))
    AmtOfCoke = (int(Coke.get()))
    AmtOfSprite = (int(Sprite.get()))
    AmtOfPepsi = (int(Pepsi.get()))
    AmtOfSaldoAwal =(int(InitialBalance.get()))

    CostOfFanta = AmtOfFanta * 500
    CostOfCoke = AmtOfCoke * 700
    CostOfSprite = AmtOfSprite * 600
    CostOfPepsi = AmtOfPepsi * 400


    CostOfMeal =str("Rp." + str((CostOfFanta + CostOfCoke + CostOfSprite + CostOfPepsi)))

    txtCost.insert('0',CostOfMeal)

def Kembalian():
    AmtOfFanta = (int(Fanta.get()))
    AmtOfCoke = (int(Coke.get()))
    AmtOfSprite = (int(Sprite.get()))
    AmtOfPepsi = (int(Pepsi.get()))
    AmtOfSaldoAwal =(int(InitialBalance.get()))

    CostOfFanta = AmtOfFanta * 500
    CostOfCoke = AmtOfCoke * 700
    CostOfSprite = AmtOfSprite * 600
    CostOfPepsi = AmtOfPepsi * 400
    total=int(AmtOfSaldoAwal*0.1)-(CostOfFanta + CostOfCoke + CostOfSprite + CostOfPepsi)
    if total>=0:
        kembali = ("Rp."+str(total))
    else:
        kembali="saldo tidak mencukupi"
    txtFinalBalance.insert(0,kembali)


def Reset():
    Fanta.set(0)
    Coke.set(0)
    Sprite.set(0)
    Pepsi.set(0)
    InitialBalance.set(0)
    Cost.set(0)
    FinalBalance.set(0)

#-------------------

Fanta=IntVar()
Coke=IntVar()
Sprite=IntVar()
Pepsi=IntVar()

lblFanta = Label(f1, font=('arial', 16, 'bold'), text='Fanta:Rp.5000',bg = 'light salmon',bd=19,anchor='w')
lblFanta.grid(row=6,column=0)
txtFanta = Entry(f1,font=('arial',16,'bold'),textvariable=Fanta,bd=10,insertwidth=4,
                bg='dark salmon',justify='right')
txtFanta.grid(row=6,column=1)

lblCoke= Label(f1, font=('arial', 16, 'bold'), text='Coke:7000', bg = 'light salmon',bd=16,anchor='w')
lblCoke.grid(row=7,column=0)
txtCoke = Entry(f1,font=('arial',16,'bold'),textvariable=Coke,bd=10,insertwidth=4,
                bg='dark salmon',justify='right')
txtCoke.grid(row=7,column=1)

lblSprite = Label(f1, font=('arial', 16, 'bold'), text='Sprite:Rp.6000', bg = 'light salmon',bd=19,anchor='w')
lblSprite.grid(row=8,column=0)
txtSprite = Entry(f1,font=('arial',16,'bold'),textvariable=Sprite,bd=10,insertwidth=4,
                bg='dark salmon',justify='right')
txtSprite.grid(row=8,column=1)

lblPepsi = Label(f1,font=('arial',16,'bold'), text="Pepsi:Rp.4000", bg = 'light salmon',bd=19, anchor='w')
lblPepsi.grid(row=9, column=0)
txtPepsi = Entry(f1,font=('arial',16,'bold'),textvariable=Pepsi,bd=10,insertwidth=4,
                bg='dark salmon',justify='right')
txtPepsi.grid(row=9,column=1)

#==================================Balance, Cost=======================================

InitialBalance=IntVar()
Cost=IntVar()
FinalBalance=IntVar()

lblInitialBalance = Label(f1,font=('arial',20,'bold'), text="Saldo Awal", bg = 'light salmon', bd=10, anchor='w')
lblInitialBalance.grid(row=2, column=0)
txtInitialBalance=Entry(f1,font=('arial',20,'bold'), textvariable=InitialBalance, bd=20, insertwidth=4,
                   bg='dark salmon', justify='right')
txtInitialBalance.grid(row=2, column=1)

lblCost = Label(f1,font=('arial',20,'bold'), text="Total Belanja ", bg = 'light salmon',bd=10, anchor='w')
lblCost.grid(row=8, column=5)
txtCost=Entry(f1,font=('arial',20,'bold'), textvariable=Cost, bd=20, insertwidth=4,
                   bg='dark salmon', justify='right')
txtCost.grid(row=8, column=6)

lblFinalBalance = Label(f1,font=('arial',20,'bold'), text="Kembalian", bg = 'light salmon',bd=20, anchor='w')
lblFinalBalance.grid(row=9, column=5)
txtFinalBalance=Entry(f1,font=('arial',20,'bold'), textvariable=FinalBalance, bd=20, insertwidth=4,
                   bg='dark salmon', justify='right')
txtFinalBalance.grid(row=9, column=6)

#==================================More Buttons=======================================

btnTotal = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=6,text="Total",bg="light salmon",
                  command=Total).grid(row=11,column=1)

btnReset = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=6,text="Reset",bg="light salmon",
                  command=Reset).grid(row=11,column=6)

btnKembalian = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=6,text="Kembalian",bg="light salmon",
                  command=Kembalian).grid(row=11,column=2)
#--------------------------------------------------------------

root.mainloop()







