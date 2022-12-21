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