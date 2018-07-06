from data.connection import oracle


def getColorByID(colorID=0): # Returns a Color for a given color ID as a parameter
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


def getColorByName(colorName=""):  # Returns a Color for a given color Name as a parameter
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


def getColorsList(): # Returns the color list
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT c.COLORNAME
     FROM COLOR c
    """)

    result = cursor.fetchall()
    cursor.close()
    return result
