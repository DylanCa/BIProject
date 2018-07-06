from data.connection import oracle
from data.tables import candies


def getStockByID(stockID=0):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT s.COMPONENT,
     s.CONDITIONNEMENTKG,
     s.PALETTEKG
     FROM STOCK s
     WHERE (s.STOCK_ID = :STOCK_ID)""", {"STOCK_ID": stockID})

    for COMPONENT, CONDITIONNEMENTKG, PALETTEKG in cursor:
        print(COMPONENT, CONDITIONNEMENTKG, PALETTEKG)

    cursor.close()
    return


def getStockByComponent(component="UNKNOWN"):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT s.COMPONENT,
     s.CONDITIONNEMENTKG,
     s.PALETTEKG
     FROM STOCK s
     WHERE (s.COMPONENT = :COMPONENT)""", {"COMPONENT": component})

    result = cursor.fetchall()
    cursor.close()
    return result


def getStocksList():
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT s.COMPONENT,
     s.CONDITIONNEMENTKG,
     s.PALETTEKG
     FROM STOCK s
    """)

    result = cursor.fetchall()
    cursor.close()
    return result


def updateStockQuantityByCandyName(candyName="UNKNOWN"):

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    results = candies.getCandyByName(candyName)[0]

    quantities = []
    quantities[0] = results[2]
    quantities[1] = results[3]
    quantities[2] = results[4]
    quantities[3] = results[5]
    quantities[4] = results[6]

    component = []
    component[0] = 'additive'
    component[1] = 'coating'
    component[2] = 'aroma'
    component[3] = 'gelling'
    component[4] = 'sugar'

    for x in range(0, len(component)):
        query = """UPDATE STOCK
            SET PALETTEKG = ( SELECT PALETTEKG FROM STOCK WHERE COMPONENT = '{}') - {}
            WHERE COMPONENT = '{}'""".format(component[x], quantities[x],
                                             component[x])

        cursor.execute(query)
        connection.commit()


def updateStockQuantityByID(stockID=0, quantity=0):

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    query = """UPDATE STOCK
        SET PALETTEKG = ( SELECT PALETTEKG FROM STOCK WHERE STOCK_ID = '{}') - {}
        WHERE STOCK_ID = '{}'""".format(stockID, quantity, stockID)
    cursor.execute(query)

    connection.commit()