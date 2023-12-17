import random
import os
#path to your walls dir
path = "/home/wastcott/Pictures/Walls"

def pickOne():
    base = os.listdir(path)
    pick = random.choice(base)
    return pick

def setPicked(pick):
    os.system((f"feh --bg-scale {path}/{pick}"))            #requirements
                                                    #Feh, python installed I guess usualy works xD

pick=pickOne()

setPicked(pick)

