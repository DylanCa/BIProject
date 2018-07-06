from data.tables import candies, packaging, countries, orders, colors, textures, variants, stocks
from data.client_infos import client_names, client_surnames

import random


def generateOrderPool(nbOrders=0): # Generates a random number of Orders according to the parameter given
    for x in range(0, nbOrders):
        clientName = random.choice(client_names)
        clientSurname = random.choice(client_surnames)
        clientMail = "{}.{}@gmail.com".format(clientName, clientSurname)
        quantity = random.randint(1, 1000)
        countryName = random.choice(countries.getCountriesList())[0]
        candyName = random.choice(candies.getCandiesList())[0]
        colorName = random.choice(colors.getColorsList())[0]
        textureName = random.choice(textures.getTexturesList())[0]
        variantName = random.choice(variants.getVariantsList())[0]
        packagingName = random.choice(["Sample", "Box", "Bag"])

        generateOrder(
            clientName=clientName,
            clientSurname=clientSurname,
            clientMail=clientMail,
            quantity=quantity,
            countryName=countryName,
            candyName=candyName,
            colorName=colorName,
            textureName=textureName,
            variantName=variantName,
            packagingName=packagingName)


def generateOrder(clientName="UNKNOWN",
                  clientSurname="UNKNOWN",
                  clientMail="UNKNOWN",
                  quantity=0,
                  countryName="UNKNOWN",
                  candyName="UNKNOWN",
                  colorName="UNKNOWN",
                  textureName="UNKNOWN",
                  variantName="UNKNOWN",
                  packagingName="UNKNOWN"): # Generates an order according to the parameters given

    packagingID = packaging.getPackagingByName(packagingName)[0][0]
    countryID = countries.getCountryByName(countryName)[0][0]
    candyPrice = candies.getCandyCostByID(
        candies.getCandyByName(candyName)[0][0])[0]

    if packagingID == 2:
        candyPrice = candyPrice[5]

    elif packagingID == 3:
        candyPrice = candyPrice[6]

    elif packagingID == 4:
        candyPrice = candyPrice[7]

    totalCost = candyPrice * quantity

    candyReferenceID = candies.createCandyReferenceByName(
        candyName=candyName,
        colorName=colorName,
        textureName=textureName,
        variantName=variantName,
        packagingName=packagingName)[0][0]

    orders.createOrder(
        clientName=clientName,
        clientSurname=clientSurname,
        clientMail=clientMail,
        quantity=quantity,
        totalCost=totalCost,
        orderState="PENDING",
        countryID=countryID,
        candyReference=candyReferenceID)

    stocks.updateStockQuantityByCandyName(candyName, quantity)

    return True
