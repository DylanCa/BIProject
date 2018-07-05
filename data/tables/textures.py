from data.connection import oracle


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
