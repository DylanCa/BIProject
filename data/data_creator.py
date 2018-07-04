from data.connection import oracle



def createOrder(clientName="UNKNOWN",
                clientSurname="UNKNOWN",
                clientMail="UNKNOWN",
                quantity=0,
                totalCost=0,
                orderState="UNKNOWN",
                trackingNumber=0000,
                country="UNKNOWN",
                candyReference=0):

    cursor = oracle.connectToOracle()

    # Add to Oracle

    cursor.close()
    return
