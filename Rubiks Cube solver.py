from select import KQ_NOTE_RENAME


# kubus=[
# ["YBO","GR","RYG","GW","WBR","OB","GOW","WR"],
# ["BY","O","GO","B","YO","R", "BR","G"],
# ["YOG","YG","BYR","RY","WOB","OW","GWR","BW"]
# ]

# begin toestand van een kubus
kubus=[
["WGO","WO","WOB","WB","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]

def wisselChar(tekst, van, naar):
	character = tekst[van]
	temp = list(tekst) 
	temp[naar] = character
	tekst = "".join(temp)
	return tekst

def draaiF(kubus):
    #  we moeten een deepcopy maken van een array, dus kubusCopy=kubus werkt niet
	# want alleen de blokjes die beinvloedt worden door de draai, moeten wijzigen. De andere blokjes moeten 
	# hetzelfde blijven als de oorspronkelijke kubus.

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]
# 	# een lege rij van rijen is handig om te zien dat sommige blokjes niet wijzgen:
# 	kubusCopy=[
# ["old","old","old","old","old","old","old","old"],
# ["old","old","old","old","old","old" ,"old","old"],
# ["old","old","old","old","old","old","old","old"]
# ]
	# kubus[0,0]=kubus[0,2]
	# 0 positie van de string op 1 komt
	# 1 positie van de string op 2 komt
	# 2 positie van de string op 0 komt
	# is gelijk aan + 2 mod 3
	b0=kubus[0][2][2]
	b1=kubus[0][2][0]
	b2=kubus[0][2][1]
	kubusCopy[0][0]=b0+b1+b2

	b0=kubus[1][2][1]
	b1=kubus[1][2][0]
	kubusCopy[0][1]=b0+b1
 
	b0=kubus[2][2][2]
	b1=kubus[2][2][0]
	b2=kubus[2][2][1]
	kubusCopy[0][2]=b0+b1+b2
	
 
	kubusCopy[1][0]=kubus[0][1]
 
	kubusCopy[1][1]=kubus[1][1]
 
	kubusCopy[1][2]=kubus[2][1]
 
	b0=kubus[0][0][2]
	b1=kubus[0][0][0]
	b2=kubus[0][0][1]
	kubusCopy[2][0]=b0+b1+b2
	
	b0=kubus[1][0][1]
	b1=kubus[1][0][0]
	kubusCopy[2][1]=b0+b1
 
	kubusCopy[2][2]=kubus[2][0]
	
	return kubusCopy

#doorloop kubus en kijk waar "OW" of "WO" zich bevindt
for kubusLaag in range(0,3):
	print("")
	print('laag '+str(kubusLaag))
	for indexPositieInLaag in range(0,8):
		print (kubus[kubusLaag][indexPositieInLaag], end = ' ')  # print on same line
print("")

kubus=draaiF(kubus)
kubus=draaiF(kubus)
kubus=draaiF(kubus)

print("***************************************************")
for kubusLaag in range(0,3):
	print("")
	print('laag '+str(kubusLaag))
	for indexPositieInLaag in range(0,8):
		print (kubus[kubusLaag][indexPositieInLaag], end = ' ')  # print on same line
print("")



# for kubusLaag in range(0,2):
# 	for indexPositieInLaag in range(0,7):
# 		if kubusLaag==0 and indexPositieInLaag==1:
# 			if kubus[kubusLaag, indexPositieInLaag]== "WO":
# 				None
# 			if kubus[kubusLaag, indexPositieInLaag]== "OW":
# 				draaiF()
# 				draaiUinv()
# 				draaiF()
# 				draaiU() #zet oranje weer voor

def draaiUinv():
	for indexPositieInLaag in range(0,7):
		kubus[0][indexPositieInLaag]=kubus[0,][(indexPositieInLaag-2) %7]

def draaiU():
	for indexPositieInLaag in range(0,7):
		kubus[0][indexPositieInLaag]=kubus[0][(indexPositieInLaag+2) %7]

	
exit()
 

				
# vergelijk een plekje op de kubus met "OW" of "WO" (kubuslaag, 
# indexPositieInLaag )

# vergelijk een plekje op de kubus met "OW" of "WO" (i,j):
		# if  kubus[i,j]=="WO":
		# # voer een oplossing algortime 1 uit om i,j op 1,2 te krijgen (i,j)
		# if kubus[i,j]=="OW":
		# voer een oplossing algortime 2 uit om i,j op 1,2 te krijgen (i,j)


# voer een oplossing algortime 1 uit om i,j op 1,2 te krijgen (i,j):
	# if i=0 and j = 2 :
		# U’   #zie mijn bijlage voor de uitleg van de beweging
             
# voer een oplossing algortime 2 uit om i,j op 1,2 te krijgen (i,j):
# 	blbalab

# U’:  #kubus upper vlak 1 slag tegen de klok in draaien
	# for indexPositieInLaag  = 0 to 7:
	# kubus[1,indexPositieInLaag ]=kubus[0,(indexPositieInLaag-2) modulo 7]
