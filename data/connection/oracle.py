from local_config import oracle_username, oracle_password, oracle_address, oracle_database_name

import random
import cx_Oracle # External Library used to connect Python to a Oracle Database

 
def connectToOracle(): # Enables a connection to the Oracle DB and returns this connection
    connection = cx_Oracle.connect(
        oracle_username,
        oracle_password,
        "{}/{}".format(oracle_address, oracle_database_name),
        mode=cx_Oracle.SYSDBA)

    return connection


def disconnectFromOracle(connection): # Disconnects the given connection from Oracle
    connection.commit()
    connection.close()
