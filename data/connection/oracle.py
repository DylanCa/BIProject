from local_config import oracle_username, oracle_password, oracle_address, oracle_database_name

import random
import cx_Oracle


def connectToOracle():
    connection = cx_Oracle.connect(
        oracle_username,
        oracle_password,
        "{}/{}".format(oracle_address, oracle_database_name),
        mode=cx_Oracle.SYSDBA)

    return connection.cursor()


def disconnectFromOracle():
    connection.commit()
    connection.close()


def getAmountOrdered():
    return random.randint(1, 100)