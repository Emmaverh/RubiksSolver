# Libraries
import json
import pandas as pd


class CubeConvert:
    """The cube convert class transfroms between ddifferen representations of the rubik's cube model.
    Methods:
        - convertEmmma2Graph
    """
    def __init__(self):
        pass

    @staticmethod
    def convertGraph2Emma (kubusGraph):
#          |R1|R2|R3|
#          |R4|R5|R6|
#          |R7|R8|R9|
# |B1|B2|B3|W1|W2|W3|G1|G2|G3|Y1|Y2|Y3|
# |B4|B5|B6|W4|W5|W6|G4|G5|G6|Y4|Y5|Y6|
# |B7|B8|B9|W7|W8|W9|G7|G8|G9|Y7|Y8|Y9|
#          |O1|O2|O3|
#          |O4|O5|O6|
#          |O7|O8|O9|

        # kubus in opgeloste toestand:
        kubus_emma=[
        ["WGO","WO","WOB","WB","WBR","WR","WRG","WG"],
        ["GO","O","OB","B","BR","R","RG","G"],
        ["OGY","OY","OYB","BY","BYR","RY","RYG","GY"]	
        ]

        # kubusGraph =json.loads('{ "w": ["w1", "w2", "w3", "w4", "w5", "w6", "w7", "w8", "w9"],"r": ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"],  "g": ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"],  "o": ["o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9"],  "b": ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"],  "y": ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8", "y9"]}')

        kubus_emma[0][0][0]=kubusGraph["w"][9][0]

        return kubus_emma

    @staticmethod
    def convertEmma2Graph (kubus_emma):
#          |R1|R2|R3|
#          |R4|R5|R6|
#          |R7|R8|R9|
# |B1|B2|B3|W1|W2|W3|G1|G2|G3|Y1|Y2|Y3|
# |B4|B5|B6|W4|W5|W6|G4|G5|G6|Y4|Y5|Y6|
# |B7|B8|B9|W7|W8|W9|G7|G8|G9|Y7|Y8|Y9|
#          |O1|O2|O3|
#          |O4|O5|O6|
#          |O7|O8|O9|


        # kubus in opgeloste toestand:
        kubusGraph =json.loads('{ "w": ["w1", "w2", "w3", "w4", "w5", "w6", "w7", "w8", "w9"],"r": ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"],  "g": ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"],  "o": ["o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9"],  "b": ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"],  "y": ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8", "y9"]}')

        for kubusLaag in range(0,3):
            for indexPositieInLaag in range(0,8):
                kubus_emma[kubusLaag][indexPositieInLaag]=kubus_emma[kubusLaag][indexPositieInLaag].lower()

        kubusGraph["w"] = [kubus_emma[0][4][0]+str(1),kubus_emma[0][5][0]+str(2),kubus_emma[0][6][0]+str(3),
        kubus_emma[0][3][0]+str(4), "w"+str(5),
        kubus_emma[0][7][0]+str(6), kubus_emma[0][2][0]+str(7), 
        kubus_emma[0][1][0]+str(8), kubus_emma[0][0][0]+str(9)  ]
        kubusGraph["r"] = [kubus_emma[2][4][2]+str(1),kubus_emma[2][5][0]+str(2),kubus_emma[2][6][0]+str(3),
        kubus_emma[1][4][1]+str(4), "r"+str(5),
        kubus_emma[1][6][0]+str(6), kubus_emma[0][4][2]+str(7), 
        kubus_emma[0][5][1]+str(8), kubus_emma[0][6][1]+str(9)  ]        
        kubusGraph["g"] = [kubus_emma[0][6][2]+str(1),kubus_emma[1][6][1]+str(2),kubus_emma[2][6][2]+str(3),
        kubus_emma[0][7][1]+str(4), "g"+str(5),
        kubus_emma[2][7][0]+str(6), kubus_emma[0][0][1]+str(7), 
        kubus_emma[1][0][0]+str(8), kubus_emma[2][0][1]+str(9)  ]
        kubusGraph["o"] = [kubus_emma[0][2][1]+str(1),kubus_emma[0][1][1]+str(2),kubus_emma[0][0][2]+str(3),
        kubus_emma[1][2][0]+str(4), "o"+str(5),
        kubus_emma[1][0][1]+str(6), kubus_emma[2][2][0]+str(7), 
        kubus_emma[2][1][0]+str(8), kubus_emma[2][0][0]+str(9)  ]
        kubusGraph["b"] = [kubus_emma[2][4][0]+str(1),kubus_emma[1][4][0]+str(2),kubus_emma[0][4][1]+str(3),
        kubus_emma[2][3][0]+str(4), "b"+str(5),
        kubus_emma[0][3][1]+str(6), kubus_emma[2][2][2]+str(7), 
        kubus_emma[1][2][1]+str(8), kubus_emma[0][2][2]+str(9)  ]
        kubusGraph["y"] = [kubus_emma[2][6][1]+str(1),kubus_emma[2][5][1]+str(2),kubus_emma[2][4][1]+str(3),
        kubus_emma[2][7][1]+str(4), "y"+str(5),
        kubus_emma[2][3][1]+str(6), kubus_emma[2][0][2]+str(7), 
        kubus_emma[2][1][1]+str(8), kubus_emma[2][2][1]+str(9)  ]
           
        with open('data/cube_saved.json', 'w') as f:
            json.dump(kubusGraph, f)

        for kubusLaag in range(0,3):
            for indexPositieInLaag in range(0,8):
                kubus_emma[kubusLaag][indexPositieInLaag]=kubus_emma[kubusLaag][indexPositieInLaag].upper()
 
        return kubusGraph

class Cube:
    """The cube class represents the rubik's cube model.
    Methods:
        - load
        - restart
        - save
    """
    def __init__(self, config: dict, data: dict):
        """
        Constructor method to generate the initial cube variables.
        :param data: loads the cube data from the json file with the latest saved state.
        """
        self.path_cube_done = config['path_cube_done']
        self.dcube = pd.DataFrame(data)

    def load(self) -> pd.DataFrame:
        """
        Loads the cube object.
        :return: returns a Dataframe with the generated cube.
        """
        return self.dcube

    def restart(self) -> pd.DataFrame:
        """
        Restart the cube by loading the solved data from the json file.
        :return: the loaded data from the json file.
        """
        # Reading the config json file
        with open(self.path_cube_done) as f:
            cube_done = json.load(f)
        # Restart Cube
        self.dcube = pd.DataFrame(cube_done)
        return self.dcube

    @staticmethod
    def save(dcube: pd.DataFrame):
        """
        Saves the state of the cube in a json file.
        :param dcube: Dataframe with the data of the state of the cube.
        :return: None.
        """
        data = dcube.to_dict('list')
        with open('data/cube_saved.json', 'w') as f:
            json.dump(data, f, indent=4)

