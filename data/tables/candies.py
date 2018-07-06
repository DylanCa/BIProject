from data.connection import oracle
from data.tables import colors, packaging, textures, variants


def getCandyByName(candyName=""): # Returns a candy for a candy name given as a parameter

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT c.CANDY_ID, c.CANDYNAME, c.ADDITIVE, c.COATING, c.AROMA, c.GELLING, c.SUGAR
     FROM CANDY c
     WHERE (c.CANDYNAME = :CANDYNAME)""", {"CANDYNAME": candyName})

    result = cursor.fetchall()
    cursor.close()
    return result


def getCandyByID(candyID=0): # Returns a candy for a candy ID given as a parameter

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT c.CANDYNAME, c.ADDITIVE, c.COATING, c.AROMA, c.GELLING, c.SUGAR
     FROM CANDY c
     WHERE (c.CANDY_ID = :CANDY_ID)""", {"CANDY_ID": candyID})

    result = cursor.fetchall()
    cursor.close()
    return result


def getCandiesList(): # Returns the Candy List

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT c.CANDYNAME, c.ADDITIVE, c.COATING, c.AROMA, c.GELLING, c.SUGAR
     FROM CANDY c
     """)
    results = cursor.fetchall()

    cursor.close()
    return results


def getCandyCostByName(candyName=""): # Returns a candy cost for a candy name given as a parameter

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    result = cursor.fetchall()
    cursor.close()
    return result


def getCandyCostByID(candyID=0): # Returns a candy cost for a candy ID given as a parameter

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT c.CANDY_ID,
        c.CANDYNAME, 
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

    result = cursor.fetchall()
    cursor.close()
    return result


def getCandyCostsList(): # Returns a candy costs List

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    results = cursor.fetchall()

    return results


def getCandyReferenceByID(candyReferenceID=0): # Returns a candy reference if exists for a given reference ID
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT cr.CANDYSTOCK,
            cr.READYTOPACK,
            cr.READYBOX,
            cr.READYBAG,
            cr.READYSAMPLE,
            candy.CANDYNAME,
            color.COLORNAME,
            text.TEXTURENAME,
            var.VARIANTNAME,
            pack.PACKAGINGNAME
        FROM CANDYREFERENCES cr
        LEFT JOIN CANDY candy ON (candy.CANDY_ID = cr.FK_CANDY_ID)
        LEFT JOIN COLOR color ON (color.COLOR_ID = cr.FK_COLOR_ID)
        LEFT JOIN TEXTURE text ON (text.TEXTURE_ID = cr.FK_TEXTURE_ID)
        LEFT JOIN VARIANT var ON (var.VARIANT_ID = cr.FK_VARIANT_ID)
        LEFT JOIN PACKAGING pack ON (pack.PACKAGING_ID = cr.FK_PACKAGING_ID)
        WHERE (cr.CANDYREFERENCE_ID = :CANDYREFERENCEID)""",
        {"CANDYREFERENCEID": candyReferenceID})

    results = cursor.fetchall()

    return results


def getCandyReferenceByCompositionID(candyID=0,
                                     colorID=0,
                                     textureID=0,
                                     variantID=0,
                                     packagingID=0):  # Returns a candy reference if exists for a given composition ID
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT cr.CANDYREFERENCE_ID,
            cr.CANDYSTOCK,
            cr.READYTOPACK,
            cr.READYBOX,
            cr.READYBAG,
            cr.READYSAMPLE,
            candy.CANDYNAME,
            color.COLORNAME,
            text.TEXTURENAME,
            var.VARIANTNAME,
            pack.PACKAGINGNAME
        FROM CANDYREFERENCES cr
        LEFT JOIN CANDY candy ON (candy.CANDY_ID = cr.FK_CANDY_ID)
        LEFT JOIN COLOR color ON (color.COLOR_ID = cr.FK_COLOR_ID)
        LEFT JOIN TEXTURE text ON (text.TEXTURE_ID = cr.FK_TEXTURE_ID)
        LEFT JOIN VARIANT var ON (var.VARIANT_ID = cr.FK_VARIANT_ID)
        LEFT JOIN PACKAGING pack ON (pack.PACKAGING_ID = cr.FK_PACKAGING_ID)
        WHERE (cr.FK_CANDY_ID = :FK_CANDY_ID AND
            cr.FK_COLOR_ID = :FK_COLOR_ID AND
            cr.FK_TEXTURE_ID = :FK_TEXTURE_ID AND
            cr.FK_VARIANT_ID = :FK_VARIANT_ID AND
            cr.FK_PACKAGING_ID = :FK_PACKAGING_ID)""", {
            "FK_CANDY_ID": candyID,
            "FK_COLOR_ID": colorID,
            "FK_TEXTURE_ID": textureID,
            "FK_VARIANT_ID": variantID,
            "FK_PACKAGING_ID": packagingID
        })

    results = cursor.fetchall()
    cursor.close()
    return results


def createCandyReferenceByID(candyID=0,
                             colorID=0,
                             textureID=0,
                             variantID=0,
                             packagingID=0): # Creates a Candy Reference for given composition IDs
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    ref = getCandyReferenceByCompositionID(candyID, colorID, textureID,
                                           variantID, packagingID)
    if not ref:
        cursor.execute(
            """
        INSERT INTO CANDYREFERENCES(FK_CANDY_ID, FK_COLOR_ID, FK_TEXTURE_ID, FK_VARIANT_ID, FK_PACKAGING_ID)
        VALUES(:FK_CANDY_ID, :FK_COLOR_ID, :FK_TEXTURE_ID, :FK_VARIANT_ID, :FK_PACKAGING_ID)""",
            {
                "FK_CANDY_ID": candyID,
                "FK_COLOR_ID": colorID,
                "FK_TEXTURE_ID": textureID,
                "FK_VARIANT_ID": variantID,
                "FK_PACKAGING_ID": packagingID
            })
        connection.commit()
        cursor.close()
        ref = getCandyReferenceByCompositionID(candyID, colorID, textureID,
                                               variantID, packagingID)

    return ref


def createCandyReferenceByName(candyName="UNKNOWN",
                               colorName="UNKNOWN",
                               textureName="UNKNOWN",
                               variantName="UNKNOWN",
                               packagingName="UNKNOWN"):  # Creates a Candy Reference for given composition Names

    candyID = getCandyByName(candyName)[0][0]
    colorID = colors.getColorByName(colorName)[0][0]
    textureID = textures.getTextureByName(textureName)[0][0]
    variantID = variants.getVariantByName(variantName)[0][0]
    packagingID = packaging.getPackagingByName(packagingName)[0][0]

    return createCandyReferenceByID(
        candyID=candyID,
        colorID=colorID,
        textureID=textureID,
        variantID=variantID,
        packagingID=packagingID)
