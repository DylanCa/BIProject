from local_config import oracle_username, oracle_password, oracle_address, oracle_database_name

import random
import cx_Oracle

 
def connectToOracle():
    connection = cx_Oracle.connect(
        oracle_username,
        oracle_password,
        "{}/{}".format(oracle_address, oracle_database_name),
        mode=cx_Oracle.SYSDBA)

    return connection


def disconnectFromOracle(connection):
    connection.commit()
    connection.close()
