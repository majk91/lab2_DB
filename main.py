import sys

import controller.myController as Controller
import dbContext as DB

if __name__ == '__main__':

    conn = DB.connect()
    if conn is None:
        print(DB.myMessage)
        sys.exit()

    # TODO:  3. Поиск по нескольким атрибутам из разных таблиц (для числа - диапазон, для строк - LIKE, bool - true/false)

    print("Chose select filter: \n "
          "1. get events by title\n "
          "2. get events by date from 2012-04-01 to 2012-11-01\n "
          "3. get venues by privat type")
    val = int(input())
    if val == 1:  # просим ввести часть слова для поиска
        print("input search part of word (for example LARP)")
        titleVal = input()
        Controller.getDataFromDb(conn,
            "SELECT events.*, venues.country_code, countries.country_name FROM events "
            "JOIN venues ON events.venue_id = venues.venue_id "
            "JOIN countries ON countries.country_code = venues.country_code "
            "WHERE events.title LIKE '%" + titleVal + "%' AND events.venue_id >= 2")
    elif val == 2:
        Controller.getDataFromDb(conn,
            "SELECT events.* FROM events WHERE starts >= '2012-04-01' AND starts   <= '2012-11-01'")
    elif val == 3:
        print("input privat type (true/false)")
        titleVal = input()
        if titleVal == "true" | titleVal == "false":
            Controller.getDataFromDb(conn,
                "SELECT venues.*, countries.country_name FROM venues "
                "JOIN countries ON countries.country_code = venues.country_code "
                "WHERE venues.private=" + titleVal)
    else:
        print("WORNING! You did not select correct menu item. Program is continue.")

    # TODO: додавання
    print("\nTo start adding row to venues input eny char")
    input()
    print("\nShow all old cities row")
    Controller.getDataFromDb(conn, "SELECT * FROM cities;")
    code1 = "00000"
    code2 = "00001"
    Controller.addDataToDb(conn, "INSERT INTO cities VALUES('NY', '"+code1+"', 'us')")
    Controller.addDataToDb(conn, "INSERT INTO cities VALUES('HollyWood', '"+code2+"', 'us')")
    print("\nShow all new cities rows")
    Controller.getDataFromDb(conn, "SELECT * FROM cities")

    # TODO: редагування
    print("\nTo UPDATE cities input eny char")
    input()
    Controller.updateData(conn, "UPDATE cities SET postal_code = '11111' WHERE postal_code = '"+code1+"'")
    Controller.updateData(conn, "UPDATE cities SET postal_code = '22222' WHERE postal_code = '"+code2+"'")
    print("\nShow all new cities row")
    Controller.getDataFromDb(conn, "SELECT * FROM cities")

    # TODO: видалення
    print("\nTo REMOVE cities input eny char")
    input()
    Controller.removeCityByPostCode(conn, "11111")
    Controller.removeCityByPostCode(conn, "22222")
    print("Show all cities:")
    Controller.getDataFromDb(conn, "SELECT * FROM cities")

    # TODO: при видаленні видаляти підлеглі
    print("\nShow all old venues row")
    Controller.addDataToDb(conn, "INSERT INTO cities VALUES('HollyWood', '00000', 'us')")
    Controller.addDataToDb(conn, "INSERT INTO venues (name, postal_code, country_code) "
                                 "VALUES ('New event us', '00000', 'us')")

    Controller.getDataFromDb(conn, "SELECT * FROM venues;")
    print("\nShow all old country row")
    Controller.getDataFromDb(conn, "SELECT * FROM cities")

    print("\nTo REMOVE country with link input postal_code")
    postalCode = input()
    Controller.removeSityByCode(conn, postalCode)

    print("Show all venues:")
    Controller.getDataFromDb(conn, "SELECT * FROM venues;")
    print("Show all cities:")
    Controller.getDataFromDb(conn, "SELECT * FROM cities")

    # TODO: генерування рандомних даних  !!!! не мовою програмування, а відповідним SQL-запитом!
    print("\nTo ADD random cities input eny char")
    input()
    Controller.generateRandomCityPostalCode(conn, "LA", "us")
    Controller.generateRandomCityPostalCode(conn, "LA", "us")
    Controller.generateRandomCityPostalCode(conn, "LA", "us")
    Controller.generateRandomCityPostalCode(conn, "LA", "us")
    Controller.generateRandomCityPostalCode(conn, "LA", "us")
    Controller.generateRandomCityPostalCode(conn, "LA", "us")

    print("Show all cities:")
    Controller.getDataFromDb(conn, "SELECT * FROM cities")

    conn.close()


