#TODO meer TDD (unit/regressie tests), opruimen, refactoren, connectie met GAN robot of grafisch representeren kubus.

import oplossen

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

#kubus=[
#["BYR","YB","OGY","GO","BOY","RB","WOB","RG"],
#["BW","O","GY","B","OB","R","WG","G"],
#["WBR","YO","WGO","WR","GRY","RY","GWR","WO"]	
#]

#kubus=[
#["GYO","RW","RWB","GY","GWR","BW","YGR","OY"],
#["RB","O","OG","B","BY","R","WO","G"],
#["BYR","BO","OBW","GR","OWG","RY","OYB","WG"]	
#]

#kubus=[
#["YRB","YG","OWG","WB","YOG","GR","BOY","WR"],
#["YB","O","WG","B","RY","R","OB","G"],
#["BWO","OW","WRG","GO","WBR","RB","RYG","YO"]	
#]

kubus=[
["WGO","WO","WOB","WB","WBR","WR","WRG","WG"],
["YG","O","OB","B","BR","R","YB","G"],
["OGY","OY","YRB","BY","YGR","RY","YBO","GY"]	
]

def wisselChar(tekst, van, naar):
	character = tekst[van]
	temp = list(tekst) 
	temp[naar] = character
	tekst = "".join(temp)
	return tekst

for kubusLaag in range(0,3):
	print("")
	print('laag '+str(kubusLaag))
	for indexPositieInLaag in range(0,8):
		print (kubus[kubusLaag][indexPositieInLaag], end = ' ')  # print on same line

print("")

kubus=oplossen.kubus_oplossen(kubus)

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

