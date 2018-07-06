from data.connection import oracle


def getPackagingByName(packagingName=""):  # Returns the packaging according to the packaging Name given as a parameter
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT p.PACKAGING_ID, p.CONTENT, p.FK_PALETTE_ID
     FROM PACKAGING p
     WHERE (p.PACKAGINGNAME = :PACKAGINGNAME)""",
        {"PACKAGINGNAME": packagingName})

    result = cursor.fetchall()

    if len(result) != 0:
        if int(result[0][1]) == 1:
            cursor.execute(
                """
                SELECT p.PACKAGING_ID, p.PACKAGINGNAME as Container, pal.PALETTENAME as Content, p.QUANTITY, pal.PLANEQUANTITY as CardboardsPerPlane, pal.BOATQUANTITY as CardboardsPerBoat, pal.TRUCKQUANTITY as CardboardsPerTruck
                FROM PACKAGING p
                LEFT JOIN PALETTE pal ON (p.FK_PALETTE_ID = pal.PALETTE_ID)
                WHERE (p.PACKAGINGNAME = :PACKAGINGNAME)""",
                {"PACKAGINGNAME": packagingName})

        elif int(result[0][0]) == 1:
            cursor.execute(
                """
            SELECT p.PACKAGING_ID, p.PACKAGINGNAME as Container, pack.PACKAGINGNAME as Content, p.QUANTITY
            FROM PACKAGING p
            LEFT JOIN PACKAGING pack ON (p.CONTENT = pack.PACKAGING_ID)
            WHERE (p.PACKAGINGNAME = :PACKAGINGNAME)""",
                {"PACKAGINGNAME": packagingName})

    else:

        cursor.execute(
            """
        SELECT p.PALETTE_ID, p.PALETTENAME as Container, c.CARDBOARDNAME as Content, p.BOATQUANTITY as CardbardsInBoat, p.TRUCKQUANTITY as CardbardsInTruck, p.PLANEQUANTITY as CardbardsInPlane
        FROM PALETTE p
        LEFT JOIN CARDBOARD c ON (p.FK_CARDBOARD_ID = c.CARDBOARD_ID)
        WHERE (p.PALETTENAME = :PALETTENAME)""",
            {"PALETTENAME": packagingName})

        result = cursor.fetchall()

        if len(result) != 1:
            cursor.execute(
                """
                SELECT c.CARDBOARD_ID, c.CARDBOARDNAME, c.SAMPLEQUANTITY as SamplesPerCardboard, c.BAGQUANTITY as BagsPerCardboard, c.BOXQUANTITY as BoxesPerCardboard
                FROM CARDBOARD c
                WHERE (c.CARDBOARDNAME = :CARDBOARDNAME)""",
                {"CARDBOARDNAME": packagingName})

    result = cursor.fetchall()
    cursor.close()
    return result
