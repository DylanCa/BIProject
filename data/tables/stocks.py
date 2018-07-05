from data.connection import oracle


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
