from select import KQ_NOTE_RENAME


kubus=[
["YBO","GR","RYG","GW","WBR","OB","GOW","WR"],
["BY","O","GO","B","YO","R", "BR","G"],
["YOG","YG","BYR","RY","WOB","OW","GWR","BW"]
]

#doorloop kubus en kijk waar "OW" of "WO" zich bevindt




for kubusLaag in range(0,2):
	for indexPositieInLaag in range(0,7):
		if kubusLaag==0 and indexPositieInLaag==1:
			if kubus[kubusLaag, indexPositieInLaag]== "WO":
				None
			if kubus[kubusLaag, indexPositieInLaag]== "OW":
				draaiF()
				draaiUinv()
				draaiF()
				draaiU() #zet oranje weer voor

def draaiUinv():
	for indexPositieInLaag in range(0,7):
		kubus[0,indexPositieInLaag]=kubus[0, (indexPositieInLaag-2) %7]

def draaiU():
	for indexPositieInLaag in range(0,7):
		kubus[0,indexPositieInLaag]=kubus[0, (indexPositieInLaag+2) %7]

def draaiF():
	kubusCopy = kubus
	# kubus[0,0]=kubusCopy[0,2]
	# 0 positie van de string op 1 komt
	# 1 positie van de string op 2 komt
	# 2 positie van de string op 0 komt
	# is gelijk aan + 1 mod 3
	kubus[0,0][0:0]=kubusCopy[0,2][2:2]
 	kubus[0,0][1:1]=kubusCopy[0,2][0:0]
  	kubus[0,0][2:2]=kubusCopy[0,2][1:1]

	kubus[0,1]=kubusCopy[1,2]
				
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
