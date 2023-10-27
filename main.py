# IMPORTS

import time as t
import math as m
import random as r

# DEV FUNCTIONS AND LISTS

askcontinue = 999

def skipsec():
    t.sleep(1)

def continueflow():
    askcontinue == int(input("> "))

keylist = []

result = askcontinue


# -------------------------------------------------------------------------------- STORY >> ---------------

print("Oi. Você não está acostumado a conversar com um computador, não é?")
skipsec()

print("Você: ...")
skipsec()

print("1. Não. Quem é você? // 2. Onde estou?")
continueflow()

if result == 1:
    print("Voz estranha: Então você não se lembra de mim... Acho que a reencarnação mexeu com sua cabeça.")
    skipsec()

    print("Você: ...")
    skipsec()








