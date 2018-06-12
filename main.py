import funkcje
from tkinter import *
from tkinter import filedialog
global tekst

okno = Tk ()
#print(font.families())
okno.title("Program szyfrujacy")
okno.geometry("750x450+500+300")
okno.configure(background = "#78B648")

topFrame = Frame(okno)
topFrame.pack()
bottomFrame= Frame(okno)
bottomFrame.pack(side=BOTTOM)

#Etykieta
etykieta1= Label(okno, text= "Wpisz tekst do zaszyfrowania/odszyfrowania:",font=("Myriad Pro",16,"italic"), bg="#295F00", fg="#F7F8F7")
etykieta1.pack()
etykieta1.pack(expand=NO)

def browsefunc():
	global tekst
	while True:
		filename = filedialog.askopenfilename()
		if (filename):
			break;
	pathlabel.config(text=filename)
	tekst = funkcje.wczytajPlik(filename)
	poletekstowe.insert('1.0', tekst)

def b1Click():
	global tekst
	tekst = poletekstowe.get('1.0', END)
	funkcje.cezar(tekst)	
	tekst = funkcje.wczytajPlik("zaszyfrowane.txt")
	poletekstowe.delete('1.0', END)
	poletekstowe.insert('1.0', tekst)

def b2Click():
	global tekst
	tekst = poletekstowe.get('1.0', END)
	funkcje.antyCezar(tekst)	
	tekst = funkcje.wczytajPlik("odszyfrowane.txt")
	poletekstowe.delete('1.0', END)
	poletekstowe.insert('1.0', tekst)

def b3Click():
	global tekst
	tekst = poletekstowe.get('1.0', END)
	funkcje.polibiusz(tekst)	
	tekst = funkcje.wczytajPlik("zaszyfrowaneP.txt")
	poletekstowe.delete('1.0', END)
	poletekstowe.insert('1.0', tekst)

def b4Click():
	global tekst
	tekst = poletekstowe.get('1.0', END)
	funkcje.antyPolibiusz(tekst)
	tekst = funkcje.wczytajPlik("odszyfrowaneP.txt")
	poletekstowe.delete('1.0', END)
	poletekstowe.insert('1.0', tekst)

#Przyciski
przycisk1=Button (topFrame, text= "Szyfruj Cezarem",command =lambda: b1Click(), font=("Myriad Pro", 12, "italic"), fg="#F7F8F7", bg="#295F00",pady=5,padx=5)
przycisk2=Button (topFrame, text= "Deszyfruj Cezarem",command =lambda: b2Click(),font=("Myriad Pro", 12, "italic"), fg="#295F00", bg="#F7F8F7",pady=5, padx=5)
przycisk3=Button (topFrame, text= "Szyfruj Polibiuszem",command =lambda:b3Click(),font=("Myriad Pro", 12, "italic"), fg="#F7F8F7", bg="#295F00",pady=5,padx=5)
przycisk4=Button (topFrame, text= "Deszyfruj Polibiuszem",command =lambda:b4Click(),font=("Myriad Pro", 12, "italic"), fg="#295F00", bg="#F7F8F7",pady=5,padx=5)
przycisk5 = Button(okno, text="Wybierz plik",font=("Myriad Pro", 12, "italic"), fg="#F7F8F7", bg="#295F00", command=browsefunc)

przycisk1.pack(side=LEFT)
przycisk2.pack(side=LEFT)
przycisk3.pack(side=LEFT)
przycisk4.pack(side=LEFT)

#Pole tekstowe
poletekstowe=Text(okno, width=70,height=20,bg="#A6FB64",fg="#295F00")
poletekstowe.pack()
przycisk5.pack()

pathlabel = Label(okno)
pathlabel.pack()
pathlabel.config(text="Nie wybrano pliku")

okno.mainloop()