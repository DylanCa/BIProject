from data.connection import oracle


def getVariantByID(variantID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT v.VARIANTNAME
     FROM VARIANT v
     WHERE (v.VARIANT_ID = :VARIANT_ID)""", {"VARIANT_ID": variantID})

    for VARIANTNAME in cursor:
        print(VARIANTNAME)

    cursor.close()
    return


def getVariantsList():
    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT v.VARIANTNAME
     FROM VARIANT v
    """)

    for VARIANTNAME in cursor:
        print(VARIANTNAME)

    cursor.close()
    return
