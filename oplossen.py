import rubik_bewerkingen

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
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai 2 keer het bovenste vlak tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het linkervlak tegen de klok in 3. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het bovenste vlak 2x met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee 2. draai het bovenste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het linker vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het linker vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het linker vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
		if OWgevonden:
			print("OW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het voorvlak met de klok mee 2. draai het bovenvlak tegen de klok in 3. draai het rechter vlak met de klok mee 4.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1.draai het bovenste vlak tegen de klok in, 2. draai het voorvlak met de klok mee 3. draai het bovenvlak tegen de klok in 4. draai het rechter vlak met de klok mee 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1.draai het bovenste vlak 2x tegen de klok in, 2. draai het voorvlak met de klok mee 3. draai het bovenvlak tegen de klok in 4. draai het rechter vlak met de klok mee 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1.draai het bovenste vlak met de klok mee 2. draai het voorvlak met de klok mee 3. draai het bovenvlak tegen de klok in 4. draai het rechter vlak met de klok mee 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het rechtervlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het linker vlak met de klok mee 3. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x tegen de klok in 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak 2x met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het voor vlak 2 keer tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het voor vlak 2 keer met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het voorste vlak 2x met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				print("WB op de staat al juiste plek")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het achterste vlak 2x tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het rechter vlak 2x tegen de klok in 2. draai onderste vlak 2x tegen de klok in 3. draai het linker vlak 2x tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het linker vlak met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het linker vlak met de klok mee")
				break			
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het linker vlak met de klok mee")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het linker vlak met de klok mee")
		if BWgevonden:
			print("BW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het linker vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het achterste vlak met de klok mee 5. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in 2. draai het bovenste vlak met de klok mee 3. draai het achterste vlak met de klok mee 4.draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in 2. draai het linker vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak 2x met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het achterste vlak met de klok mee 4.draai het linker vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak 2x met de klok mee 3. draai het linker vlak 2x met de klok mee. ")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het linker vlak 2x tegen de klok in 2. draai het bovenste vlak met de klok mee 3. draai het achterste vlak met de klok mee 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het linker vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het linker vlak 2x tegen de klok in.")
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				print("WR op de staat al juiste plek")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak 2x tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het achterste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak 2x tegen de klok in 2. draai het achterste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het achterste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in 2. draai het bovenste vlak met de klok mee 3. draai het rechter vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in")
				break
		if RWgevonden:
			print("RW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het bovenste vlak met de klok mee 4. draai het rechter vlak tegen de klok in 5. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het achterste vlak met de klok mee 3. draai het rechter vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het bovenste vlak met de klok mee 3. draai het rechter vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het achterste vlak tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het achterste vlak tegen de klok in. 5. draai het bovenste vlak met de klok mee 6. draai het rechter vlak tegen de klok in. 7. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het achterste vlak 2x tegen de klok in. 2. draai het bovenste vlak met de klok mee 3. draai het rechter vlak tegen de klok in. 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1.draai het achterste vlak 2x tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x tegen de klok in")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				print("WG staat al op de juiste plek")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee 2. draai het linker vlak tegen de klok in 3. draai het bovenste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het achterste vlak met de klok mee 3. draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4.draai het achterste vlak tegen de klok in. 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4.draai het achterste vlak tegen de klok in. 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4.draai het achterste vlak tegen de klok in. 5.draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het bovenste vlak tegen de klok in. 3.draai het achterste vlak tegen de klok in. 4.draai het bovenste vlak met de klok mee.")
				break
		if GWgevonden:
			print("GW gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==0 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee. 2. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in 2. draai het voorste vlak met de klok mee. 3. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==0 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee 2. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==0 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het bovenste vlak met de klok mee. 3. draai het voorste vlak tegen de klok in 4. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak met de klok mee. 2. draai het voorste vlak met de klok mee 3. draai het bovenste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				print("1. draai het bovenste vlak 2x met de klok mee. 2. draai het linker vlak met de klok mee 3. draai het bovenste vlak 2x tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
				print("1. draai het bovenste vlak tegen de klok in. 2. draai het achterste vlak tegen de klok in 3. draai het bovenste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het rechter vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in 2. draai het rechter vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak 2x tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
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
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("B1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==4: 
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in 2. draai het onderste vlak 2x tegen de klok in 3. draai het linker vlak met de klok mee.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("C1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==6: 
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("D1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("E1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("F1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("G1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("H1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][0] == "WGO":
						break 
				break
 
	return WOB_OBW_BWO_oplossen(kubusFormalParameter)


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
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het rechter vlak met de klok mee")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("J1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==4: 
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("K1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==6: 
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het onderste vlak 2x met de klok mee 3. draai het rechter vlak tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("L1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("M1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("N1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("O1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("P1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het voorste vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][2] == "WOB":
						break 
				break

	return WBR_BRW_RWB_oplossen(kubusFormalParameter)


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
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak 2x met de klok mee 3. draai het rechter vlak met de klok mee")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("R1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==2: 
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het linker vlak tegen de klok in 4. draai het onderste vlak met de klok mee. ")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("S1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==6: 
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("T1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("U1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("V1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("W1. draai het linker vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][4] == "WBR":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
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
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee 4. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("Z1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==2: 
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee 2. draai het onderste vlak 2x met de klok mee 3. draai het linker vlak tegen de klok in")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("AA1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==0 and indexPositieInLaag==4: 
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("BB1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==0: 
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("CC1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break
				break
			if kubusLaag==2 and indexPositieInLaag==2: 
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("DD1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break 
				break
			if kubusLaag==2 and indexPositieInLaag==4: 
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee.")
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
					print("EE1. draai het achterste vlak met de klok mee 2. draai het onderste vlak met de klok mee 3. draai het achterste vlak tegen de klok in 4. draai het onderste vlak tegen de klok in. ")
					if kubusFormalParameter[0][6] == "WRG":
						break
				break
			if kubusLaag==2 and indexPositieInLaag==6: 
				while True:
					kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
					kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het rechter vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee 7. draai het onderste vlak met de klok mee. 8. draai het voorste vlak tegen de klok in. / 9. draai het onderste vlak met de klok mee. 10. draai het linker vlak met de klok mee. 11. draai het onderste vlak met de klok mee. 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak met de klok mee. 14. draai het voorste vlak tegen de klok in. 15. draai het onderste vlak tegen de klok in. 16. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				print("OB op de staat al juiste plek")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee. 9. draai het onderste vlak tegen de klok in 10. draai het voorste vlak tegen de klok in. 11. draai het onderste vlak tegen de klok in 12. draai het voorste vlak met de klok mee. 13. draai het onderste vlak tegen de klok in 14. draai het linker vlak met de klok mee. 15. draai het onderste vlak met de klok mee 16. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak 2x met de klok mee 10. draai het voorste vlak tegen de klok in. 11. draai het onderste vlak tegen de klok in 12. draai het voorste vlak met de klok mee. 13. draai het onderste vlak tegen de klok in 14. draai het linker vlak met de klok mee. 15. draai het onderste vlak met de klok mee 16. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het voorste vlak met de klok mee.  ")
				break
		if BOgevonden: 	
			print("BO gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het rechter vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee 7. draai het onderste vlak met de klok mee. 8. draai het voorste vlak 2x tegen de klok in. 9. draai het onderste vlak tegen de klok in 10. draai het voorste vlak met de klok mee. 11. draai het onderste vlak tegen de klok in 12. draai het linker vlak met de klok mee. 13. draai het onderste vlak met de klok mee 14. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in. 9. draai het voorste vlak tegen de klok in 10. draai het onderste vlak tegen de klok in 11. draai het voorste vlak met de klok mee. 12. draai het onderste vlak tegen de klok in 13. draai het linker vlak met de klok mee. 14. draai het onderste vlak met de klok mee 15. draai het linker vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak 2x met de klok mee. 8. draai het onderste vlak met de klok mee 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak met de klok mee 11. draai het voorste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in 13. draai het voorste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in 10. draai het linker vlak met de klok mee. 11. draai het onderste vlak met de klok mee. 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak met de klok mee. 14. draai het voorste vlak tegen de klok in. 15. draai het onderste vlak tegen de klok in. 16. draai het voorste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het voorste vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het voorste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak met de klok mee 8. draai het linker vlak tegen de klok in. ")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het voorste vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het voorste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak met de klok mee 8. draai het linker vlak tegen de klok in. ")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. ")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak 2x met de klok mee 9. draai het achterste vlak tegen de klok in. 10. draai het onderste vlak met de klok mee. 11. draai het achterste vlak met de klok mee. 12. draai het onderste vlak met de klok mee. 13. draai het linker vlak tegen de klok in. 14. draai het onderste vlak tegen de klok in. 15. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het achterste vlak tegen de klok in. 10. draai het onderste vlak met de klok mee. 11. draai het achterste vlak met de klok mee. 12. draai het onderste vlak met de klok mee. 13. draai het linker vlak tegen de klok in. 14. draai het onderste vlak tegen de klok in. 15. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				print("BR staat al goed.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak tegen de klok in 11. draai het linker vlak met de klok mee. 12. draai het onderste vlak tegen de klok in 13. draai het achterste vlak tegen de klok in. 14. draai het onderste vlak met de klok mee 15. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het linker vlak met de klok mee.")
				break
		if RBgevonden: 	
			print("RB gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak tegen de klok in. 11. draai het linker vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het achterste vlak tegen de klok in. 14. draai het onderste vlak met de klok mee. 15. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak 2x tegen de klok in. 8. draai het onderste vlak tegen de klok in. 9. draai het linker vlak met de klok mee. 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het linker vlak tegen de klok in. 2. draai het onderste vlak tegen de klok in. 3. draai het linker vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het achterste vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het achterste vlak met de klok mee. 8. draai het onderste vlak tegen de klok in. 9. draai het linker vlak tegen de klok in. 10. draai het onderste vlak tegen de klok in. 11. draai het linker vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het achterste vlak tegen de klok in. 14. draai het onderste vlak met de klok mee. 15. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak 2x tegen de klok in. 8. draai het onderste vlak met de klok mee. 9. draai het achterste vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het linker vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het linker vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het linker vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het linker vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
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
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak 2x met de klok mee 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)	
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee. 8. draai het onderste vlak met de klok mee. 9. draai het achterste vlak met de klok mee 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het rechter vlak met de klok mee. 14. draai het onderste vlak met de klok mee. 15. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				print("RG staat al goed")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het achterste vlak met de klok mee. 7. draai het onderste vlak tegen de klok in. 8. draai het achterste vlak tegen de klok in.")
				break
		if GRgevonden: 	
			print("GR gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)				
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak 2x met de klok mee 9. draai het achterste vlak met de klok mee. 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het rechter vlak met de klok mee. 14. draai het onderste vlak met de klok mee. 15. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het voorste vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het voorste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak met de klok mee 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak met de klok mee. 9. draai het achterste vlak met de klok mee. 10. draai het onderste vlak tegen de klok in. 11. draai het achterste vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het rechter vlak met de klok mee. 14. draai het onderste vlak met de klok mee. 15. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee. 8. draai het onderste vlak 2x met de klok mee 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in. 9. draai het rechter vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het achterste vlak met de klok mee. 14. draai het onderste vlak tegen de klok in. 15. draai het achterste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het achterste vlak met de klok mee. 2. draai het onderste vlak tegen de klok in. 3. draai het achterste vlak tegen de klok in. 4. draai het onderste vlak tegen de klok in. 5. draai het rechter vlak met de klok mee. 6. draai het onderste vlak met de klok mee. 7. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het achterste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak met de klok mee. 8. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het achterste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak met de klok mee. 8. draai het rechter vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het achterste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak met de klok mee. 8. draai het rechter vlak tegen de klok in.")
				break

	return GO_of_OG_oplossen(kubusFormalParameter)

def GO_of_OG_oplossen(kubusFormalParameter):
	GOgevonden=False
	OGgevonden=False
	for kubusLaag in range(0,3):
		print("")
		print('laag '+str(kubusLaag))
		for indexPositieInLaag in range(0,8):
			print (kubusFormalParameter[kubusLaag][indexPositieInLaag], end = ' ')  
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "GO":
				GOgevonden=True
				break
			if kubusFormalParameter[kubusLaag][indexPositieInLaag] == "OG":
				OGgevonden=True
				break
		if GOgevonden: 	
			print("GO gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				print("GO staat al goed")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het linker vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het voorste vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het voorste vlak met de klok mee. 8. draai het onderste vlak tegen de klok in. 9. draai het rechter vlak tegen de klok in 10. draai het onderste vlak tegen de klok in 11. draai het rechter vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het voorste vlak met de klok mee 14. draai het onderste vlak met de klok mee. 15. draai het voorste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee. 8. draai het onderste vlak 2x met de klok mee. 9. draai het rechter vlak tegen de klok in 10. draai het onderste vlak tegen de klok in 11. draai het rechter vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het voorste vlak met de klok mee 14. draai het onderste vlak met de klok mee. 15. draai het voorste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het rechter vlak tegen de klok in 10. draai het onderste vlak tegen de klok in 11. draai het rechter vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het voorste vlak met de klok mee 14. draai het onderste vlak met de klok mee. 15. draai het voorste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het voorste vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het rechter vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het voorste vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het rechter vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het voorste vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het voorste vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het rechter vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het voorste vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het rechter vlak tegen de klok in. 7. draai het onderste vlak tegen de klok in. 8. draai het rechter vlak met de klok mee.")
				break
		if OGgevonden: 	
			print("OG gevonden in laag "+str(kubusLaag)+" op positie "+str(indexPositieInLaag))
			if kubusLaag==1 and indexPositieInLaag==0:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in 9. draai het rechter vlak tegen de klok in 10. draai het onderste vlak tegen de klok in 11. draai het rechter vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het voorste vlak met de klok mee 14. draai het onderste vlak met de klok mee. 15. draai het voorste vlak tegen de klok in.")
				break
			if kubusLaag==1 and indexPositieInLaag==2:
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het linker vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het linker vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het voorste vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het voorste vlak 2x met de klok mee. 8. draai het onderste vlak met de klok mee. 9. draai het voorste vlak tegen de klok in. 10. draai het onderste vlak met de klok mee. 11. draai het rechter vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het rechter vlak met de klok mee. ")
				break
			if kubusLaag==1 and indexPositieInLaag==4:
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak met de klok mee. 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak tegen de klok in. 7. draai het linker vlak met de klok mee. 8. draai het onderste vlak tegen de klok in 9. draai het voorste vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het voorste vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het rechter vlak tegen de klok in. 14. draai het onderste vlak tegen de klok in. 15. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==1 and indexPositieInLaag==6:
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak met de klok mee. 5. draai het achterste vlak met de klok mee. 6. draai het onderste vlak tegen de klok in. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak 2x met de klok mee. 9. draai het voorste vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het voorste vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het rechter vlak tegen de klok in. 14. draai het onderste vlak tegen de klok in. 15. draai het rechter vlak met de klok mee.")
				break
			if kubusLaag==2 and indexPositieInLaag==1:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het onderste vlak met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het rechter vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee 7. draai het onderste vlak met de klok mee. 8. draai het voorste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==3:
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het rechter vlak tegen de klok in 2. draai het onderste vlak tegen de klok in 3. draai het rechter vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==5:
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het onderste vlak tegen de klok in 2. draai het rechter vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het rechter vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee 7. draai het onderste vlak met de klok mee. 8. draai het voorste vlak tegen de klok in.")
				break
			if kubusLaag==2 and indexPositieInLaag==7:
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
				kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
				print("1. draai het onderste vlak 2x met de klok mee 2. draai het rechter vlak tegen de klok in 3. draai het onderste vlak tegen de klok in 4. draai het rechter vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee 7. draai het onderste vlak met de klok mee. 8. draai het voorste vlak tegen de klok in.")
				break

	return Geel_kruis_maken(kubusFormalParameter)


def Geel_kruis_maken(kubusFormalParameter):
	print("****** nu gaan we het gele kruis maken op laag 2 : ")	
	if kubusFormalParameter[2][1][-1]=="Y" and kubusFormalParameter[2][3][-1]=="Y" and kubusFormalParameter[2][5][-1]=="Y" and kubusFormalParameter[2][7][-1]=="Y":
		print("Het gele kruis is er al") 
	if (kubusFormalParameter[2][3][-1]=="Y" and kubusFormalParameter[2][5][-1]=="Y" and kubusFormalParameter[2][1][0]=="Y" and kubusFormalParameter[2][7][0]=="Y"):
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		print("L1. draai het onderste vlak tegen de klok in. 2. draai het voorste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het voorste vlak met de klok mee 10. draai het linker vlak met de klok mee 11. draai het onderste vlak tegen de klok in 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak met de klok mee. 14. draai het voorste vlak tegen de klok in.")
	if (kubusFormalParameter[2][1][-1]=="Y" and kubusFormalParameter[2][3][-1]=="Y" and kubusFormalParameter[2][5][0]=="Y" and kubusFormalParameter[2][7][0]=="Y"):
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		print("Q1. draai het voorste vlak met de klok mee 2. draai het linker vlak met de klok mee 3. draai het onderste vlak tegen de klok in 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee 8. draai het voorste vlak met de klok mee 9. draai het linker vlak met de klok mee 10. draai het onderste vlak tegen de klok in 11. draai het linker vlak tegen de klok in. 12. draai het onderste vlak met de klok mee. 13. draai het voorste vlak tegen de klok in.")
	if (kubusFormalParameter[2][5][-1]=="Y" and kubusFormalParameter[2][7][-1]=="Y" and kubusFormalParameter[2][1][0]=="Y" and kubusFormalParameter[2][3][0]=="Y"):
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		print("PO1. draai het onderste vlak 2x met de klok mee. 2. draai het voorste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het voorste vlak met de klok mee 10. draai het linker vlak met de klok mee 11. draai het onderste vlak tegen de klok in 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak met de klok mee. 14. draai het voorste vlak tegen de klok in.")
	if (kubusFormalParameter[2][1][-1]=="Y" and kubusFormalParameter[2][7][-1]=="Y" and kubusFormalParameter[2][3][0]=="Y" and kubusFormalParameter[2][5][0]=="Y"):
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		print("A1. draai het onderste vlak met de klok mee 2. draai het voorste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak met de klok mee 9. draai het voorste vlak met de klok mee 10. draai het linker vlak met de klok mee 11. draai het onderste vlak tegen de klok in 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak met de klok mee. 14. draai het voorste vlak tegen de klok in.")
	if (kubusFormalParameter[2][3][-1]=="Y" and kubusFormalParameter[2][7][-1]=="Y" and kubusFormalParameter[2][1][0]=="Y" and kubusFormalParameter[2][5][0]=="Y"):
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		print("YY1. draai het voorste vlak met de klok mee 2. draai het linker vlak met de klok mee 3. draai het onderste vlak tegen de klok in 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6.draai het voorste vlak tegen de klok in.")
	if (kubusFormalParameter[2][1][-1]=="Y" and kubusFormalParameter[2][5][-1]=="Y" and kubusFormalParameter[2][3][0]=="Y" and kubusFormalParameter[2][7][0]=="Y"):
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		print("KK1. draai het onderste vlak tegen de klok in 2. draai het voorste vlak met de klok mee 3. draai het linker vlak met de klok mee 4. draai het onderste vlak tegen de klok in 5. draai het linker vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het voorste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="Y" and kubusFormalParameter[2][3][0]=="Y" and kubusFormalParameter[2][5][0]=="Y" and kubusFormalParameter[2][7][0]=="Y":
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		print("LOLLLLLL1. draai het voorste vlak met de klok mee 2. draai het linker vlak met de klok mee 3. draai het onderste vlak tegen de klok in 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak met de klok mee. 6. draai het linker vlak met de klok mee 7. draai het onderste vlak tegen de klok in 8. draai het linker vlak tegen de klok in. 9. draai het onderste vlak met de klok mee. 10. draai het voorste vlak tegen de klok in. 11. draai het onderste vlak met de klok mee 12. draai het voorste vlak met de klok mee 13. draai het linker vlak met de klok mee 14. draai het onderste vlak tegen de klok in 15. draai het linker vlak tegen de klok in. 16. draai het onderste vlak met de klok mee. 17. draai het voorste vlak tegen de klok in.")
 
	return Geel_kruis_goedzetten (kubusFormalParameter)

def Geel_kruis_goedzetten (kubusFormalParameter):
	print("********** we gaan nu het gele kruis goed zetten: ")
	if kubusFormalParameter[2][1][0]=="O" and kubusFormalParameter[2][3][0]=="B" and kubusFormalParameter[2][5][0]=="R" and kubusFormalParameter[2][7][0]=="G":
		print("Het gele kruis staat al goed") 
	if kubusFormalParameter[2][1][0]=="G" and kubusFormalParameter[2][3][0]=="B" and kubusFormalParameter[2][5][0]=="R" and kubusFormalParameter[2][7][0]=="O":
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)	
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het linker vlak met de klok mee. 2. draai het onderste vlak tegen de klok in. 3. draai het linker vlak tegen de klok in. 4. draai het onderste vlak tegen de klok in. 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak 2x tegen de klok in. 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="O" and kubusFormalParameter[2][3][0]=="G" and kubusFormalParameter[2][5][0]=="B" and kubusFormalParameter[2][7][0]=="R":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het linker vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="R" and kubusFormalParameter[2][3][0]=="O" and kubusFormalParameter[2][5][0]=="G" and kubusFormalParameter[2][7][0]=="B":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het linker vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="B" and kubusFormalParameter[2][3][0]=="R" and kubusFormalParameter[2][5][0]=="O" and kubusFormalParameter[2][7][0]=="G":
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het linker vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="B" and kubusFormalParameter[2][3][0]=="O" and kubusFormalParameter[2][5][0]=="G" and kubusFormalParameter[2][7][0]=="R":
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het linker vlak met de klok mee. 2. draai het onderste vlak tegen de klok in. 3. draai het linker vlak tegen de klok in. 4. draai het onderste vlak tegen de klok in. 5. draai het linker vlak met de klok mee. 6. draai het onderste vlak 2x tegen de klok in. 7. draai het linker vlak tegen de klok in. 8. draai het onderste vlak met de klok mee. 9. draai het linker vlak met de klok mee. 10. draai het onderste vlak tegen de klok in. 11. draai het linker vlak tegen de klok in. 12. draai het onderste vlak tegen de klok in. 13. draai het linker vlak met de klok mee. 14. draai het onderste vlak 2x tegen de klok in. 15. draai het linker vlak tegen de klok in. 16. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="R" and kubusFormalParameter[2][3][0]=="B" and kubusFormalParameter[2][5][0]=="O" and kubusFormalParameter[2][7][0]=="G":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het linker vlak tegen de klok in. 9. draai het onderste vlak met de klok mee. 10. draai het linker vlak met de klok mee. 11. draai het onderste vlak tegen de klok in. 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak tegen de klok in. 14. draai het linker vlak met de klok mee. 15. draai het onderste vlak 2x tegen de klok in. 16. draai het linker vlak tegen de klok in. 17. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="G" and kubusFormalParameter[2][3][0]=="R" and kubusFormalParameter[2][5][0]=="B" and kubusFormalParameter[2][7][0]=="O":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak 2x tegen de klok in 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het linker vlak tegen de klok in. 9. draai het onderste vlak met de klok mee. 10. draai het linker vlak met de klok mee. 11. draai het onderste vlak tegen de klok in. 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak tegen de klok in. 14. draai het linker vlak met de klok mee. 15. draai het onderste vlak 2x tegen de klok in. 16. draai het linker vlak tegen de klok in. 17. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="O" and kubusFormalParameter[2][3][0]=="G" and kubusFormalParameter[2][5][0]=="R" and kubusFormalParameter[2][7][0]=="B":
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiL(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiLinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee. 2. draai het linker vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het linker vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het linker vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het linker vlak tegen de klok in. 9. draai het onderste vlak met de klok mee. 10. draai het linker vlak met de klok mee. 11. draai het onderste vlak tegen de klok in. 12. draai het linker vlak tegen de klok in. 13. draai het onderste vlak tegen de klok in. 14. draai het linker vlak met de klok mee. 15. draai het onderste vlak 2x tegen de klok in. 16. draai het linker vlak tegen de klok in. 17. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="R" and kubusFormalParameter[2][3][0]=="G" and kubusFormalParameter[2][5][0]=="O" and kubusFormalParameter[2][7][0]=="B":
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		print("1. draai het onderste vlak 2x met de klok mee.")
	if kubusFormalParameter[2][1][0]=="B" and kubusFormalParameter[2][3][0]=="R" and kubusFormalParameter[2][5][0]=="G" and kubusFormalParameter[2][7][0]=="O":
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee.")
	if kubusFormalParameter[2][1][0]=="G" and kubusFormalParameter[2][3][0]=="O" and kubusFormalParameter[2][5][0]=="B" and kubusFormalParameter[2][7][0]=="R":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in.")
	if kubusFormalParameter[2][1][0]=="O" and kubusFormalParameter[2][3][0]=="R" and kubusFormalParameter[2][5][0]=="B" and kubusFormalParameter[2][7][0]=="G":
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het rechter vlak met de klok mee. 2. draai het onderste vlak tegen de klok in. 3. draai het rechter vlak tegen de klok in. 4. draai het onderste vlak tegen de klok in. 5. draai het rechter vlak met de klok mee. 6. draai het onderste vlak 2x tegen de klok in. 7. draai het rechter vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="G" and kubusFormalParameter[2][3][0]=="O" and kubusFormalParameter[2][5][0]=="R" and kubusFormalParameter[2][7][0]=="B":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het rechter vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="B" and kubusFormalParameter[2][3][0]=="G" and kubusFormalParameter[2][5][0]=="O" and kubusFormalParameter[2][7][0]=="R":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het rechter vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="R" and kubusFormalParameter[2][3][0]=="B" and kubusFormalParameter[2][5][0]=="G" and kubusFormalParameter[2][7][0]=="O":
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiR(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiRinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee. 2. draai het rechter vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het rechter vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het rechter vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het rechter vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="O" and kubusFormalParameter[2][3][0]=="B" and kubusFormalParameter[2][5][0]=="G" and kubusFormalParameter[2][7][0]=="R":
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het voorste vlak met de klok mee. 2. draai het onderste vlak tegen de klok in. 3. draai het voorste vlak tegen de klok in. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak met de klok mee. 6. draai het onderste vlak 2x tegen de klok in. 7. draai het voorste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="R" and kubusFormalParameter[2][3][0]=="O" and kubusFormalParameter[2][5][0]=="B" and kubusFormalParameter[2][7][0]=="G":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het voorste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het voorste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="G" and kubusFormalParameter[2][3][0]=="R" and kubusFormalParameter[2][5][0]=="O" and kubusFormalParameter[2][7][0]=="B":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het voorste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het voorste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="B" and kubusFormalParameter[2][3][0]=="G" and kubusFormalParameter[2][5][0]=="R" and kubusFormalParameter[2][7][0]=="O":
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak tegen de klok in. 4. draai het voorste vlak tegen de klok in. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak met de klok mee. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het voorste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="B" and kubusFormalParameter[2][3][0]=="O" and kubusFormalParameter[2][5][0]=="R" and kubusFormalParameter[2][7][0]=="G":
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het achterste vlak tegen de klok in. 2. draai het onderste vlak tegen de klok in. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het achterste vlak tegen de klok in. 6. draai het onderste vlak 2x tegen de klok in. 7. draai het achterste vlak met de klok mee. 8. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="G" and kubusFormalParameter[2][3][0]=="B" and kubusFormalParameter[2][5][0]=="O" and kubusFormalParameter[2][7][0]=="R":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het achterste vlak met de klok mee. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="R" and kubusFormalParameter[2][3][0]=="G" and kubusFormalParameter[2][5][0]=="B" and kubusFormalParameter[2][7][0]=="O":
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak 2xtegen de klok in. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het achterste vlak met de klok mee. 9. draai het onderste vlak tegen de klok in")
	if kubusFormalParameter[2][1][0]=="O" and kubusFormalParameter[2][3][0]=="R" and kubusFormalParameter[2][5][0]=="G" and kubusFormalParameter[2][7][0]=="B":
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee. 2. draai het achterste vlak tegen de klok in. 3. draai het onderste vlak tegen de klok in. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het achterste vlak tegen de klok in. 7. draai het onderste vlak 2x tegen de klok in. 8. draai het achterste vlak met de klok mee. 9. draai het onderste vlak tegen de klok in")
  
	return GeleHoeken_op_de_goede_plaats_zetten(kubusFormalParameter) 

def GeleHoeken_op_de_goede_plaats_zetten(kubusFormalParameter):
	print("********** we gaan nu de gele hoeken op de goede plaats zetten: ")
	if (kubusFormalParameter[2][0]=="OGY" or kubusFormalParameter[2][0]=="YOG" or kubusFormalParameter[2][0]=="GYO") and (kubusFormalParameter[2][2]=="OYB" or kubusFormalParameter[2][2]=="BOY" or kubusFormalParameter[2][2]=="YBO") and (kubusFormalParameter[2][4]=="BYR" or kubusFormalParameter[2][4]=="RBY" or kubusFormalParameter[2][4]=="YRB") and (kubusFormalParameter[2][6]=="RYG" or kubusFormalParameter[2][6]=="YGR" or kubusFormalParameter[2][6]=="GRY"):
		print("De gele hoeken staan al op de goede plaats") 
	if (kubusFormalParameter[2][0]=="OGY" or kubusFormalParameter[2][0]=="YOG" or kubusFormalParameter[2][0]=="GYO") and (kubusFormalParameter[2][2]=="RYG" or kubusFormalParameter[2][2]=="YGR" or kubusFormalParameter[2][2]=="GRY") and (kubusFormalParameter[2][4]=="OYB" or kubusFormalParameter[2][4]=="BOY" or kubusFormalParameter[2][4]=="YBO") and (kubusFormalParameter[2][6]=="BYR" or kubusFormalParameter[2][6]=="RBY" or kubusFormalParameter[2][6]=="YRB"):	
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in. 10. draai het voorste vlak met de klok mee. 11. draai het onderste vlak met de klok mee. 12. draai het achterste vlak met de klok mee. 13. draai het onderste vlak tegen de klok in. 14. draai het voorste vlak tegen de klok in. 15. draai het onderste vlak met de klok mee. 16. draai het achterste vlak tegen de klok in.")
		#tot hier gewerkt.
	if (kubusFormalParameter[2][0]=="OGY" or kubusFormalParameter[2][0]=="YOG" or kubusFormalParameter[2][0]=="GYO") and (kubusFormalParameter[2][2]=="BYR" or kubusFormalParameter[2][2]=="RBY" or kubusFormalParameter[2][2]=="YRB") and (kubusFormalParameter[2][4]=="RYG" or kubusFormalParameter[2][4]=="YGR" or kubusFormalParameter[2][4]=="GRY")and (kubusFormalParameter[2][6]=="OYB" or kubusFormalParameter[2][6]=="BOY" or kubusFormalParameter[2][6]=="YBO"):
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		print("1. draai het onderste vlak tegen de klok in. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak tegen de klok in.")
	if (kubusFormalParameter[2][0]=="RYG" or kubusFormalParameter[2][0]=="YGR" or kubusFormalParameter[2][0]=="GRY") and (kubusFormalParameter[2][2]=="OYB" or kubusFormalParameter[2][2]=="BOY" or kubusFormalParameter[2][2]=="YBO") and (kubusFormalParameter[2][4]=="OGY" or kubusFormalParameter[2][4]=="YOG" or kubusFormalParameter[2][4]=="GYO") and (kubusFormalParameter[2][6]=="BYR" or kubusFormalParameter[2][6]=="RBY" or kubusFormalParameter[2][6]=="YRB"):	
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in. 10. draai het voorste vlak met de klok mee. 11. draai het onderste vlak met de klok mee. 12. draai het achterste vlak met de klok mee. 13. draai het onderste vlak tegen de klok in. 14. draai het voorste vlak tegen de klok in. 15. draai het onderste vlak met de klok mee. 16. draai het achterste vlak tegen de klok in. 17. draai het onderste vlak met de klok mee.")
	if (kubusFormalParameter[2][0]=="BYR" or kubusFormalParameter[2][0]=="RBY" or kubusFormalParameter[2][0]=="YRB") and (kubusFormalParameter[2][2]=="OYB" or kubusFormalParameter[2][2]=="BOY" or kubusFormalParameter[2][2]=="YBO") and (kubusFormalParameter[2][4]=="RYG" or kubusFormalParameter[2][4]=="YGR" or kubusFormalParameter[2][4]=="GRY") and (kubusFormalParameter[2][6]=="OGY" or kubusFormalParameter[2][6]=="YOG" or kubusFormalParameter[2][6]=="GYO"):	
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		print("1. draai het onderste vlak 2x tegen de klok in. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak met de klok mee.")
	if (kubusFormalParameter[2][0]=="RYG" or kubusFormalParameter[2][0]=="YGR" or kubusFormalParameter[2][0]=="GRY") and (kubusFormalParameter[2][2]=="OGY" or kubusFormalParameter[2][2]=="YOG" or kubusFormalParameter[2][2]=="GYO") and (kubusFormalParameter[2][4]=="BYR" or kubusFormalParameter[2][4]=="RBY" or kubusFormalParameter[2][4]=="YRB") and (kubusFormalParameter[2][6]=="OYB" or kubusFormalParameter[2][6]=="BOY" or kubusFormalParameter[2][6]=="YBO"):
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee. 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak tegen de klok in. 10. draai het voorste vlak met de klok mee. 11. draai het onderste vlak met de klok mee. 12. draai het achterste vlak met de klok mee. 13. draai het onderste vlak tegen de klok in. 14. draai het voorste vlak tegen de klok in. 15. draai het onderste vlak met de klok mee. 16. draai het achterste vlak tegen de klok in. 17. draai het onderste vlak 2x met de klok mee.")
	if (kubusFormalParameter[2][0]=="OYB" or kubusFormalParameter[2][0]=="BOY" or kubusFormalParameter[2][0]=="YBO") and (kubusFormalParameter[2][2]=="RYG" or kubusFormalParameter[2][2]=="YGR" or kubusFormalParameter[2][2]=="GRY") and (kubusFormalParameter[2][4]=="BYR" or kubusFormalParameter[2][4]=="RBY" or kubusFormalParameter[2][4]=="YRB") and (kubusFormalParameter[2][6]=="OGY" or kubusFormalParameter[2][6]=="YOG" or kubusFormalParameter[2][6]=="GYO"):
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		print("1. draai het onderste vlak met de klok mee . 2. draai het voorste vlak met de klok mee. 3. draai het onderste vlak met de klok mee. 4. draai het achterste vlak met de klok mee. 5. draai het onderste vlak tegen de klok in. 6. draai het voorste vlak tegen de klok in. 7. draai het onderste vlak met de klok mee. 8. draai het achterste vlak tegen de klok in. 9. draai het onderste vlak 2x met de klok mee.")
	if (kubusFormalParameter[2][0]=="BYR" or kubusFormalParameter[2][0]=="RBY" or kubusFormalParameter[2][0]=="YRB") and (kubusFormalParameter[2][2]=="OGY" or kubusFormalParameter[2][2]=="YOG" or kubusFormalParameter[2][2]=="GYO") and (kubusFormalParameter[2][4]=="OYB" or kubusFormalParameter[2][4]=="BOY" or kubusFormalParameter[2][4]=="YBO") and (kubusFormalParameter[2][6]=="RYG" or kubusFormalParameter[2][6]=="YGR" or kubusFormalParameter[2][6]=="GRY"):
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het voorste vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in. 9. draai het voorste vlak met de klok mee. 10. draai het onderste vlak met de klok mee. 11. draai het achterste vlak met de klok mee. 12. draai het onderste vlak tegen de klok in. 13. draai het voorste vlak tegen de klok in. 14. draai het onderste vlak met de klok mee. 15. draai het achterste vlak tegen de klok in. 16. draai het onderste vlak tegen de klok in.")
	if (kubusFormalParameter[2][0]=="OYB" or kubusFormalParameter[2][0]=="BOY" or kubusFormalParameter[2][0]=="YBO") and (kubusFormalParameter[2][2]=="BYR" or kubusFormalParameter[2][2]=="RBY" or kubusFormalParameter[2][2]=="YRB") and (kubusFormalParameter[2][4]=="OGY" or kubusFormalParameter[2][4]=="YOG" or kubusFormalParameter[2][4]=="GYO") and  (kubusFormalParameter[2][6]=="RYG" or kubusFormalParameter[2][6]=="YGR" or kubusFormalParameter[2][6]=="GRY"):
		kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiB(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiBinv(kubusFormalParameter)
		kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
		print("1. draai het voorste vlak met de klok mee. 2. draai het onderste vlak met de klok mee. 3. draai het achterste vlak met de klok mee. 4. draai het onderste vlak tegen de klok in. 5. draai het voorste vlak tegen de klok in. 6. draai het onderste vlak met de klok mee. 7. draai het achterste vlak tegen de klok in. 8. draai het onderste vlak tegen de klok in.")
  
	return GeleHoeken_goed_zetten(kubusFormalParameter)

def GeleHoeken_goed_zetten(kubusFormalParameter):
    print("we gaan nu de gele hoeken goed zetten")
    if kubusFormalParameter[2][0]=="OGY": 
        print ("OGY", end = ' ')  # print on same line
        print("gevonden in laag "+str(2)+" op positie "+str(0))
        print("OGY staat al goed")
        
    if kubusFormalParameter[2][0]=="YOG":
        while True:
            print(kubusFormalParameter[2][0])
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("AAA1. draai het voorste vlak tegen de klok in 2. draai het bovenste vlak tegen de klok in. 3. draai het voorste vlak met de klok mee 4. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][0] == "OGY":
                break
         
    if kubusFormalParameter[2][0]=="GYO": 
        while True:
            print(kubusFormalParameter[2][0])
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("AAA1. draai het voorste vlak tegen de klok in 2. draai het bovenste vlak tegen de klok in. 3. draai het voorste vlak met de klok mee 4. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][0] == "OGY":
                break
    
        
    if kubusFormalParameter[2][2]=="OYB": 
        print ("OYB", end = ' ')  # print on same line
        print("gevonden in laag "+str(2)+" op positie "+str(2))
        print("OYB staat al goed")
        
    if kubusFormalParameter[2][2]=="BOY":
        while True:
            print(kubusFormalParameter[2][2])
            kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("ABA 1. draai het onderste vlak tegen de klok in. 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4. draai het voorste vlak met de klok mee 5. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][2] == "OYB":
                break
    
    if kubusFormalParameter[2][2]=="YBO":
        while True:
            print(kubusFormalParameter[2][2])
            kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("ABA 1. draai het onderste vlak tegen de klok in. 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4. draai het voorste vlak met de klok mee 5. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][2] == "OYB":
                break
    

        
    if kubusFormalParameter[2][4]=="BYR": 
        print ("BYR", end = ' ')  # print on same line
        print("gevonden in laag "+str(2)+" op positie "+str(4))
        print("BYR staat al goed")

    if kubusFormalParameter[2][4]=="RBY":
        while True:
            print(kubusFormalParameter[2][4])
            kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("ACA 1. draai het onderste vlak 2x tegen de klok in. 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4. draai het voorste vlak met de klok mee 5. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][4] == "BYR":
                break
        
        
    
    if kubusFormalParameter[2][4]=="YRB": 
        while True:
            print(kubusFormalParameter[2][4])
            kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiDinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("ACA 1. draai het onderste vlak 2x tegen de klok in. 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4. draai het voorste vlak met de klok mee 5. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][4] == "BYR":
                break
    
    if kubusFormalParameter[2][6]=="RYG": 
        print ("RYG", end = ' ')  # print on same line
        print("gevonden in laag "+str(2)+" op positie "+str(6))
        print("RYG staat al goed")

    if kubusFormalParameter[2][6]=="YGR":
        while True:
            print(kubusFormalParameter[2][6])
            kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("ADA 1. draai het onderste vlak met de klok mee. 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4. draai het voorste vlak met de klok mee 5. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][6]== "RYG":
                break
        
    if kubusFormalParameter[2][6]=="GRY": 
        while True:
            print(kubusFormalParameter[2][6])
            kubusFormalParameter=rubik_bewerkingen.draaiD(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiFinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiUinv(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiF(kubusFormalParameter)
            kubusFormalParameter=rubik_bewerkingen.draaiU(kubusFormalParameter)
            print("ADA 1. draai het onderste vlak met de klok mee. 2. draai het voorste vlak tegen de klok in 3. draai het bovenste vlak tegen de klok in. 4. draai het voorste vlak met de klok mee 5. draai het bovenste vlak met de klok mee. ")
            if kubusFormalParameter[2][6]== "RYG":
                break
        
    if kubusFormalParameter[2][0]=="OGY" and kubusFormalParameter[2][2]=="OYB" and kubusFormalParameter[2][4]=="BYR" and kubusFormalParameter[2][6]=="RYG":
        print("de gele hoek kubusjes staan goed!")
    
    return kubusFormalParameter
    

 
