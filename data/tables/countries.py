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
