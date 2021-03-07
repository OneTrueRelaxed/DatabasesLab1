import csv
import time
import logging
import os, psycopg2, csv

from psycopg2 import sql
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

conn = None
cursor = None

zno_files_inserted = {2019: False, 2020: False}

logging.basicConfig(
    filename="logs.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

def get_env_var(name):
    return os.environ.get(name)

def handle_operational(func):
    def wrapper(times=0):
        if times < 60:
            try:
                func()
            except psycopg2.OperationalError:
                times += 1
                logging.info(f"Trying to reconnect to database. Try: {times}")
                time.sleep(0.5)
                wrapper(times)

    return wrapper

def reconnect_after_connection_loss(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except psycopg2.errors.AdminShutdown:
            global conn, cursor

            cursor.close()
            cursor = None

            conn.close()
            conn = None

            do_the_lab()

    return wrapper

def do_the_lab():
    establish_connection()
    create_cursor()

    start = datetime.now()

    create_table()
    logging.info("Start populating the database")


    if zno_files_inserted[2019] == False:
        zno2019 = get_env_var("zno2019")
        populate_table(zno2019, 2019)
        
    if zno_files_inserted[2020] == False:
        zno2020 = get_env_var("zno2020")
        populate_table(zno2020, 2020)

    logging.info("End of populating the database")
    end = datetime.now()
    logging.info(f"Time for executing is : {end - start}\n")

    make_query()

    cursor.close()
    conn.close()

@handle_operational
def establish_connection():
    global conn
    conn = psycopg2.connect(
        dbname=get_env_var("db"),
        user=get_env_var("user"),
        password=get_env_var("password"),
        host=get_env_var("url"),
    )

def create_cursor():
    global conn, cursor
    if conn != None:
        cursor = conn.cursor()
    else:
        establish_connection()

def test_connection():
    global conn, cursor
    establish_connection()
    create_cursor()

    cursor.execute("insert into test values (%(test)s)", {"test": "test"}) 
    conn.commit()
    query = "SELECT * FROM test;"
    cursor.execute(query, ('test'))
    print(cursor.fetchall())

def create_table():
    table_name = get_env_var("table")

    global conn, cursor

    query=f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            OUTID VARCHAR, 
            Birth VARCHAR, 
            SEXTYPENAME VARCHAR, 
            REGNAME VARCHAR, 
            AREANAME VARCHAR, 
            TERNAME VARCHAR, 
            REGTYPENAME VARCHAR, 
            TerTypeName VARCHAR, 
            ClassProfileNAME VARCHAR, 
            ClassLangName VARCHAR, 
            EONAME VARCHAR, 
            EOTYPENAME VARCHAR, 
            EORegName VARCHAR, 
            EOAreaName VARCHAR, 
            EOTerName VARCHAR, 
            EOParent VARCHAR, 
            UkrTest VARCHAR, 
            UkrTestStatus VARCHAR, 
            UkrBall100 VARCHAR, 
            UkrBall12 VARCHAR, 
            UkrBall VARCHAR, 
            UkrAdaptScale VARCHAR, 
            UkrPTName VARCHAR, 
            UkrPTRegName VARCHAR, 
            UkrPTAreaName VARCHAR, 
            UkrPTTerName VARCHAR, 
            histTest VARCHAR, 
            HistLang VARCHAR, 
            histTestStatus VARCHAR, 
            histBall100 VARCHAR, 
            histBall12 VARCHAR, 
            histBall VARCHAR, 
            histPTName VARCHAR, 
            histPTRegName VARCHAR, 
            histPTAreaName VARCHAR, 
            histPTTerName VARCHAR, 
            mathTest VARCHAR, 
            mathLang VARCHAR, 
            mathTestStatus VARCHAR, 
            mathBall100 REAL, 
            mathBall12 VARCHAR, 
            mathBall VARCHAR, 
            mathPTName VARCHAR, 
            mathPTRegName VARCHAR, 
            mathPTAreaName VARCHAR, 
            mathPTTerName VARCHAR, 
            physTest VARCHAR, 
            physLang VARCHAR, 
            physTestStatus VARCHAR, 
            physBall100 VARCHAR, 
            physBall12 VARCHAR, 
            physBall VARCHAR, 
            physPTName VARCHAR, 
            physPTRegName VARCHAR, 
            physPTAreaName VARCHAR, 
            physPTTerName VARCHAR, 
            chemTest VARCHAR, 
            chemLang VARCHAR, 
            chemTestStatus VARCHAR, 
            chemBall100 VARCHAR, 
            chemBall12 VARCHAR, 
            chemBall VARCHAR, 
            chemPTName VARCHAR, 
            chemPTRegName VARCHAR, 
            chemPTAreaName VARCHAR, 
            chemPTTerName VARCHAR, 
            bioTest VARCHAR, 
            bioLang VARCHAR, 
            bioTestStatus VARCHAR, 
            bioBall100 VARCHAR, 
            bioBall12 VARCHAR, 
            bioBall VARCHAR, 
            bioPTName VARCHAR, 
            bioPTRegName VARCHAR, 
            bioPTAreaName VARCHAR, 
            bioPTTerName VARCHAR, 
            geoTest VARCHAR, 
            geoLang VARCHAR, 
            geoTestStatus VARCHAR, 
            geoBall100 VARCHAR, 
            geoBall12 VARCHAR, 
            geoBall VARCHAR, 
            geoPTName VARCHAR, 
            geoPTRegName VARCHAR, 
            geoPTAreaName VARCHAR, 
            geoPTTerName VARCHAR, 
            engTest VARCHAR, 
            engTestStatus VARCHAR, 
            engBall100 VARCHAR, 
            engBall12 VARCHAR, 
            engDPALevel VARCHAR, 
            engBall VARCHAR, 
            engPTName VARCHAR, 
            engPTRegName VARCHAR, 
            engPTAreaName VARCHAR, 
            engPTTerName VARCHAR, 
            fraTest VARCHAR, 
            fraTestStatus VARCHAR, 
            fraBall100 VARCHAR, 
            fraBall12 VARCHAR, 
            fraDPALevel VARCHAR, 
            fraBall VARCHAR, 
            fraPTName VARCHAR, 
            fraPTRegName VARCHAR, 
            fraPTAreaName VARCHAR, 
            fraPTTerName VARCHAR, 
            deuTest VARCHAR, 
            deuTestStatus VARCHAR, 
            deuBall100 VARCHAR, 
            deuBall12 VARCHAR, 
            deuDPALevel VARCHAR, 
            deuBall VARCHAR, 
            deuPTName VARCHAR, 
            deuPTRegName VARCHAR, 
            deuPTAreaName VARCHAR, 
            deuPTTerName VARCHAR, 
            spaTest VARCHAR, 
            spaTestStatus VARCHAR, 
            spaBall100 VARCHAR, 
            spaBall12 VARCHAR, 
            spaDPALevel VARCHAR, 
            spaBall VARCHAR, 
            spaPTName VARCHAR, 
            spaPTRegName VARCHAR, 
            spaPTAreaName VARCHAR, 
            spaPTTerName VARCHAR,
            year INT,
            PRIMARY KEY (OUTID, year)
        );
    """

    cursor.execute(query)
    conn.commit()

@reconnect_after_connection_loss
def populate_table(zno_file, year):
    global conn, cursor

    with open(zno_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        for row in csv_reader:
            query = create_insert_query(row)

            if row["mathBall100"] == 'null':
                row["mathBall100"] = -1.0
            else:
                row["mathBall100"] = float(row["mathBall100"].replace(",", "."))

            values = row
            values["year"] = year

            cursor.execute(query, values)

        conn.commit()
        zno_files_inserted[year] = True

def create_insert_query(row):
    table_name = get_env_var("table")

    columns = ""
    placeholders = ""
    values = []

    for column in row:
        columns += column + ","
        values.append(row[column])
        placeholders += f"%({column})s,"

    columns += "year"
    placeholders += "%(year)s"

    query = f"INSERT INTO {table_name}({columns}) VALUES({placeholders})"

    return query

def make_query():
    conn = psycopg2.connect(
        dbname=get_env_var("db"),
        user=get_env_var("user"),
        password=get_env_var("password"),
        host=get_env_var("url"),
    )

    cur = conn.cursor()

    query = """
select REGNAME, min(mathBall100), year from zno
where mathTestStatus='Зараховано'
group by REGNAME, year
order by year; 
     """

    cur.execute(query)
    res = cur.fetchall()

    res = csv_sort(res)

    with open("query_result.csv", "w") as result_csv:
        query_result = csv.writer(result_csv, delimiter=",")

        query_result.writerow(["Region", "2019", "2020"])

        for row in res:
            query_result.writerow(row)

    cur.close()
    conn.close()

def csv_sort(ls):
    regions = []

    for row in ls:
        regions.append(row[0])

    regions = set(regions)

    res = []

    for reg in regions:
        reg1, reg2 = find_region(ls, reg)

        print(reg1, reg2)

        triple = [reg, None, None]

        if reg1[2] == 2019:
            triple[1] = float(reg1[1])
            triple[2] = float(reg2[1])
        else:
            triple[2] = float(reg1[1])
            triple[1] = float(reg2[1])

        res.append(tuple(triple))

    return res

def find_region(ls, reg):
    res = []

    for row in ls:
        if row[0] == reg:
            res.append(row)

    return tuple(res)

if __name__ == "__main__":
    do_the_lab()
    #test_connection()
    #rows 733112