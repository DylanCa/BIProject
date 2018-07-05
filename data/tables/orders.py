from data.connection import oracle


def getOrderByID(orderID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT o.ORDERDATE,
     o.CLIENTNAME,
     o.CLIENTSURNAME,
     o.CLIENTMAIL,
     o.FK_CANDYREFERENCE_ID,
     o.QUANTITY,
     o.TOTALCOST,
     o.ORDERSTATE,
     c.COUNTRY
     o.TRACKINGNUMBER
     FROM ORDERS o
     LEFT JOIN COUNTRY c ON (c.COUNTRY_ID = o.FK_COUNTRY_ID )
     WHERE (o.ORDER_ID = :ORDER_ID)""", {"ORDER_ID": orderID})

    for ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL, FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY, TRACKINGNUMBER in cursor:
        print(ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL,
              FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY,
              TRACKINGNUMBER)

    cursor.close()
    return


def getOrderByReferenceID(referenceID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT o.ORDERDATE,
     o.CLIENTNAME,
     o.CLIENTSURNAME,
     o.CLIENTMAIL,
     o.FK_CANDYREFERENCE_ID,
     o.QUANTITY,
     o.TOTALCOST,
     o.ORDERSTATE,
     c.COUNTRY
     o.TRACKINGNUMBER
     FROM ORDERS o
     LEFT JOIN COUNTRY c ON (c.COUNTRY_ID = o.FK_COUNTRY_ID )
     WHERE (o.FK_CANDYREFERENCE_ID = :FK_CANDYREFERENCE_ID)""",
        {"FK_CANDYREFERENCE_ID": referenceID})

    for ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL, FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY, TRACKINGNUMBER in cursor:
        print(ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL,
              FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY,
              TRACKINGNUMBER)

    cursor.close()
    return


def getOrdersList():
    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT o.ORDERDATE,
     o.CLIENTNAME,
     o.CLIENTSURNAME,
     o.CLIENTMAIL,
     o.FK_CANDYREFERENCE_ID,
     o.QUANTITY,
     o.TOTALCOST,
     o.ORDERSTATE,
     c.COUNTRY
     o.TRACKINGNUMBER
     FROM ORDERS o
     LEFT JOIN COUNTRY c ON (c.COUNTRY_ID = o.FK_COUNTRY_ID )
     """)

    for ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL, FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY, TRACKINGNUMBER in cursor:
        print(ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL,
              FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY,
              TRACKINGNUMBER)

    cursor.close()
    return


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
