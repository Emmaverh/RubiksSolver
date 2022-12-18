# kubus=[
# ["YBO","GR","RYG","GW","WBR","OB","GOW","WR"],
# ["BY","O","GO","B","YO","R", "BR","G"],
# ["YOG","YG","BYR","RY","WOB","OW","GWR","BW"]
# ]

# begin toestand van een kubus
#kubus=[
#["WBR","BW","OYB","BY","WRG","GY","GOW","YO"],
#["GO","O","RW","B","OB","R","GR","G"],
#["WGO","YR","BYR","WO","RYG","RB","BWO","WG"]	
#]

#kubus=[
#["OGY","WG","GWR","WB","YBO","GO","YRB","RB"],
#["GY","O","RW","B","RY","R","WO","G"],
#["BWO","GR","WGO","BY","WBR","YO","RYG","OB"]	
#]

#kubus=[
#["GWR","RY","BWO","RB","OGY","RW","YGR","YO"],
#["WB","O","GW","B","GR","R","OB","G"],
#["YBO","YB","YRB","YG","WGO","GO","RWB","OW"]	
#]

#kubus=[
#["OBW","BR","GWR","OB","BYR","OY","RYG","RY"],
#["RW","O","BY","B","YG","R","BW","G"],
#["RWB","RG","WGO","OG","OGY","OW","YBO","GW"]	
#]

#kubus=[
#["RBY","BO","OBW","GW","BOY","YB","YGR","OY"],
#["WB","O","GY","B","GR","R","GO","G"],
#["WGO","YR","WRG","RW","YOG","BR","BRW","WO"]	
#]

kubus=[
["BYR","YB","OGY","GO","BOY","RB","WOB","RG"],
["BW","O","GY","B","OB","R","WG","G"],
["WBR","YO","WGO","WR","GRY","RY","GWR","WO"]	
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

def draaiFinv(kubus):


	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]

	b0=kubus[2][0][1]
	b1=kubus[2][0][2]
	b2=kubus[2][0][0]
	kubusCopy[0][0]=b0+b1+b2

	kubusCopy[0][1]=kubus[1][0]
 
	b0=kubus[0][0][1]
	b1=kubus[0][0][2]
	b2=kubus[0][0][0]
	kubusCopy[0][2]=b0+b1+b2
	
	b0=kubus[2][1][1]
	b1=kubus[2][1][0]
	kubusCopy[1][0]=b0+b1
 
	kubusCopy[1][1]=kubus[1][1]
 
	b0=kubus[0][1][1]
	b1=kubus[0][1][0]
	kubusCopy[1][2]=b0+b1
 
	kubusCopy[2][0]=kubus[2][2]
	
	kubusCopy[2][1]=kubus[1][2]
 
	b0=kubus[0][2][1]
	b1=kubus[0][2][2]
	b2=kubus[0][2][0]
	kubusCopy[2][2]=b0+b1+b2
	
	return kubusCopy

def draaiL(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	b0=kubus[0][4][2]
	b1=kubus[0][4][0]
	b2=kubus[0][4][1]
	kubusCopy[0][2]=b0+b1+b2

	b0=kubus[1][4][1]
	b1=kubus[1][4][0]
	kubusCopy[0][3]=b0+b1
 
	b0=kubus[2][4][2]
	b1=kubus[2][4][0]
	b2=kubus[2][4][1]
	kubusCopy[0][4]=b0+b1+b2
	
 
	kubusCopy[1][2]=kubus[0][3]
 
	kubusCopy[1][3]=kubus[1][3]
 
	kubusCopy[1][4]=kubus[2][3]
 
	kubusCopy[2][2]=kubus[0][2]
	
	b0=kubus[1][2][1]
	b1=kubus[1][2][0]
	kubusCopy[2][3]=b0+b1
 
	b0=kubus[2][2][2]
	b1=kubus[2][2][0]
	b2=kubus[2][2][1]
	kubusCopy[2][4]=b0+b1+b2
	
	return kubusCopy

def draaiLinv(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	kubusCopy[0][2]=kubus[2][2]

	kubusCopy[0][3]=kubus[1][2]
 
	b0=kubus[0][2][1]
	b1=kubus[0][2][2]
	b2=kubus[0][2][0]
	kubusCopy[0][4]=b0+b1+b2
	
	b0=kubus[2][3][1]
	b1=kubus[2][3][0]
	kubusCopy[1][2]=b0+b1
 
	kubusCopy[1][3]=kubus[1][3]
 
	b0=kubus[0][3][1]
	b1=kubus[0][3][0]
	kubusCopy[1][4]=b0+b1
 
	b0=kubus[2][4][1]
	b1=kubus[2][4][2]
	b2=kubus[2][4][0]
	kubusCopy[2][2]=b0+b1+b2
	
	kubusCopy[2][3]=kubus[1][4]
 
	b0=kubus[0][4][1]
	b1=kubus[0][4][2]
	b2=kubus[0][4][0]
	kubusCopy[2][4]=b0+b1+b2
	
	return kubusCopy

def draaiB(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	kubusCopy[0][4]=kubus[2][4]

	kubusCopy[0][5]=kubus[1][4]
 
	b0=kubus[0][4][1]
	b1=kubus[0][4][2]
	b2=kubus[0][4][0]
	kubusCopy[0][6]=b0+b1+b2
	
	b0=kubus[2][5][1]
	b1=kubus[2][5][0]
	kubusCopy[1][4]=b0+b1
	
 
	kubusCopy[1][5]=kubus[1][5]

	b0=kubus[0][5][1]
	b1=kubus[0][5][0]
	kubusCopy[1][6]=b0+b1

	b0=kubus[2][6][1]
	b1=kubus[2][6][2]
	b2=kubus[2][6][0]
	kubusCopy[2][4]=b0+b1+b2
	
	kubusCopy[2][5]=kubus[1][6]
 
	b0=kubus[0][6][1]
	b1=kubus[0][6][2]
	b2=kubus[0][6][0]
	kubusCopy[2][6]=b0+b1+b2
	
	return kubusCopy

def draaiBinv(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	b0=kubus[0][6][2]
	b1=kubus[0][6][0]
	b2=kubus[0][6][1]
	kubusCopy[0][4]=b0+b1+b2

	b0=kubus[1][6][1]
	b1=kubus[1][6][0]
	kubusCopy[0][5]=b0+b1
 
	b0=kubus[2][6][2]
	b1=kubus[2][6][0]
	b2=kubus[2][6][1]
	kubusCopy[0][6]=b0+b1+b2
	
	kubusCopy[1][4]=kubus[0][5]
	
 
	kubusCopy[1][5]=kubus[1][5]

	kubusCopy[1][6]=kubus[2][5]

	kubusCopy[2][4]=kubus[0][4]
	
	b0=kubus[1][4][1]
	b1=kubus[1][4][0]
	kubusCopy[2][5]=b0+b1
 
	b0=kubus[2][4][2]
	b1=kubus[2][4][0]
	b2=kubus[2][4][1]
	kubusCopy[2][6]=b0+b1+b2
	
	return kubusCopy

def draaiR(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	b0=kubus[0][0][2]
	b1=kubus[0][0][0]
	b2=kubus[0][0][1]
	kubusCopy[0][6]=b0+b1+b2

	b0=kubus[1][0][1]
	b1=kubus[1][0][0]
	kubusCopy[0][7]=b0+b1
 
	kubusCopy[0][0]=kubus[2][0]
	
	kubusCopy[1][6]=kubus[0][7]
	
	kubusCopy[1][7]=kubus[1][7]

	kubusCopy[1][0]=kubus[2][7]

	kubusCopy[2][6]=kubus[0][6]
	
	b0=kubus[1][6][1]
	b1=kubus[1][6][0]
	kubusCopy[2][7]=b0+b1	
	
	b0=kubus[2][6][1]
	b1=kubus[2][6][2]
	b2=kubus[2][6][0]
	kubusCopy[2][0]=b0+b1+b2
	
	return kubusCopy

def draaiRinv(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	kubusCopy[0][6]=kubus[2][6]
 
	kubusCopy[0][7]=kubus[1][6]
 
	b0=kubus[0][6][1]
	b1=kubus[0][6][2]
	b2=kubus[0][6][0]
	kubusCopy[0][0]=b0+b1+b2
	
	b0=kubus[2][7][1]
	b1=kubus[2][7][0]
	kubusCopy[1][6]=b0+b1	
	
	kubusCopy[1][7]=kubus[1][7]

	b0=kubus[0][7][1]
	b1=kubus[0][7][0]
	kubusCopy[1][0]=b0+b1	

	b0=kubus[2][0][2]
	b1=kubus[2][0][0]
	b2=kubus[2][0][1]
	kubusCopy[2][6]=b0+b1+b2
	
	kubusCopy[2][7]=kubus[1][0]
	
	kubusCopy[2][0]=kubus[0][0]
	
	return kubusCopy

def draaiD(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	b0=kubus[2][6][2]
	b1=kubus[2][6][0]
	b2=kubus[2][6][1]
	kubusCopy[2][0]=b0+b1+b2

	kubusCopy[2][1]=kubus[2][7]
 
	b0=kubus[2][0][1]
	b1=kubus[2][0][2]
	b2=kubus[2][0][0]
	kubusCopy[2][2]=b0+b1+b2
	
	kubusCopy[2][3]=kubus[2][1]
	
	kubusCopy[2][4]=kubus[2][2]

	kubusCopy[2][5]=kubus[2][3]

	kubusCopy[2][6]=kubus[2][4]
	
	kubusCopy[2][7]=kubus[2][5]
	
	return kubusCopy

def draaiDinv(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	b0=kubus[2][2][2]
	b1=kubus[2][2][0]
	b2=kubus[2][2][1]
	kubusCopy[2][0]=b0+b1+b2

	kubusCopy[2][1]=kubus[2][3]
 
	kubusCopy[2][2]=kubus[2][4]
	
	kubusCopy[2][3]=kubus[2][5]
	
	kubusCopy[2][4]=kubus[2][6]

	kubusCopy[2][5]=kubus[2][7]

	b0=kubus[2][0][1]
	b1=kubus[2][0][2]
	b2=kubus[2][0][0]
	kubusCopy[2][6]=b0+b1+b2
	
	kubusCopy[2][7]=kubus[2][1]
	
	return kubusCopy

def draaiU(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	kubusCopy[0][0]=kubus[0][6]

	kubusCopy[0][1]=kubus[0][7]
 
	kubusCopy[0][2]=kubus[0][0]
	
	kubusCopy[0][3]=kubus[0][1]
	
	kubusCopy[0][4]=kubus[0][2]

	kubusCopy[0][5]=kubus[0][3]

	kubusCopy[0][6]=kubus[0][4]
	
	kubusCopy[0][7]=kubus[0][5]
	
	return kubusCopy

def draaiUinv(kubus):
    

	# see https://stackoverflow.com/a/6533065
	# kubusCopy=kubus.deepcopy()
	kubusCopy = [row[:] for row in kubus]


	kubusCopy[0][0]=kubus[0][2]

	kubusCopy[0][1]=kubus[0][3]
 
	kubusCopy[0][2]=kubus[0][4]
	
	kubusCopy[0][3]=kubus[0][5]
	
	kubusCopy[0][4]=kubus[0][6]

	kubusCopy[0][5]=kubus[0][7]

	kubusCopy[0][6]=kubus[0][0]
	
	kubusCopy[0][7]=kubus[0][1]
	
	return kubusCopy

def kubus_oplossen(kubusFormalParameter):
	# bovenste vlak oplossen: wit kruis maken
	#zoek oranje wit (of WO) blokje
	WOgevonden=False
	OWgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  # print on same line
			# if kubus[kubusLaag][indexPositieInLaag] == "OW":
			# 	gevonden=True
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WO":
				WOgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "OW":
				OWgevonden=True
				break
		if WOgevonden:
			print("WO gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				print("WO staat al op de juiste plek") 
				break 
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai 2 keer het bovenste vlak tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het linkervlak tegen de klok in 3. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het bovenste vlak 2x met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee 2. draai het bovenste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het linker vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het linker vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het linker vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
		if OWgevonden:
			print("OW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het voorvlak met de klok mee 2. draai het bovenvlak tegen de klok in 3. draai het rechter vlak met de klok mee 4.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1.draai het bovenste vlak tegen de klok in, 2. draai het voorvlak met de klok mee 3. draai het bovenvlak tegen de klok in 4. draai het rechter vlak met de klok mee 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1.draai het bovenste vlak 2x tegen de klok in, 2. draai het voorvlak met de klok mee 3. draai het bovenvlak tegen de klok in 4. draai het rechter vlak met de klok mee 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1.draai het bovenste vlak met de klok mee 2. draai het voorvlak met de klok mee 3. draai het bovenvlak tegen de klok in 4. draai het rechter vlak met de klok mee 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het rechtervlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het linker vlak met de klok mee 3. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x tegen de klok in 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak 2x met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				print("1. draai het voor vlak 2 keer tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het voor vlak 2 keer met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het voorste vlak 2x met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het rechter vlak 2x met de klok mee 2. draai het voor vlak met de klok mee.")
				break
	return WB_of_BW_oplossen(kubusFormalParameter)
	# print("opgelost")


def WB_of_BW_oplossen(kubusFormalParameter):
    	# bovenste vlak oplossen: wit kruis maken
	#zoek oranje wit (of WO) blokje
	WBgevonden=False
	BWgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  # print on same line
			# if kubus[kubusLaag][indexPositieInLaag] == "OW":
			# 	gevonden=True
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WB":
				WBgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "BW":
				BWgevonden=True
				break
		if WBgevonden:
			print("WB gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				print("WB op de staat al juiste plek")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het achterste vlak 2x tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het rechter vlak 2x tegen de klok in 2. draai onderste vlak 2x tegen de klok in 3. draai het linker vlak 2x tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het linker vlak met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het linker vlak met de klok mee")
				break			
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het linker vlak met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het linker vlak met de klok mee")
		if BWgevonden:
			print("BW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het linker vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het achterste vlak met de klok mee 5. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in 2. draai het bovenste vlak met de klok mee 3. draai het achterste vlak met de klok mee 4.draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in 2. draai het linker vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak 2x met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het achterste vlak met de klok mee 4.draai het linker vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak 2x met de klok mee 3. draai het linker vlak 2x met de klok mee. ")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het linker vlak 2x tegen de klok in 2. draai het bovenste vlak met de klok mee 3. draai het achterste vlak met de klok mee 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het linker vlak 2x tegen de klok in.")
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het linker vlak 2x tegen de klok in.")
				break
	return WR_of_RW_oplossen(kubusFormalParameter)


def WR_of_RW_oplossen(kubusFormalParameter):
    	# bovenste vlak oplossen: wit kruis maken
	#zoek oranje wit (of WO) blokje
	WRgevonden=False
	RWgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WR":
				WRgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "RW":
				RWgevonden=True
				break
		if WRgevonden:
			print("WR gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				print("WR op de staat al juiste plek")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak 2x tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het achterste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak 2x tegen de klok in 2. draai het achterste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het achterste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in 2. draai het bovenste vlak met de klok mee 3. draai het rechter vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
		if RWgevonden:
			print("RW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het rechter vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het bovenste vlak met de klok mee 3. draai het rechter vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het achterste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het achterste vlak tegen de klok in. 5. draai het bovenste vlak met de klok mee 6. draai het rechter vlak tegen de klok in. 7. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak 2x tegen de klok in. 2. draai het bovenste vlak met de klok mee 3. draai het rechter vlak tegen de klok in. 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==7:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1.draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het achterste vlak 2x tegen de klok in")
				break
	return WG_of_GW_oplossen(kubusFormalParameter)
   
def WG_of_GW_oplossen(kubusFormalParameter):
    	# bovenste vlak oplossen: wit kruis maken
	#zoek oranje wit (of WO) blokje
	WGgevonden=False
	GWgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WG":
				WGgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "GW":
				GWgevonden=True
				break
		if WGgevonden: 	
			print("WG gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				print("WG staat al op de juiste plek")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee 2. draai het linker vlak tegen de klok in 3. draai het bovenste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het achterste vlak met de klok mee 3. draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4.draai het achterste vlak tegen de klok in. 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4.draai het achterste vlak tegen de klok in. 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4.draai het achterste vlak tegen de klok in. 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het bovenste vlak tegen de klok in. 3.draai het achterste vlak tegen de klok in. 4.draai het bovenste vlak met de klok mee.")
				break
		if GWgevonden:
			print("GW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee. 2. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het voorste vlak met de klok mee. 3. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het bovenste vlak met de klok mee. 3. draai het voorste vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee. 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee. 2. draai het linker vlak met de klok mee 3. draai het bovenste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiUinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in. 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het rechter vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het rechter vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het rechter vlak 2x tegen de klok in.")
				break
	return WGO_GOW_OWG_oplossen(kubusFormalParameter)


def WGO_GOW_OWG_oplossen(kubusFormalParameter):		
	WGOgevonden=False
	GOWgevonden=False
	OWGgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ') 
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WGO":
				WGOgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "GOW":
				GOWgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "OWG":
				OWGgevonden=True
				break
		if WGOgevonden:
			if kubusLaag==0 and indexPositieInLaag==0: 
				print ("WGO", end = ' ')  # print on same line
				print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
				print("WGO staat al goed")
				break
		if GOWgevonden or OWGgevonden:
			if GOWgevonden: print ("GOW", end = ' ')  # print on same line
			if OWGgevonden: print ("OWG", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==0: 
				while True:
					print(kubusFormalParameter[0][0])
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("A1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
		if WGOgevonden or GOWgevonden or OWGgevonden:
			if WGOgevonden: print ("WGO", end = ' ')  # print on same line
			if GOWgevonden: print ("GOW", end = ' ')  # print on same line
			if OWGgevonden: print ("OWG", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))	
			if kubusLaag==0 and indexPositieInLaag==2: 
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("B1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==4: 
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in 2. draai het onderste vlak 2x tegen de klok in 3. draai het linker vlak met de klok mee.")
				while True:
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("C1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==6: 
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("D1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				while True:
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("E1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("F1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in.")
				while True:
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("G1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=draaiRinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiR(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("H1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
 
	return WOB_OBW_BWO_oplossen(kubusFormalParameter)

#tot hier goed denk ik
def WOB_OBW_BWO_oplossen(kubusFormalParameter):		
	WOBgevonden=False
	OBWgevonden=False
	BWOgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ') 
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WOB":
				WOBgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "OBW":
				OBWgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "BWO":
				BWOgevonden=True
				break
		if WOBgevonden:
			if kubusLaag==0 and indexPositieInLaag==2: 
				print ("WOB", end = ' ')  # print on same line
				print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
				print("WOB staat al goed")
				break 
		if OBWgevonden or BWOgevonden:
			if OBWgevonden: print ("OBW", end = ' ')  # print on same line
			if BWOgevonden: print ("BWO", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==2: 
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("I1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
		if WOBgevonden or OBWgevonden or BWOgevonden:
			if WOBgevonden: print ("WOB", end = ' ')  # print on same line
			if OBWgevonden: print ("OBW", end = ' ')  # print on same line
			if BWOgevonden: print ("BWO", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))	
			if kubusLaag==0 and indexPositieInLaag==0: 
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee")
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("J1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==4: 
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("K1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==6: 
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het onderste vlak 2x met de klok mee 3. draai het rechter vlak tegen de klok in.")
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("L1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("M1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("N1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("O1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee.")
				while True:
					kubusFormalParameter=draaiFinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiF(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("P1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break

	return WBR_BRW_RWB_oplossen(kubusFormalParameter)

#tot hier goed denk ik
def WBR_BRW_RWB_oplossen(kubusFormalParameter):		
	WBRgevonden=False
	BRWgevonden=False
	RWBgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ') 
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WBR":
				WBRgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "BRW":
				BRWgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "RWB":
				RWBgevonden=True
				break
		if WBRgevonden:
			if kubusLaag==0 and indexPositieInLaag==4: 
				print ("WBR", end = ' ')  # print on same line
				print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
				print("WBR staat al goed")
				break 
		if BRWgevonden or RWBgevonden:
			if BRWgevonden: print ("BRW", end = ' ')  # print on same line
			if RWBgevonden: print ("RWB", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==4: 
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("Q1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
		if WBRgevonden or BRWgevonden or RWBgevonden:
			if WBRgevonden: print ("WBR", end = ' ')  # print on same line
			if BRWgevonden: print ("BRW", end = ' ')  # print on same line
			if RWBgevonden: print ("RWB", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))	
			if kubusLaag==0 and indexPositieInLaag==0: 
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak 2x met de klok mee 3. draai het rechter vlak met de klok mee")
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("R1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==2: 
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het onderste vlak met de klok mee. ")
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("S1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==6: 
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak tegen de klok in.")
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("T1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee.")
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("U1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee")
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("V1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("W1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de de klok in.")
				while True:
					kubusFormalParameter=draaiLinv(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiL(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("X1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break

	return WRG_RGW_GWR_oplossen(kubusFormalParameter)

def WRG_RGW_GWR_oplossen(kubusFormalParameter):		
	WRGgevonden=False
	RGWgevonden=False
	GWRgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ') 
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "WRG":
				WRGgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "RGW":
				RGWgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "GWR":
				GWRgevonden=True
				break
		if WRGgevonden:
			if kubusLaag==0 and indexPositieInLaag==6: 
				print ("WRG", end = ' ')  # print on same line
				print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
				print("WRG staat al goed")
				break 
		if RGWgevonden or GWRgevonden:
			if RGWgevonden: print ("RGW", end = ' ')  # print on same line
			if GWRgevonden: print ("GWR", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==6: 
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("Y1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
		if WRGgevonden or RGWgevonden or GWRgevonden:
			if WRGgevonden: print ("WRG", end = ' ')  # print on same line
			if RGWgevonden: print ("RGW", end = ' ')  # print on same line
			if GWRgevonden: print ("GWR", end = ' ')  # print on same line
			print("gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))	
			if kubusLaag==0 and indexPositieInLaag==0: 
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("Z1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==2: 
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak 2x met de klok mee 3. draai het linker vlak tegen de klok in")
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("AA1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==4: 
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee")
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("BB1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("CC1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in.")
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("DD1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				kubusFormalParameter=draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("EE1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				while True:
					kubusFormalParameter=draaiB(kubusFormalParameter)
					kubusFormalParameter=draaiD(kubusFormalParameter)
					kubusFormalParameter=draaiBinv(kubusFormalParameter)
					kubusFormalParameter=draaiDinv(kubusFormalParameter)
					print("FF1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break

	return OB_of_BO_oplossen(kubusFormalParameter)
 
def OB_of_BO_oplossen(kubusFormalParameter):
    	# bovenste vlak oplossen: wit kruis maken
	#zoek oranje wit (of WO) blokje
	OBgevonden=False
	BOgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "OB":
				OBgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "BO":
				BOgevonden=True
				break
		if OBgevonden: 	
			print("OB gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het rechter vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee 7. draai het onderste vlak met de klok mee. 8. draai het voorste vlak tegen de klok in. / 9. draai het onderste vlak met de klok mee. 10. draai het linker vlak met de klok mee. 11. draai het onderste vlak met de klok mee. 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak met de klok mee. 14. draai het voorste vlak tegen de klok in. 15. draai het onderste vlak tegen de klok in. 16. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				print("OB op de staat al juiste plek")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee. 9. draai het onderste vlak tegen de klok in 10. draai het voorste vlak tegen de klok in. 11. draai het onderste vlak tegen de klok in 12. draai het voorste vlak met de klok mee. 13. draai het onderste vlak tegen de klok in 14. draai het linker vlak met de klok mee. 15. draai het onderste vlak met de klok mee 16. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak 2x met de klok mee 10. draai het voorste vlak tegen de klok in. 11. draai het onderste vlak tegen de klok in 12. draai het voorste vlak met de klok mee. 13. draai het onderste vlak tegen de klok in 14. draai het linker vlak met de klok mee. 15. draai het onderste vlak met de klok mee 16. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
		if BOgevonden: 	
			print("BO gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het rechter vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee 7. draai het onderste vlak met de klok mee. 8. draai het voorste vlak 2x tegen de klok in. 9. draai het onderste vlak tegen de klok in 10. draai het voorste vlak met de klok mee. 11. draai het onderste vlak tegen de klok in 12. draai het linker vlak met de klok mee. 13. draai het onderste vlak met de klok mee 14. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in. 9. draai het voorste vlak tegen de klok in 10. draai het onderste vlak tegen de klok in 11. draai het voorste vlak met de klok mee. 12. draai het onderste vlak tegen de klok in 13. draai het linker vlak met de klok mee. 14. draai het onderste vlak met de klok mee 15. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak 2x met de klok mee. 8. draai het onderste vlak met de klok mee 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak met de klok mee 11. draai het voorste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in 13. draai het voorste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in 10. draai het linker vlak met de klok mee. 11. draai het onderste vlak met de klok mee. 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak met de klok mee. 14. draai het voorste vlak tegen de klok in. 15. draai het onderste vlak tegen de klok in. 16. draai het voorste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het voorste vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het voorste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak met de klok mee 8. draai het linker vlak tegen de klok in. ")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het voorste vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het voorste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak met de klok mee 8. draai het linker vlak tegen de klok in. ")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. ")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het voorste vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het voorste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak met de klok mee 8. draai het linker vlak tegen de klok in. ")
				break

	return BR_of_RB_oplossen(kubusFormalParameter)

def BR_of_RB_oplossen(kubusFormalParameter):
    	# bovenste vlak oplossen: wit kruis maken
	#zoek oranje wit (of WO) blokje
	BRgevonden=False
	RBgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "BR":
				BRgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "RB":
				RBgevonden=True
				break
		if BRgevonden: 	
			print("BR gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak 2x met de klok mee 9. draai het achterste vlak tegen de klok in. 10. draai het onderste vlak met de klok mee. 11. draai het achterste vlak met de klok mee. 12. draai het onderste vlak met de klok mee. 13. draai het linker vlak tegen de klok in. 14. draai het onderste vlak tegen de klok in. 15. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het achterste vlak tegen de klok in. 10. draai het onderste vlak met de klok mee. 11. draai het achterste vlak met de klok mee. 12. draai het onderste vlak met de klok mee. 13. draai het linker vlak tegen de klok in. 14. draai het onderste vlak tegen de klok in. 15. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				print("BR staat al goed.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak tegen de klok in 11. draai het linker vlak met de klok mee. 12. draai het onderste vlak tegen de klok in 13. draai het achterste vlak tegen de klok in. 14. draai het onderste vlak met de klok mee 15. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee.")
				break
		if RBgevonden: 	
			print("RB gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak tegen de klok in. 11. draai het linker vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het achterste vlak tegen de klok in. 14. draai het onderste vlak met de klok mee. 15. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak 2x tegen de klok in. 8. draai het onderste vlak tegen de klok in. 9. draai het linker vlak met de klok mee. 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in. 2. draai het onderste vlak tegen de klok in. 3. draai het linker vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het achterste vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het achterste vlak met de klok mee. 8. draai het onderste vlak tegen de klok in. 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak tegen de klok in. 11. draai het linker vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het achterste vlak tegen de klok in. 14. draai het onderste vlak met de klok mee. 15. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak 2x tegen de klok in. 8. draai het onderste vlak met de klok mee. 9. draai het achterste vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het linker vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het linker vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het linker vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in. 2. draai het onderste vlak tegen de klok in. 3. draai het linker vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het achterste vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het achterste vlak met de klok mee.")
				break

	return RG_of_GR_oplossen(kubusFormalParameter)

def RG_of_GR_oplossen(kubusFormalParameter):
	RGgevonden=False
	GRgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "RG":
				RGgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "GR":
				GRgevonden=True
				break
		if RGgevonden: 	
			print("RG gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak 2x met de klok mee 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)	
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee. 8. draai het onderste vlak met de klok mee. 9. draai het achterste vlak met de klok mee 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het rechter vlak met de klok mee. 14. draai het onderste vlak met de klok mee. 15. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				print("RG staat al goed")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in.")
				break
		if GRgevonden: 	
			print("GR gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)				
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak 2x met de klok mee 9. draai het achterste vlak met de klok mee. 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het rechter vlak met de klok mee. 14. draai het onderste vlak met de klok mee. 15. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=draaiFinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiF(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak met de klok mee. 9. draai het achterste vlak met de klok mee. 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het rechter vlak met de klok mee. 14. draai het onderste vlak met de klok mee. 15. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiLinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiL(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee. 8. draai het onderste vlak 2x met de klok mee 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in. 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee. 2. draai het onderste vlak tegen de klok in. 3. draai het achterste vlak tegen de klok in. 4. draai het onderste vlak tegen de klok in. 5. draai het rechter vlak met de klok mee. 6. draai het onderste vlak met de klok mee. 7. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het achterste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak met de klok mee. 8. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het achterste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak met de klok mee. 8. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiB(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiBinv(kubusFormalParameter)
				kubusFormalParameter=draaiDinv(kubusFormalParameter)
				kubusFormalParameter=draaiR(kubusFormalParameter)
				kubusFormalParameter=draaiD(kubusFormalParameter)
				kubusFormalParameter=draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het achterste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak met de klok mee. 8. draai het rechter vlak tegen de klok in.")
				break

	return kubusFormalParameter
 
 
 
#doorloop kubus en kijk waar "OW" of "WO" zich bevindt
for kubusLaag in range(0,3):
	print("")
	print('laag '+str(kubusLaag))
	for indexPositieInLaag in range(0,8):
		print (kubus[kubusLaag][indexPositieInLaag], end = ' ')  # print on same line
print("")



kubus=kubus_oplossen(kubus)



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



def test_draaiU():
        # begin toestand van een kubus
    kubus=[
["WGO","WO","WOB","WB","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]
    assert draaiU(kubus) != [
["WGO","WO","WOB","WB","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]

def test_draaiU_2():
        # begin toestand van een kubus
	kubus=[
["WGO","WO","WOB","WB","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]
	expected = [
["WRG","WG","WGO","WO","WOB","WB","WBR","WR"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]
	result = draaiU(kubus)

	assert controleer_kubus(result, expected)


def controleer_kubus(kubus1, kubus2):
	gelijk = kubus1[0][0] == kubus2[0][0]	
	gelijk = gelijk and (kubus1[0][1] == kubus2[0][1])
	gelijk = gelijk and (kubus1[0][2] == kubus2[0][2])
	# test andere blokjes ook

	return gelijk





def test_opgelost_als_WO_op_juiste_plek():
        # begin toestand van een kubus
	kubus=[
["WGO","WO","WOB","WB","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]

	assert eerste_laag_oplossen(kubus)

def test_opgelost_als_WO_op_onjuiste_plek():
        # begin toestand van een kubus
	kubus=[
["WGO","OW","WOB","WB","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]

	assert not eerste_laag_oplossen(kubus)

def test_opgelost_als_WO_op_plek03():
        # begin toestand van een kubus
	kubus=[
["WGO","WB","WOB","WO","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]

	assert eerste_laag_oplossen(kubus)

def test_opgelost_als_WO_niet_op_plek03():
        # begin toestand van een kubus
	kubus=[
["WGO","WB","WOB","OW","WBR","WR","WRG","WG"],
["GO","O","OB","B","BR","R","RG","G"],
["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
]

	assert not eerste_laag_oplossen(kubus)

