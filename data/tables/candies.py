from data.connection import oracle


def getCandyByName(candyName=""):

    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT c.CANDYNAME, c.ADDITIVE, c.COATING, c.AROMA, c.GELLING, c.SUGAR
     FROM CANDY c
     WHERE (c.CANDYNAME = :CANDYNAME)""", {"CANDYNAME": candyName})

    for CANDYNAME, ADDITIVE, COATING, AROMA, GELLING, SUGAR in cursor:
        print(CANDYNAME, ADDITIVE, COATING, AROMA, GELLING, SUGAR)

    cursor.close()
    return


def getCandyByID(candyID=0):

    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT c.CANDYNAME, c.ADDITIVE, c.COATING, c.AROMA, c.GELLING, c.SUGAR
     FROM CANDY c
     WHERE (c.CANDY_ID = :CANDY_ID)""", {"CANDY_ID": candyID})

    for CANDYNAME, ADDITIVE, COATING, AROMA, GELLING, SUGAR in cursor:
        print(CANDYNAME, ADDITIVE, COATING, AROMA, GELLING, SUGAR)

    cursor.close()
    return


def getCandiesList():

    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT c.CANDYNAME, c.ADDITIVE, c.COATING, c.AROMA, c.GELLING, c.SUGAR
     FROM CANDY c
     """)
    results = cursor.fetchall[0]

    cursor.close()
    return results


def getCandyCostByName(candyName=""):

    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT c.CANDYNAME, 
        cost.manufacturePercentage, 
        cost.contioningPercentage, 
        cost.shippingPercentage,
        cost.generalPercentage, 
        cost.sampleCost, 
        cost.bagCost, 
        cost.boxCost
     FROM CANDY c
     LEFT JOIN CANDYCOST cost ON (c.CANDY_ID = cost.CANDYCOST_ID )
     WHERE (c.CANDYNAME = :CANDYNAME)""", {"CANDYNAME": candyName})

    for CANDYNAME, MANUFACTUREPERCENTAGE, CONTIONINGPERCENTAGE, SHIPPINGPERCENTAGE, GENERALPERCENTAGE, SAMPLECOST, BAGCOST, BOXCOST in cursor:
        print(CANDYNAME, MANUFACTUREPERCENTAGE, CONTIONINGPERCENTAGE,
              SHIPPINGPERCENTAGE, GENERALPERCENTAGE, SAMPLECOST, BAGCOST,
              BOXCOST)
    cursor.close()
    return


def getCandyCostByID(candyID=0):

    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT c.CANDYNAME, 
        cost.manufacturePercentage, 
        cost.contioningPercentage, 
        cost.shippingPercentage,
        cost.generalPercentage, 
        cost.sampleCost, 
        cost.bagCost, 
        cost.boxCost
     FROM CANDY c
     LEFT JOIN CANDYCOST cost ON (c.CANDY_ID = cost.CANDYCOST_ID )
     WHERE (c.CANDY_ID = :CANDY_ID)""", {"CANDY_ID": candyID})

    for CANDYNAME, MANUFACTUREPERCENTAGE, CONTIONINGPERCENTAGE, SHIPPINGPERCENTAGE, GENERALPERCENTAGE, SAMPLECOST, BAGCOST, BOXCOST in cursor:
        print(CANDYNAME, MANUFACTUREPERCENTAGE, CONTIONINGPERCENTAGE,
              SHIPPINGPERCENTAGE, GENERALPERCENTAGE, SAMPLECOST, BAGCOST,
              BOXCOST)

    cursor.close()
    return


def getCandyCostsList():

    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT c.CANDYNAME, 
        cost.manufacturePercentage, 
        cost.contioningPercentage, 
        cost.shippingPercentage,
        cost.generalPercentage, 
        cost.sampleCost, 
        cost.bagCost, 
        cost.boxCost
     FROM CANDY c
     LEFT JOIN CANDYCOST cost ON (c.CANDY_ID = cost.CANDYCOST_ID )
     """)

    for CANDYNAME, MANUFACTUREPERCENTAGE, CONTIONINGPERCENTAGE, SHIPPINGPERCENTAGE, GENERALPERCENTAGE, SAMPLECOST, BAGCOST, BOXCOST in cursor:
        print(CANDYNAME, MANUFACTUREPERCENTAGE, CONTIONINGPERCENTAGE,
              SHIPPINGPERCENTAGE, GENERALPERCENTAGE, SAMPLECOST, BAGCOST,
              BOXCOST)
    cursor.close()
    return


def getCandyReferenceByID(candyReferenceID=0):  # TODO: FINISH IT
    pass


def getCandyReferenceByCompositionID(colorID=0,
                                     textureID=0,
                                     variantID=0,
                                     packagingID=0):  # TODO: FINISH IT
    pass