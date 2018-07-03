from .ENUMS import *
import random


def getCountry():
    # TODO:
    # ADD SHIPPING ASSOCIATED
    return random.choice(test_countries)


def getCandy():
    return random.choice(test_candy)


# SELECT column FROM
# ( SELECT column FROM table
# ORDER BY dbms_random.value )
# WHERE rownum = 1


def getColor():
    return random.choice(test_color)


def getVariant():
    return random.choice(test_variant)


def getTexture():
    return random.choice(test_texture)


def getConditionning():
    return random.choice(test_conditionning)


def getAmountOrdered():
    return random.randint(1, 100)
