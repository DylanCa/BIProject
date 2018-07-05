from data.connection import oracle


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

    for MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME in cursor:
        print(MACHINENUMBER, CADENCE, MACHINEDELAY, VARIANTNAME, PACKAGINGNAME)

    cursor.close()
    return