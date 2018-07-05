from data.connection import oracle


def getStockByID(stockID=0):
    cursor = oracle.connectToOracle()

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
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT s.COMPONENT,
     s.CONDITIONNEMENTKG,
     s.PALETTEKG
     FROM STOCK s
     WHERE (s.COMPONENT = :COMPONENT)""", {"COMPONENT": component})

    for COMPONENT, CONDITIONNEMENTKG, PALETTEKG in cursor:
        print(COMPONENT, CONDITIONNEMENTKG, PALETTEKG)

    cursor.close()
    return


def getStockList():
    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT s.COMPONENT,
     s.CONDITIONNEMENTKG,
     s.PALETTEKG
     FROM STOCK s
    """)

    for COMPONENT, CONDITIONNEMENTKG, PALETTEKG in cursor:
        print(COMPONENT, CONDITIONNEMENTKG, PALETTEKG)

    cursor.close()
    return
