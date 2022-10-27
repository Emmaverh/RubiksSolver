kubus=[
[“OGY”,“RB”,”RBY”,”WO”,”OYB”,”GY”,”OBW”,”OY”],
[“GR”,"O",”GW”,"B",”BW”,"R", ”RW”,"G"],
[“RGW”,”YR”,”GOW”,”OB”,”RWB”,”OG”,”GRY”,”YB”]
]

#doorloop kubus en kijk waar “OW” of “WO” zich bevindt

#het is handiger om ook voor de 2de laag 8 blokjes te geven, blokje 5,6,7,8 
kubus[2,5]= null
kubus[2,6]= null
kubus[2,7]= null
kubus[2,8]= null

null betekent dat de variabele geen waarde heeft. 

for kubusLaag = 1 to 3:
for indexPostieInLaag = 1 to 8:
vergelijk een plekje op de kubus met “OW” of “WO” (kubuslaag, 
indexPostieInLaag )

vergelijk een plekje op de kubus met “OW” of “WO” (i,j):
	if  kubus[i,j]==”WO”:
		voer een oplossing algortime 1 uit om i,j op 1,2 te krijgen (i,j)
	if kubus[i,j]==”OW”:
		voer een oplossing algortime 2 uit om i,j op 1,2 te krijgen (i,j)


voer een oplossing algortime 1 uit om i,j op 1,2 te krijgen (i,j):
	if i=1 and j = 4 :
		U’   #zie mijn bijlage voor de uitleg van de beweging
             
voer een oplossing algortime 2 uit om i,j op 1,2 te krijgen (i,j):
	blbalab

U’:  #kubus upper vlak 1 slag tegen de klok in draaien
	for indexPostieInLaag  = 1 to 8:
	kubus[1,indexPostieInLaag ]=kubus[1,(indexPostieInLaag-2) modulo 8]
