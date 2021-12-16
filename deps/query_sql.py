from mysql.connector import MySQLConnection, Error
from greenhos.mysql_dbconfig import read_db_config

def end_query():
    """end_query."""
    cursor.close()
    conn.close()


def insert_nilai_DHT(sensorHumidit, sensorTemp):
    """insert_nilai_DHT.

    :param sensorHumidit: data sensor humadity dari DHT
    :param sensorTemp: data sensor suhu dari DHT
    """
    query = "INSERT INTO dht_sensor(humidity,temp) " \
            "VALUES(%s,%s)"
    args = (sensorHumidit, sensorTemp)
    try:
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

def insert_nilai_SOIL(moisture):
    """insert_nilai_SOIL.

    :param moisture: data bacaan sensor dari Soil Moisture sensor
    """
    query = "INSERT INTO soil_sensor(moisture) " \
            "VALUES(%s,%s)"
    args = (moisture)
    try:
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

def insert_nilai_lain(jarak,cahaya):
    """insert_nilai_lain.

    :param jarak: data bacaan jarak pada sensor HCSR04
    :param cahaya: data bacaan cahaya masuk pada sensor LDR
    """
    query = "INSERT INTO sensor_etc(jarak,cahaya) " \
            "VALUES(%s,%s)"
    args = (jarak,cahaya)
    try:
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

def insert_nilai_relay(relay1,relay2,relay3,relay4):
    """insert_nilai_relay.

    :param relay1: data kondisi relay1
    :param relay2: data kondisi relay2
    :param relay3: data kondisi relay3
    :param relay4: data kondisi relay4
    """
    query = "INSERT INTO relay(relayone,relaytwo,relaythree,relayfour) " \
            "VALUES(%s,%s)"
    args = (relay1,relay2,relay3,relay4)
    try:
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)


db_config = read_db_config()
conn = MySQLConnection(**db_config)
cursor = conn.cursor()
