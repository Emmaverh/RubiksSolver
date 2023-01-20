# Libraries
import argparse
import json
import random as rndm
from playsound import playsound

# Classes
import re
import time

from .cube import Cube
from .visualizer import Viz
from .drive import Drive


class RubikLibrary:
    """
    Library Class acting as an orchestrator calling other classes.
    Methods:
        - run
        - move
        - __interface
    """

    def __init__(self, do_run):
        """
        Constructor from APP class to read the config file, generate the instances from modules
        and declare global variables.
        :param dir_config: path with the configuration file.
        :param dir_face_map: path with the face mapper file.
        :param dir_cube_saved: path with the data of the cube resolved.
        """
        
        self.do_run=do_run
        if not do_run:
            return

        # App execution
        dir_config = "data/config.json"
        dir_face_map= "data/face_map.json"
        dir_cube_saved="data/cube_saved.json"

        # Reading the face map json file
        with open(dir_config) as f:
            self.config = json.load(f)

        # Reading the face map json file
        with open(dir_face_map) as f:
            face_map = json.load(f)

        # Reading the config json file
        with open(dir_cube_saved) as f:
            self.data = json.load(f)

        # Instance
        self.cube = Cube(self.config, self.data)
        self.viz = Viz(self.config)
        self.drive = Drive(face_map)

        # Variables
        self.help = """Valid commands:
                    - t: Top side move 1 clockwise.
                    - f: Front side move 1 clockwise.
                    - d: Down side move 1 clockwise.
                    - r: Right side move 1 clockwise.
                    - l: Left side move 1 clockwise.
                    - b: Back side move 1 clockwise.
                    - h: show the help.
                    - s: solve the cube.
                    - c: close the app.
                    """
        self.dcube = self.cube.load()
        self.moves_counter = 0

        """
        orchestrator, managing all calls.
        """
        print("[APP] Initializing the Rubik's Cube")

        # Rendering latest state
        print("[APP] Rendering the latest saved state from the Cube:")
        self.viz.render(self.dcube, self.moves_counter)

        # # Starting the communication interface
        # self.__interface()

        # # Saving the cube
        # self.cube.save(self.dcube)
        # print("[APP] Rubik\'s cube successfully saved")

        # # Closing program
        # print("[APP] Program closed")

    def move(self, permutation):
        """
        This method makes a move in the cube.
        :param permutation: (f, t, d, r, l, b) followed by a number.
        :return: None.
        """
        if not self.do_run:
            return
        #converteer bewerking, want wit is bij graphics voor en oranje is onder
        aantalperm = permutation[1:2]
        side = permutation[0:1]
        if side == 't':
            side='f'
        elif side == 'f':
            side='d'
        elif side == 'd':
            side='b'
            aantalperm =  str((int(aantalperm)+2)%4) # wegens, volgens mij foutje vanm Emma, DINV is D en andersom???
        elif side == 'b':
            side='t'
            aantalperm =  str((int(aantalperm)+2)%4) # wegens, volgens mij foutje vanm Emma, DINV is D en andersom???
        permutation=side+aantalperm

        self.dcube = self.drive.move(self.dcube, permutation)
        playsound('./rubikscubegraphics/draai.mp3')
        self.viz.render(self.dcube, self.moves_counter)
        self.moves_counter += 1
        # time.sleep(1)

    def __interface(self):
        """
        This method acts as a front-end to input the commands and interact with the cube.
        :return: None.
        """
        intro = """Please insert a face to move (f, t, d, r, l, b) followed by a number or type 'r' to reset or 'h' for help:\n"""
        inpt = input(intro)
        check = self.drive.check_for_moves(inpt)

        # Input commands
        if inpt != 'c' and check:
            self.dcube = self.drive.move(self.dcube, inpt)
            print("[APP] The Cube was updated:")
            self.moves_counter += 1
            self.viz.render(self.dcube, self.moves_counter)
            return self.__interface()
        elif inpt == 'h':
            print(self.help)
            return self.__interface()
        elif inpt == 'r':
            self.dcube = self.cube.restart()
            self.moves_counter = 0
            self.viz.render(self.dcube, self.moves_counter)
            print(f'[APP] Cube was restarted after {self.moves_counter} moves.')
            return self.__interface()
        elif inpt == 'x':
            msg = "[APP] Please select the number of random moves to apply:\n"
            moves = int(input(msg))
            self.__auto_move(moves)
            return self.__interface()
        elif inpt != 'c' and not check:
            print(f"[APP] Sorry, the command {inpt} is not valid.")
            return self.__interface()
        elif inpt == 'c':
            print('[APP] Closing the app.')


