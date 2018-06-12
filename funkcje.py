def wczytajPlik(sciezka):
    plik = open(sciezka)
    try:
        tekst = plik.read()
    finally:
        plik.close()

    return tekst

def cezar(tekst):
    plik = open('zaszyfrowane.txt', 'w')

    for letter in tekst:
        if(letter.isalpha()):
            a=ord(letter)
            if(letter=='x'):
                a=ord('a')
            elif(letter=="X"):
                a=ord("A")
            elif(letter=='y'):
                a=ord('b')
            elif(letter=='Y'):
                a=ord('B')
            elif(letter=='z'):
                a=ord('c')
            elif(letter=='Z'):
                a=ord('C')
            else:
                a+=3
            plik.write(chr(a))
        else:
            plik.write(letter)

    plik.close()

def antyCezar(tekst):
	plik = open('odszyfrowane.txt', 'w')

	for letter in tekst:
		if(letter.isalpha()):
			a=ord(letter)
			if(letter=='a'):
			    a=ord('x')
			elif(letter=="A"):
			    a=ord("X")
			elif(letter=='b'):
			    a=ord('y')
			elif(letter=='B'):
			    a=ord('Y')
			elif(letter=='c'):
			    a=ord('z')
			elif(letter=='C'):
			    a=ord('Z')
			else:
			    a-=3
			plik.write(chr(a))
		else:
			plik.write(letter)

	plik.close()

def polibiusz(tekst):
	indexy = [11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
	tab =[]
	for i in range(26):
			tab.append(ord('A')+i)
	tab.remove(ord('J'))

	plik = open('zaszyfrowaneP.txt', 'w')
	tekst =tekst.upper()

	for letter in tekst:
		if(letter.isalpha()):
			if(letter == 'J'):
					plik.write('24::')
			counter=0
			for alfa in tab:
				counter+=1
				if(chr(alfa) == letter):
					plik.write(str(indexy[counter-1])+"::")
				
		else:
			plik.write(letter+"::")

	plik.close()

def antyPolibiusz(tekst):
	indexy = [11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]
	tab =[]
	for i in range(26):
			tab.append(ord('A')+i)
	tab.remove(ord('J'))
	plik = open('odszyfrowaneP.txt', 'w')
	tekst = tekst.split(" ")
	
	for item in tekst:
		item = item.split("::")

		for x in item:
			#plik.write(x+"\n")
			if(x.isnumeric()):
				counter=0
				for inx in indexy:
					counter+=1
					if(str(inx) == x):
						plik.write(chr(tab[counter-1]))
			else:
				plik.write(x)
		plik.write(" ")
		
	plik.close()

