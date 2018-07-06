from data.connection import oracle

import time


def getOrderByID(orderID=0):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    result = cursor.fetchall()
    cursor.close()
    return result


def getOrderByReferenceID(referenceID=0):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    result = cursor.fetchall()
    cursor.close()
    return result


def getOrdersList():
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    result = cursor.fetchall()
    cursor.close()
    return result


def createOrder(clientName="UNKNOWN",
                clientSurname="UNKNOWN",
                clientMail="UNKNOWN",
                quantity=0,
                totalCost=0,
                orderState="UNKNOWN",
                trackingNumber=0000,
                countryID=0,
                candyReference=0):

    connection = oracle.connectToOracle()
    cursor = connection.cursor()
          
    cursor.execute(
        """
        INSERT INTO ORDERS(ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL, QUANTITY, TOTALCOST, ORDERSTATE, TRACKINGNUMBER, FK_COUNTRY_ID, FK_CANDYREFERENCE_ID)
        VALUES(TO_TIMESTAMP(:ORDERDATE, 'DD/MM/YYYY hh24:mi:ss'), :CLIENTNAME, :CLIENTSURNAME, :CLIENTMAIL, :QUANTITY, :TOTALCOST, :ORDERSTATE, :TRACKINGNUMBER, :FK_COUNTRY_ID, :FK_CANDYREFERENCE_ID)""",
        {
            "ORDERDATE": time.strftime('%d-%m-%Y %H:%M:%S'),
            "CLIENTNAME": clientName,
            "CLIENTSURNAME": clientSurname,
            "CLIENTMAIL": clientMail,
            "QUANTITY": quantity,
            "TOTALCOST": totalCost,
            "ORDERSTATE": orderState,
            "TRACKINGNUMBER": trackingNumber,
            "FK_COUNTRY_ID": countryID,
            "FK_CANDYREFERENCE_ID": candyReference
        })

    connection.commit()
    cursor.close()
    return True
