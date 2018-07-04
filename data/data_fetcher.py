from data.connection import oracle


def getCountryByName(countryname=""):

    cursor = oracle.connectToOracle()

    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT c.COUNTRYNAME, p.PACKAGINGNAME
     FROM COUNTRY c 
     LEFT JOIN PACKAGING p ON (c.FK_PACKAGING_ID = p.PACKAGING_ID )
     WHERE (c.COUNTRYNAME = :COUNTRYNAME)""", {"COUNTRYNAME": countryname})

    for COUNTRYNAME, PACKAGINGNAME in cursor:
        print(COUNTRYNAME, PACKAGINGNAME)

    cursor.close()
    return


def getCountryByID(countryID=0):

    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT c.COUNTRYNAME, p.PACKAGINGNAME
     FROM COUNTRY c 
     LEFT JOIN PACKAGING p ON (c.FK_PACKAGING_ID = p.PACKAGING_ID )
     WHERE (c.COUNTRY_ID = :COUNTRY_ID)""", {"COUNTRY_ID": countryID})

    for COUNTRYNAME, PACKAGINGNAME in cursor:
        print(COUNTRYNAME, PACKAGINGNAME)

    cursor.close()
    return


def getCountriesList():

    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT c.COUNTRYNAME, p.PACKAGINGNAME
     FROM COUNTRY c 
     LEFT JOIN PACKAGING p ON (c.FK_PACKAGING_ID = p.PACKAGING_ID )
     """)

    for COUNTRYNAME, PACKAGINGNAME in cursor:
        print(COUNTRYNAME, PACKAGINGNAME)

    cursor.close()
    return


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

    for CANDYNAME, ADDITIVE, COATING, AROMA, GELLING, SUGAR in cursor:
        print(CANDYNAME, ADDITIVE, COATING, AROMA, GELLING, SUGAR)

    cursor.close()
    return


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


def getTextureByID(textureID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT t.TEXTURENAME
     FROM TEXTURE t
     WHERE (t.TEXTURE_ID = :TEXTURE_ID)""", {"TEXTURE_ID": textureID})

    for VARIANTNAME in cursor:
        print(VARIANTNAME)

    cursor.close()
    return


def getTexturesList():
    cursor = oracle.connectToOracle()

    cursor.execute("""
     SELECT t.TEXTURENAME
     FROM TEXTURE t
    """)

    for VARIANTNAME in cursor:
        print(VARIANTNAME)

    cursor.close()
    return


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


def getPackagingByName(packagingName=""): # TODO: CORRECT IT
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT p.CONTENT, p.FK_PALETTE_ID
     FROM PACKAGING p
     WHERE (p.PACKAGINGNAME = :PACKAGINGNAME)""",
        {"PACKAGINGNAME": packagingName})

    result = cursor.fetchall()

    if len(result) != 0:
        if int(result[0][1]) == 1:
            cursor.execute(
                """
                SELECT p.PACKAGINGNAME as Container, pal.PALETTENAME as Content, p.QUANTITY, pal.PLANEQUANTITY as CardboardsPerPlane, pal.BOATQUANTITY as CardboardsPerBoat, pal.TRUCKQUANTITY as CardboardsPerTruck
                FROM PACKAGING p
                LEFT JOIN PALETTE pal ON (p.FK_PALETTE_ID = pal.PALETTE_ID)
                WHERE (p.PACKAGINGNAME = :PACKAGINGNAME)""",
                {"PACKAGINGNAME": packagingName})

        elif int(result[0][0]) == 1:
            cursor.execute(
                """
            SELECT p.PACKAGINGNAME as Container, pack.PACKAGINGNAME as Content, p.QUANTITY
            FROM PACKAGING p
            LEFT JOIN PACKAGING pack ON (p.CONTENT = pack.PACKAGING_ID)
            WHERE (p.PACKAGINGNAME = :PACKAGINGNAME)""",
                {"PACKAGINGNAME": packagingName})

    else:

        cursor.execute(
            """
        SELECT p.PALETTENAME as Container, c.CARDBOARDNAME as Content, p.BOATQUANTITY as CardbardsInBoat, p.TRUCKQUANTITY as CardbardsInTruck, p.PLANEQUANTITY as CardbardsInPlane
        FROM PALETTE p
        LEFT JOIN CARDBOARD c ON (p.FK_CARDBOARD_ID = c.CARDBOARD_ID)
        WHERE (p.PALETTENAME = :PALETTENAME)""",
            {"PALETTENAME": packagingName})

        result = cursor.fetchall()

        if len(result) != 1:
            cursor.execute(
                """
                SELECT c.CARDBOARDNAME, c.SAMPLEQUANTITY as SamplesPerCardboard, c.BAGQUANTITY as BagsPerCardboard, c.BOXQUANTITY as BoxesPerCardboard
                FROM CARDBOARD c
                WHERE (c.CARDBOARDNAME = :CARDBOARDNAME)""",
                {"CARDBOARDNAME": packagingName})
     
    result = cursor.fetchall()
    print(result)
    cursor.close()
    return


def getCandyReferenceByID(candyReferenceID=0): # TODO: FINISH IT
    pass


def getCandyReferenceByCompositionID(colorID=0,
                                     textureID=0,
                                     variantID=0,
                                     packagingID=0):  # TODO: FINISH IT
    pass


def getOrderByID(orderID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT o.ORDERDATE,
     o.CLIENTNAME,
     o.CLIENTSURNAME,
     o.CLIENTMAIL,
     o.FK_CANDYREFERENCE_ID,
     o.QUANTITY,
     o.TOTALCOST,
     o.ORDERSTATE,
     c.COUNTRY
     o.TRACKINGNUMBER
     FROM ORDERS o
     LEFT JOIN COUNTRY c ON (c.COUNTRY_ID = o.FK_COUNTRY_ID )
     WHERE (o.ORDER_ID = :ORDER_ID)""", {"ORDER_ID": orderID})

    for ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL, FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY, TRACKINGNUMBER in cursor:
        print(ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL,
              FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY,
              TRACKINGNUMBER)

    cursor.close()
    return


def getOrderByReferenceID(referenceID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT o.ORDERDATE,
     o.CLIENTNAME,
     o.CLIENTSURNAME,
     o.CLIENTMAIL,
     o.FK_CANDYREFERENCE_ID,
     o.QUANTITY,
     o.TOTALCOST,
     o.ORDERSTATE,
     c.COUNTRY
     o.TRACKINGNUMBER
     FROM ORDERS o
     LEFT JOIN COUNTRY c ON (c.COUNTRY_ID = o.FK_COUNTRY_ID )
     WHERE (o.FK_CANDYREFERENCE_ID = :FK_CANDYREFERENCE_ID)""",
        {"FK_CANDYREFERENCE_ID": referenceID})

    for ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL, FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY, TRACKINGNUMBER in cursor:
        print(ORDERDATE, CLIENTNAME, CLIENTSURNAME, CLIENTMAIL,
              FK_CANDYREFERENCE_ID, QUANTITY, TOTALCOST, ORDERSTATE, COUNTRY,
              TRACKINGNUMBER)

    cursor.close()
    return


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


def getMachineByID(machineID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT m.MACHINENUMBER,
     m.CADENCE,
     m.MACHINEDELAY,
     v.VARIANTNAME,
     p.PACKAGINGNAME
     FROM MACHINE m
     LEFT JOIN VARIANT v ON (v.VARIANT_ID = m.FK_VARIANT_ID)
     LEFT JOIN PACKAGING p ON (p.PACKAGING_ID = m.FK_PACKAGING_ID)

     WHERE (m.MACHINE_ID = :MACHINE_ID)""", {"MACHINE_ID": machineID})

    for MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME in cursor:
        print(MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME)

    cursor.close()
    return


def getMachineByVariantID(machineVariantID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT m.MACHINENUMBER,
     m.CADENCE,
     m.MACHINEDELAY,
     v.VARIANTNAME,
     p.PACKAGINGNAME
     FROM MACHINE m
     LEFT JOIN VARIANT v ON (v.VARIANT_ID = m.FK_VARIANT_ID)
     LEFT JOIN PACKAGING p ON (p.PACKAGING_ID = m.FK_PACKAGING_ID)

     WHERE (v.VARIANT_ID = :VARIANT_ID)""", {"VARIANT_ID": machineVariantID})

    for MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME in cursor:
        print(MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME)

    cursor.close()
    return


def getMachineByPackagingID(machinePackagingID=0):
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT m.MACHINENUMBER,
     m.CADENCE,
     m.MACHINEDELAY,
     v.VARIANTNAME,
     p.PACKAGINGNAME
     FROM MACHINE m
     LEFT JOIN VARIANT v ON (v.VARIANT_ID = m.FK_VARIANT_ID)
     LEFT JOIN PACKAGING p ON (p.PACKAGING_ID = m.FK_PACKAGING_ID)

     WHERE (p.PACKAGING_ID = :PACKAGING_ID)""",
        {"PACKAGING_ID": machinePackagingID})

    for MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME in cursor:
        print(MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME)

    cursor.close()
    return


def getMachinesList():
    cursor = oracle.connectToOracle()

    cursor.execute(
        """
     SELECT m.MACHINENUMBER,
     m.CADENCE,
     m.MACHINEDELAY,
     v.VARIANTNAME, 
     p.PACKAGINGNAME
     FROM MACHINE m
     LEFT JOIN VARIANT v ON (v.VARIANT_ID = m.FK_VARIANT_ID)
     LEFT JOIN PACKAGING p ON (p.PACKAGING_ID = m.FK_PACKAGING_ID)
    """)

    for MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME in cursor:
        print(MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME)

    cursor.close()
    return