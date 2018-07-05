from data.connection import oracle


def getColorByID(colorID=0):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT c.COLORNAME
     FROM COLOR c
     WHERE (c.COLOR_ID = :COLOR_ID)""", {"COLOR_ID": colorID})

    result = cursor.fetchall()
    cursor.close()
    return result


def getColorByName(colorName=""):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT c.COLOR_ID, c.COLORNAME
     FROM COLOR c
     WHERE (c.COLORNAME = :COLORNAME)""", {"COLORNAME": colorName})

    result = cursor.fetchall()
    cursor.close()
    return result


def getColorsList():
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT c.COLORNAME
     FROM COLOR c
    """)

    result = cursor.fetchall()
    cursor.close()
    return result
