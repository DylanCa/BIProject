from data.connection import oracle
from data.tables import candies


def getStockByID(stockID=0):  # Returns a component stock for a given stock ID as a parameter
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


def getStockByComponent(component="UNKNOWN"): # Returns a component stock for a given component name as a parameter
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


def getStocksList(): # Returns the stock list
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


def updateStockQuantityByCandyName(candyName="UNKNOWN", totalQuantity=0): # Updates the stock quantity according to a given candy composition * total quantity required given as a parameter

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    results = candies.getCandyByName(candyName)[0]

    quantities = [results[2], results[3], results[4], results[5], results[6]]
    
    component = ['additive', 'coating', 'aroma', 'gelling', 'sugar']

    for x in range(0, len(component)):
        query = """UPDATE STOCK
            SET PALETTEG = ( SELECT PALETTEG FROM STOCK WHERE COMPONENT = '{}') - {}
            WHERE COMPONENT = '{}'""".format(component[x], quantities[x] * totalQuantity,
                                             component[x])

        cursor.execute(query)
        connection.commit()
