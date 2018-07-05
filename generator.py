from data.tables import candies, packaging, countries, orders


def generateRandomOrders(clientName="UNKNOWN",
                         clientSurname="UNKNOWN",
                         nbOrder=0):
    pass


def generateOrderPool(nbOrders=0):
    pass


def generateOrder(clientName="UNKNOWN",
                  clientSurname="UNKNOWN",
                  clientMail="UNKNOWN",
                  quantity=0,
                  countryName="UNKNOWN",
                  candyName="UNKNOWN",
                  colorName="UNKNOWN",
                  textureName="UNKNOWN",
                  variantName="UNKNOWN",
                  packagingName="UNKNOWN"):

    packagingID = packaging.getPackagingByName(packagingName)[0][0]
    countryID = countries.getCountryByName(countryName)[0][0]
    candyPrice = candies.getCandyCostByID(candies.getCandyByName(candyName)[0][0])[0]

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

    return True
