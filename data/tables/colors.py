from data.connection import oracle


def getColorByID(colorID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT c.COLORNAME
     FROM COLOR c
     WHERE (c.COLOR_ID = :COLOR_ID)""", {"COLOR_ID": colorID})

    for COLORNAME in cursor:
        print(COLORNAME)

    cursor.close()
    return


def getColorsList():
    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT c.COLORNAME
     FROM COLOR c
    """)

    for COLORNAME in cursor:
        print(COLORNAME)

    cursor.close()
    return
