from .ENUMS import *
import random
from time import gmtime, strftime


def generateOrder(clientName="UNKNOWN", nbOrder=0):

    pool = list()

    for x in range(0, nbOrder):
        pool.append(
            "Order #{} - Date: {}, Client: {}, Amount: {}, Total Cost: {}, Country: {}, Reference Candy: #{}".
            format(x + 1, strftime("%d-%m-%Y %H:%M:%S", gmtime()), clientName,
                   random.randint(1, 100), random.randint(1, 9999),
                   random.choice(test_countries), random.randint(1, 3888)))

    for line in pool:
        print(line)
