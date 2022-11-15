from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('Encode-Decode')

message = StringVar()
key = StringVar()
mode = StringVar()
result1 = StringVar()
result2 = StringVar()


# functions

def startenc():
    psswrd = key.get()
    secret = message.get()
    result1.set(encodefunc(secret, psswrd))
    Label(text='Encrypted text:', font='arial 8 bold', ).place(x=35, y=250)
    key.set("")
    message.set("")


def startdec():
    psswrd = key.get()
    secret = result1.get()
    result2.set(decodefunc(secret, psswrd))
    Label(text='Decrypted text:', font='arial 8 bold', ).place(x=35, y=320)


def encodefunc(secret, psswrd):
    lst = []
    for i in range(len(secret)):
        flag = psswrd[i % len(psswrd)]
        new = (ord(secret[i]) + ord(flag)) % 256
        lst.append(chr(new))
    encstring = ''.join(lst)
    return encstring


def decodefunc(secret, psswrd):
    if psswrd == key.get():
        lst1 = []
        for i in range(len(secret)):
            flag1 = psswrd[i % len(psswrd)]
            new1 = (256 + ord(secret[i]) - ord(flag1)) % 256
            lst1.append(chr(new1))
        decstring = ''.join(lst1)
        return decstring


def exitfunc():
    root.destroy()


def resetfunc():
    message.set("")
    key.set("")
    mode.set("")
    result1.set("")
    result2.set("")


# labels and buttons

Button(root, text='Encode', font='arial 12 bold', command=startenc).place(x=80, y=395)
Button(root, text='Decode', font='arial 12 bold', command=startdec).place(x=180, y=395)
Button(root, text='Reset', font='arial 12 bold', command=resetfunc).place(x=275, y=395)
Button(root, text='Exit', font='arial 12 bold', command=exitfunc).place(x=375, y=395)

Label(text='ENCODE DECODE', font='arial 20 bold').place(x=120, y=40)
Label(text='kKaya', font='arial 10 italic').place(x=195, y=450)

Label(text='MESSAGE', font='arial 10 bold', ).place(x=35, y=150)
Label(text='KEY', font='arial 10 bold', ).place(x=35, y=200)

Entry(textvariable=message, width=55).place(x=120, y=150)
Entry(textvariable=key, width=55).place(x=120, y=200)

Entry(textvariable=result1, bd=8, width=70).place(x=28, y=270)
Entry(textvariable=result2, bd=8, width=70).place(x=28, y=340)

root.mainloop()