from data.connection import oracle


def getTextureByID(textureID=0):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT t.TEXTURENAME
     FROM TEXTURE t
     WHERE (t.TEXTURE_ID = :TEXTURE_ID)""", {"TEXTURE_ID": textureID})

    result = cursor.fetchall()
    cursor.close()
    return result


def getTextureByName(textureName=""):
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT t.TEXTURE_ID, t.TEXTURENAME
     FROM TEXTURE t
     WHERE (t.TEXTURENAME = :TEXTURENAME)""", {"TEXTURENAME": textureName})

    result = cursor.fetchall()
    cursor.close()
    return result


def getTexturesList():
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT t.TEXTURENAME
     FROM TEXTURE t
    """)

    result = cursor.fetchall()
    cursor.close()
    return result
