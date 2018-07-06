from data.connection import oracle


def getVariantByID(variantID=0):  # Returns a variant a given variant ID as a parameter
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT v.VARIANTNAME
     FROM VARIANT v
     WHERE (v.VARIANT_ID = :VARIANT_ID)""", {"VARIANT_ID": variantID})

    result = cursor.fetchall()
    cursor.close()
    return result


def getVariantByName(variantName=""): # Returns a variant a given variant name as a parameter
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT v.VARIANT_ID, v.VARIANTNAME
     FROM VARIANT v
     WHERE (v.VARIANTNAME = :VARIANTNAME)""", {"VARIANTNAME": variantName})

    result = cursor.fetchall()
    cursor.close()
    return result


def getVariantsList():  # Returns the variants list
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT v.VARIANTNAME
     FROM VARIANT v
    """)

    result = cursor.fetchall()
    cursor.close()
    return result
