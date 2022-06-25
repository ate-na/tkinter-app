import sqlite3
import random
import string


plane_name_list = [
    'Airbus A310',
    'Boeing 727',
    'Convair 880',
    'Irkut MC-21',
    'Airbus A318',
    'Boeing 757',
    'Dassault Mercure',
    'Lockheed L-1011',
    'Airbus A380',
    'Boeing 767',
    'Douglas DC-8',
    'Vickers VC10',
    'BAC One-Eleven',
    'Comac C919',
    'Ilyushin Il-86',
    'Airbus A321'
]
airline_name_list = [
            'Iran Air',
            'Iran Aseman Airlines',
            'Zagros Airlines',
            'Mahan Air',
            'ATA Airlines',
            'Taban Air',
            'Caspian Airlines',
            'Karun Airlines',
            'Sepehran Airlines',
            'Varesh Air',
            'FlyPersia',
            'Pars Air'
        ]
city_name_dict = {
    'Tehran': 0.4,
    'Mashhad': 0.1,
    'Kish': 0.1,
    'Qeshm': 0.1,
    'Shiraz': 0.05,
    'Tabriz': 0.05,
    'Bandar Abbas': 0.05,
    'Yazd': 0.05,
    'Isfahan': 0.05,
    'Kermanshah': 0.05
}
male_firstname_list = [
    'Ahura', 'Ashkan', 'Armin', 'Afshin', 'Aria', 'Ario', 'Arman', 'Ahmed', 'Armin', 'Arash', 'Afraz', 'Ahoora',
    'Arvand', 'Afrasiab', 'Anoushirevan', 'Avesta', 'Abtin', 'Arshia', 'Arshiya', 'Ardeshir', 'Artin', 'Arvin',
    'Arya', 'Aryan', 'Ashem', 'Bahman', 'Bijan', 'Babak', 'Bahram', 'Bardia', 'Bashir', 'Behnam', 'Benyamin',
    'Dana', 'Dariush', 'Derafsh', 'Ervin', 'Ebrahim', 'Ehsan', 'Farhad', 'Farbod', 'Farrokh', 'Farshid', 'Farzad',
    'Feraydoon', 'FarshadFarhang', 'Garshasp', 'Ghazi', 'Gilgamesh', 'GivGoshtasb', 'Hashem', 'Homayun', 'Hormuzd',
    'Hooman', 'Houshang', 'Houtan', 'Ibrahim', 'Iman', 'Izad', 'Iraj', 'Jamshid', 'Jamshed', 'Javad', 'Jawed',
    'Kamran', 'Kamyar', 'Karvan', 'Kasra', 'Kaveh', 'Kazem', 'Keyvan', 'Khashayar', 'Khosrow', 'Kian', 'Kiarash',
    'Kourosh', 'Mahan', 'Mazdak', 'Mazdan', 'Maziar', 'Mehran', 'Mehruz', 'Mehyar', 'Manuchehr', 'Mehrdad', 'Marzban',
    'Mardan', 'Mehrzad', 'Mehdi', 'Meysam', 'Milad', 'MirMobeen', 'Ormazd', 'Parizad', 'Parsa', 'Parviz', 'Payam',
    'Pedram', 'Peyman', 'Pezhman', 'Piruz', 'Pouria', 'Pouya', 'Pouyan', 'Ramin', 'Ramshad', 'Saman', 'Sassan',
    'Sepehr', 'Sepanta', 'Shahin', 'Shapur', 'Shahryar', 'Shayan', 'Shervin', 'Soroush', 'Tirdad', 'Vahid'

]
female_firstname_list = [
    'Amaya', 'Anahita', 'Anousheh', 'Ashti', 'Arina', 'ArmitaArya', 'Ashraf', 'Astar', 'Atoosa', 'Azar', 'Azadi',
    'Banu', 'Baharak', 'Bita', 'Beeta', 'Donya', 'Farangis', 'Frida', 'Farideh', 'Farnaz', 'Farzaneh', 'Fereshteh',
    'Golnaz', 'HodaHoma', 'Jaleh', 'Kamand', 'Kiana', 'Kimia', 'Kejal', 'Khorshid', 'Laleh', 'Leila', 'Lanvin',
    'Mandana', 'Mahshid', 'Mahta', 'Mahtab', 'Maryam', 'Mehregan', 'Mina', 'Mozhgan', 'Manizheh', 'Nahid', 'Niousha',
    'Neda', 'Nishtiman', 'Niloufar', 'Nazanin', 'Nahal', 'Negin', 'Nooshin', 'Parastu', 'Parisa', 'Parmida', 'Parvin',
    'Parva', 'Payvand', 'Reyhan', 'Roksaneh', 'Roya', 'Roxana', 'Ronak', 'Safie', 'Sara', 'Sepideh', 'Setare', 'Shapol',
    'Shaghayegh', 'Shirin', 'Shireen', 'SiminSoraya', 'Tahmineh', 'Tannaz', 'Tara', 'Taraneh', 'Yasmin', 'Ziwar',
    'Zivar', 'Zhila', 'Zenwar', 'Zenwer', 'Zanwer'
]
lastname_list = [
    'Abdullahi', 'Abedini', 'Ahadi', 'Ahmadi', 'Akbari', 'Akbarian', 'Akbarpour', 'Alizadeh', 'Asadi', 'Azimi',
    'Baraghani', 'Barati', 'Ebrahimi', 'Esfahani', 'Esmaili', 'Fanaei', 'Farahani', 'Fikri', 'Fironzja', 'Firouzja',
    'Ghasemi','Hakimi', 'Hamadani', 'Hamidi', 'Hatami', 'Heydari', 'Hijazi', 'Hosseinzadeh', 'Husseini', 'Jahanbani',
    'Jalili', 'Jamshidi', 'Javadi' 'Karimi', 'Karimian', 'Kazmi', 'Khadem', 'Khalaji', 'Khomeini', 'Khorsandi',
    'Maghsoodloo', 'Mahdavi', 'Mahini', 'Mahmoudi', 'Mahmoudieh', 'Majidi', 'Mazanderani', 'Mirzaei', 'Mokri', 'Nabavi',
    'Naceri', 'Nafisi', 'Najafi', 'Namazi', 'Namdar', 'Nariman', 'Norouzi', 'Pahlavi', 'Pashaei', 'Qazwini', 'Rahimi',
    'Rajaei', 'Rashidi', 'Saberi',
    'Salehi', 'Salemi', 'Semnani', 'Shahbazi', 'Shahidi', 'Shirazi', 'Shojaee', 'Soltani', 'Soomekh', 'Tabatabaei',
    'Tajbakhsh', 'Talebi', 'Tousi' 'Yazdani', 'Yazdi', 'Zadeh', 'Zaland', 'Zomorodi'
]
tour_company_name_list =[
    'Madhu', 'Edyne', 'Mile', 'Gaspard', 'Thanuj', 'Snjy', 'Fayis', 'Tasmiya', 'Bhaskar', 'Sharon', 'Vinita', 'Haris',
    'Naushard', 'Zillur', 'Rani', 'Hobs', 'Rey', 'Dolly', 'Novy', 'Mojeeb', 'Yana', 'Biren', 'Anne'
]

plane_dict = {}
airline_dict = {}
flight_dict = {}


# This function populates different tables of database with fake records
def populate():
    def table_airplane():
        global plane_dict
        try:
            sqliteConnection = sqlite3.connect('Airport.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            # Iterate through airplane models/names
            for plane_model in plane_name_list:
                # For each airplane randomly choose a number of that, and register them one by one
                how_many = random.randint(1, 10)
                company, model_1 = plane_model.split()
                # Operate through different planes of the same model
                for plane in range(how_many):
                    model = "{}-{}".format(model_1, ''.join(random.choices(string.ascii_uppercase, k=2))+''.join(random.choices(string.digits, k=3)))
                    plane_id = ''.join(random.SystemRandom().choices(string.ascii_letters + string.digits, k=20))
                    in_use = '{}-{}-{}'.format(random.choice(range(2000, 2022)), random.choice(range(1, 13)),random.choice(range(1, 31)))
                    # Distinguish automatically generated records with real ones
                    # (preventing lose real data when purging db by checking this flag)
                    fake_record = 1
                    # Sql command to be executed
                    sql_query = """INSERT INTO Airplane VALUES('{}', '{}', '{}', '{}', '{}', {})""".format(plane_id, plane_model, model, company, in_use, fake_record)
                    # Execute query
                    cursor.execute(sql_query)
                    # Store locally
                    plane_dict[plane_id] = {'name': plane_model, 'model': model, 'company': company, 'in_use': in_use, 'fake_record': fake_record}
            sqliteConnection.commit()
                # Command to list table content in order by year
                # SELECT * FROM  Airplane ORDER BY been_in_use_from;
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
                sqliteConnection.close()
                print("sqlite connection is closed")

    def table_airline():
        global airline_dict
        try:
            sqliteConnection = sqlite3.connect('Airport.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            # Iterate through airlines
            for airline in airline_name_list:
                airline_id = ''.join(random.SystemRandom().choices(string.ascii_letters + string.digits, k=20))
                registered_date = '{}-{}-{}'.format(random.choice(range(2000, 2010)), random.choice(range(1, 13)), random.choice(range(1, 31)))
                # Distinguish automatically generated records.
                # (Prevents losing real data when purging db by checking this flag)
                fake_record = 1
                # SQL query
                sql_query = """INSERT INTO Airline VALUES('{}', '{}', '{}', {})""".format(airline_id, airline, registered_date, fake_record)
                # Execute query (store data on database/disk)
                cursor.execute(sql_query)
                # Store data locally
                airline_dict[airline_id] = {'name': airline, 'date': registered_date, 'fake_record': fake_record}
            sqliteConnection.commit()
            # Command to list table content order by date.
            # SELECT * FROM airline ORDER BY registered_date;
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
                sqliteConnection.close()
                print("sqlite connection is closed")

    def table_passenger():
        try:
            sqliteConnection = sqlite3.connect('Airport.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            for person in range(10000):
                gender = random.SystemRandom().choice(['male', 'female'])
                if gender == 'male':
                    firstname = random.SystemRandom().choice(male_firstname_list)
                else:
                    firstname = random.SystemRandom().choice(female_firstname_list)
                lastname = random.SystemRandom().choice(lastname_list)
                name = "{} {}".format(firstname, lastname)
                ssn = ''.join(random.SystemRandom().choices(string.digits, k=10))
                nationality = 'iran'
                flight_id = random.SystemRandom().choice(list(flight_dict.keys()))
                passenger_id = ''.join(random.SystemRandom().choices(string.ascii_letters + string.digits, k=20))
                age = random.SystemRandom().choice(range(20, 60))
                created_at = '{}-{}-{}'.format(random.choice(range(2000, 2010)), random.choice(range(1, 13)),
                                                    random.choice(range(1, 31)))
                fake_record = 1
                # SQL query
                sql_query = """INSERT INTO Passenger VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(passenger_id,
                                flight_id, ssn, nationality, fake_record, age, created_at, name)
                # Execute
                cursor.execute(sql_query)
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
                sqliteConnection.close()
                print("sqlite connection is closed")

    def table_flight():
        global flight_dict
        try:
            sqliteConnection = sqlite3.connect('Airport.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            # Iteration through years to register flights
            for year in (2021, 2022):
                # Iteration through month to register flights
                for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']:
                    # Iteration through days
                    for day in range(1, 31):
                        # Iteration through hours
                        for hour in range(12):
                            # We use '12' hour clock system
                            for half_day in ['am', 'pm']:
                                # Flights each half of an hour
                                for half_hour in ['30', '00']:
                                    flight_id = ''.join(random.SystemRandom().choices(string.ascii_letters + string.digits, k=20))
                                    # Make a copy of city list, to prevent tampering real data
                                    tmp_city_list = dict(city_name_dict)
                                    origin = random.SystemRandom().choices(list(city_name_dict.keys()), weights=list(city_name_dict.values()))[0]
                                    # Pop the origin to prevent it wouldn't be selected as dst as well.
                                    tmp_city_list.pop(origin)
                                    destination = random.SystemRandom().choices(list(city_name_dict.keys()), weights=list(city_name_dict.values()))[0]
                                    date = '{} {} {}  {}:{} {}'.format(year, month, day, hour, half_hour, half_day)
                                    delay = 0
                                    # A random airplane
                                    plane_id = random.SystemRandom().choice(list(plane_dict.keys()))
                                    # A random airline
                                    airline_id = random.SystemRandom().choice(list(airline_dict.keys()))
                                    # Distinguish automatically generated records.
                                    # (For preventing losing data when purging db by checking this flag.)
                                    fake_record = 1
                                    # SQL query
                                    sql_query = """INSERT INTO flight VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format\
                                        (flight_id, origin, destination, date, delay, plane_id, airline_id, fake_record)
                                    # Execute query (store data on disk/db)
                                    cursor.execute(sql_query)
                                    # Store data locally
                                    flight_dict[flight_id] = {'flight_id': flight_id, 'origin': origin,
                                        'destination': destination, 'date': date, 'delay': delay, 'plane_id': plane_id,
                                                              'airline_id': airline_id, 'fake_record': fake_record}
            # Commit and close db connection
            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
                sqliteConnection.close()
                print("sqlite connection is closed")

    def table_tour():
        try:
            sqliteConnection = sqlite3.connect('Airport.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            for tour in range(1000):
                tour_id = ''.join(random.SystemRandom().choices(string.ascii_letters + string.digits, k=20))
                gender = random.SystemRandom().choice(['male', 'female'])
                if gender == 'male':
                    firstname = random.SystemRandom().choice(male_firstname_list)
                else:
                    firstname = random.SystemRandom().choice(female_firstname_list)
                lastname = random.SystemRandom().choice(lastname_list)
                name = "{} {}".format(firstname, lastname)

                # Make a copy of flight dict, to prevent tampering real data
                tmp_flight_dict = dict(flight_dict)
                departure_flight_id = random.SystemRandom().choice(list(flight_dict.keys()))
                origin = flight_dict[departure_flight_id]['origin']
                destination = flight_dict[departure_flight_id]['destination']
                # Pop the arrival_flight_id to prevent it wouldn't be selected again.
                tmp_flight_dict.pop(departure_flight_id)
                arrival_flight_id = random.SystemRandom().choice(list(flight_dict.keys()))
                fake_record = 1
                booking = random.SystemRandom().choice(range(20, 40))
                company_name = random.SystemRandom().choice(tour_company_name_list)

                # SQL query
                sql_query = """INSERT INTO Tour VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(tour_id, name, company_name, origin, destination, booking, departure_flight_id, arrival_flight_id, fake_record)
                # Execute
                cursor.execute(sql_query)

            sqliteConnection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
                sqliteConnection.close()
                print("sqlite connection is closed")

    random.seed()
    table_airplane()
    table_airline()
    table_flight()
    table_passenger()
    table_tour()

# This function deletes purges database, and removes all automatically generated data
# (Distinguished by fake_record column)
def purge():
    try:
        sqliteConnection = sqlite3.connect('Airport.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        # SQL query
        sql_query = """SELECT name FROM sqlite_schema WHERE type=='table'"""
        # Execute
        cursor.execute(sql_query)
        for table in cursor.fetchall():
            sql_query = """DELETE FROM {} WHERE fake_record==1""".format(table[0])
            cursor.execute(sql_query)
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            print("Total Rows affected since the database connection was opened: ", sqliteConnection.total_changes)
            sqliteConnection.close()
            print("sqlite connection is closed")


def run():
    purge()
    populate()


if __name__ == "__main__":
    purge()
    populate()
