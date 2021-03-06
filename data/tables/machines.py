from data.connection import oracle


def getMachineByID(machineID=0):  # Returns a Machine for a given machine ID as a parameter
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    result = cursor.fetchall()
    cursor.close()
    return result


def getMachineByVariantID(machineVariantID=0): # Returns a machine for a given variant ID as a parameter
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    result = cursor.fetchall()
    cursor.close()
    return result


def getMachineByPackagingID(machinePackagingID=0): # Returns a machine for a given packaging ID as a parameter
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

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

    result = cursor.fetchall()
    cursor.close()
    return result


def getMachinesList(): # Returns the machine list
    connection = oracle.connectToOracle()
    cursor = connection.cursor()

    cursor.execute("""
     SELECT m.MACHINENUMBER,
     m.CADENCE,
     m.MACHINEDELAY,
     v.VARIANTNAME, 
     p.PACKAGINGNAME
     FROM MACHINE m
     LEFT JOIN VARIANT v ON (v.VARIANT_ID = m.FK_VARIANT_ID)
     LEFT JOIN PACKAGING p ON (p.PACKAGING_ID = m.FK_PACKAGING_ID)
    """)

    result = cursor.fetchall()
    cursor.close()
    return result
