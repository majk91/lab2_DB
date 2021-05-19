import time
import psycopg2


def getDataFromDb(conn, query):
    cur = conn.cursor()
    try:

        millis_start = int(round(time.time() * 1000))
        cur.execute(query)
        rows = cur.fetchall()
        millis_end = int(round(time.time() * 1000))
        print("Rows: ")
        for row in rows:
            res = ""
            for item in row:
                res += str(item) + "||"
            print(res)
        print("Request time: 1" + str(millis_end - millis_start) + "ms")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def addDataToDb(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
        # rows = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def updateData(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def removeCityByPostCode(conn, code):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM cities WHERE postal_code = '" + code + "'")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def removeSityByCode(conn, code):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM venues WHERE venues.postal_code = '"+code+"'")
        cur.execute("DELETE FROM cities WHERE cities.postal_code = '"+code+"'")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def generateRandomCityPostalCode(conn, name, code):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO cities(name, postal_code, country_code)  "
                    "VALUES ('"+name+"', "
                        "(SELECT trunc(random()*1000)::int from generate_series(1,1)),"
                        " '"+code+"')")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

