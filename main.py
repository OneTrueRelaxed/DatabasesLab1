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

logging.basicConfig(
    filename="logs.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

def get_env_var(name):
    return os.environ.get(name)

def do_the_lab():
    establish_connection()
    create_cursor()

    start = datetime.now()

    create_tables()

    insert_breakpoint()

    create_inserted()

    cursor.execute("SELECT inserted FROM inserted WHERE year=2019;")
    inserted2019 = cursor.fetchone()[0]

    cursor.execute("SELECT inserted FROM inserted WHERE year=2020;")
    inserted2020 = cursor.fetchone()[0]

    logging.info("Start populating the database")

    if inserted2019 != True:
        zno2019 = get_env_var("zno2019")
        populate_table(zno2019, 2019)

    if inserted2020 != True:     
        zno2020 = get_env_var("zno2020")
        populate_table(zno2020, 2020)

    logging.info("End of populating the database")
    end = datetime.now()
    logging.info(f"Time for executing is : {end - start}\n")

    #make_query()

    cursor.close()
    conn.close()

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

def create_tables():
    table_name = get_env_var("table")

    global conn, cursor

    query=f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            OUTID VARCHAR, 
            Birth INT, 
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
            UkrBall100 FLOAT, 
            UkrBall12 INT, 
            UkrBall INT, 
            UkrAdaptScale VARCHAR, 
            UkrPTName VARCHAR, 
            UkrPTRegName VARCHAR, 
            UkrPTAreaName VARCHAR, 
            UkrPTTerName VARCHAR, 
            histTest VARCHAR, 
            HistLang VARCHAR, 
            histTestStatus VARCHAR, 
            histBall100 FLOAT, 
            histBall12 INT, 
            histBall INT, 
            histPTName VARCHAR, 
            histPTRegName VARCHAR, 
            histPTAreaName VARCHAR, 
            histPTTerName VARCHAR, 
            mathTest VARCHAR, 
            mathLang VARCHAR, 
            mathTestStatus VARCHAR, 
            mathBall100 FLOAT, 
            mathBall12 INT, 
            mathBall INT, 
            mathPTName VARCHAR, 
            mathPTRegName VARCHAR, 
            mathPTAreaName VARCHAR, 
            mathPTTerName VARCHAR, 
            physTest VARCHAR, 
            physLang VARCHAR, 
            physTestStatus VARCHAR, 
            physBall100 FLOAT, 
            physBall12 INT, 
            physBall INT, 
            physPTName VARCHAR, 
            physPTRegName VARCHAR, 
            physPTAreaName VARCHAR, 
            physPTTerName VARCHAR, 
            chemTest VARCHAR, 
            chemLang VARCHAR, 
            chemTestStatus VARCHAR, 
            chemBall100 FLOAT, 
            chemBall12 INT, 
            chemBall INT, 
            chemPTName VARCHAR, 
            chemPTRegName VARCHAR, 
            chemPTAreaName VARCHAR, 
            chemPTTerName VARCHAR, 
            bioTest VARCHAR, 
            bioLang VARCHAR, 
            bioTestStatus VARCHAR, 
            bioBall100 FLOAT, 
            bioBall12 INT, 
            bioBall INT, 
            bioPTName VARCHAR, 
            bioPTRegName VARCHAR, 
            bioPTAreaName VARCHAR, 
            bioPTTerName VARCHAR, 
            geoTest VARCHAR, 
            geoLang VARCHAR, 
            geoTestStatus VARCHAR, 
            geoBall100 FLOAT, 
            geoBall12 INT, 
            geoBall INT, 
            geoPTName VARCHAR, 
            geoPTRegName VARCHAR, 
            geoPTAreaName VARCHAR, 
            geoPTTerName VARCHAR, 
            engTest VARCHAR, 
            engTestStatus VARCHAR, 
            engBall100 FLOAT, 
            engBall12 INT, 
            engDPALevel VARCHAR, 
            engBall VARCHAR, 
            engPTName VARCHAR, 
            engPTRegName VARCHAR, 
            engPTAreaName VARCHAR, 
            engPTTerName VARCHAR, 
            fraTest VARCHAR, 
            fraTestStatus VARCHAR, 
            fraBall100 FLOAT, 
            fraBall12 INT, 
            fraDPALevel VARCHAR, 
            fraBall VARCHAR, 
            fraPTName VARCHAR, 
            fraPTRegName VARCHAR, 
            fraPTAreaName VARCHAR, 
            fraPTTerName VARCHAR, 
            deuTest VARCHAR, 
            deuTestStatus VARCHAR, 
            deuBall100 FLOAT, 
            deuBall12 INT, 
            deuDPALevel VARCHAR, 
            deuBall VARCHAR, 
            deuPTName VARCHAR, 
            deuPTRegName VARCHAR, 
            deuPTAreaName VARCHAR, 
            deuPTTerName VARCHAR, 
            spaTest VARCHAR, 
            spaTestStatus VARCHAR, 
            spaBall100 FLOAT, 
            spaBall12 INT, 
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

    query = """
        CREATE TABLE IF NOT EXISTS breakpoint(
            breakpoint INT,
            year INT
        );
    """

    cursor.execute(query)
    conn.commit()

    query = """
        CREATE TABLE IF NOT EXISTS inserted (
            inserted BOOL,
            year INT
        );
    """

    cursor.execute(query)
    conn.commit()

def insert_breakpoint():
    global cursor, conn

    cursor.execute("SELECT year FROM breakpoint WHERE year=2019;")
    res = cursor.fetchone()

    if res == None:
        cursor.execute("INSERT INTO breakpoint(breakpoint, year) VALUES(0, 2019);")
        conn.commit()

    cursor.execute("SELECT year FROM breakpoint WHERE year=2020;")
    res = cursor.fetchone()

    if res == None:
        cursor.execute("INSERT INTO breakpoint(breakpoint, year) VALUES(0, 2020);")
        conn.commit()

def create_inserted():
    global cursor, conn

    cursor.execute("SELECT year FROM inserted WHERE year=2019;")
    res = cursor.fetchone()

    if res == None:
        cursor.execute("INSERT INTO inserted(inserted, year) VALUES(false, 2019);")
        conn.commit()

    cursor.execute("SELECT year FROM inserted WHERE year=2020;")
    res = cursor.fetchone()

    if res == None:
        cursor.execute("INSERT INTO inserted(inserted, year) VALUES(false, 2020);")
        conn.commit()  

def populate_table(zno_file, year):
    global conn, cursor

    with open(zno_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")

        brkpoint = get_breakpoint(year)

        i = 0

        for row in csv_reader:
            if i <= brkpoint:
                i += 1
                continue

            query = create_insert_query(row)

            replace_commas(row)
            replace_nulls(row)

            values = row
            values["year"] = year

            cursor.execute(query, values)

            if i % 1000 == 0:
                set_breakpoint(i, year)
                conn.commit() 

            i += 1

        cursor.execute("UPDATE inserted SET inserted=true WHERE year=%(year)s;", {"year": year}) 
        conn.commit()

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

def replace_commas(row):
    subjects = [
        "UkrBall100",
        "histBall100",
        "mathBall100",
        "physBall100",
        "chemBall100",
        "bioBall100",
        "geoBall100",
        "engBall100",
        "fraBall100",
        "deuBall100",
        "spaBall100",
    ]

    for subject in subjects:
        if row[subject] != "null":
            row[subject] = float(row[subject].replace(",", "."))
        else:
            row[subject] = None

def replace_nulls(row):
    subjects = [
        "UkrBall12",
        "UkrBall",
        "histBall12",
        "histBall",
        "mathBall12",
        "mathBall",
        "physBall12",
        "physBall",
        "chemBall12",
        "chemBall",
        "bioBall12",
        "bioBall",
        "geoBall12",
        "geoBall",
        "engBall12",
        "fraBall12",
        "deuBall12",
        "spaBall12"
    ]

    for subject in subjects:
        if row[subject] == "null":
            row[subject] = None

def get_breakpoint(year):
    global cursor

    cursor.execute(f"SELECT breakpoint FROM breakpoint WHERE year={year};")
    brkpoint = cursor.fetchone()

    brkpoint = brkpoint[0]

    res = brkpoint - brkpoint % 1000 

    return res

def set_breakpoint(line, year):
    global conn, cursor

    cursor.execute("UPDATE breakpoint SET breakpoint=%(line)s WHERE year=%(year)s;", {"line": line, "year": year})

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