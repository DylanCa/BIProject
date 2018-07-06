from data.connection import oracle


def getCountryByName(countryname=""): # Returns a Country for a given country name as a parameter

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT c.COUNTRY_ID, c.COUNTRYNAME, p.PACKAGINGNAME
     FROM COUNTRY c
     LEFT JOIN PACKAGING p ON (c.FK_PACKAGING_ID = p.PACKAGING_ID )
     WHERE (c.COUNTRYNAME = :COUNTRYNAME)""", {"COUNTRYNAME": countryname})

    result = cursor.fetchall()
    cursor.close()
    return result


def getCountryByID(countryID=0):  # Returns a Country for a given country ID as a parameter

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute(
        """
     SELECT c.COUNTRYNAME, p.PACKAGINGNAME
     FROM COUNTRY c
     LEFT JOIN PACKAGING p ON (c.FK_PACKAGING_ID = p.PACKAGING_ID )
     WHERE (c.COUNTRY_ID = :COUNTRY_ID)""", {"COUNTRY_ID": countryID})

    result = cursor.fetchall()
    cursor.close()
    return result


def getCountriesList(): # Return the country list

    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT c.COUNTRYNAME, p.PACKAGINGNAME
     FROM COUNTRY c
     LEFT JOIN PACKAGING p ON (c.FK_PACKAGING_ID = p.PACKAGING_ID )
     """)

    result = cursor.fetchall()
    cursor.close()
    return result
