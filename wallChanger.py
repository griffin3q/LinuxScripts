import random
import os

path = "/home/wastcott/Pictures/Walls"

def pickOne():
    base = os.listdir(path)
    pick = random.choice(base)
    return pick

def setPicked(pick):
    os.system((f"feh --bg-scale {path}/{pick}"))
    

pick=pickOne()

setPicked(pick)

