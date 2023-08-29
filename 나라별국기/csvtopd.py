from connectDB import cur, conn
import pandas as pd

url = "https://raw.githubusercontent.com/kig2929kig/db/main/%EA%B5%AD%EA%B0%80%EB%B3%84%EC%9D%B8%EA%B5%AC%EC%88%9C%EC%9C%84.csv"
df = pd.read_csv(url)

def creatTable() :
    sql = "create table worldPopulation ("
    column1 = "순번 int, 국가코드 char(2),"
    column2 = "국가 varchar(50), 수도 varchar(50),"
    column3 = "인구 float,"
    option = "primary key (국가코드))default charset=utf8"
    sql = sql + column1 + column2 + column3 + option
    cur.execute(sql)

def dropTable() :
    try :
        sql = "drop table worldPopulation"
        cur.execute(sql)
    except Exception as e :
        print(e)

def insertTable() :
    data = zip(df['순번'], df['국가코드'], df['국가'], df['수도'], df['인구'])
    for no, code, country, city, population in data :
        code = str(code); code = code[0:2]; code = code.upper()
        print(no, code, country, city, population)
        sql = f'insert into worldPopulation values({no}, "{code}", "{country}", "{city}", {population})'
        cur.execute(sql)
    conn.commit()

dropTable()
creatTable()
insertTable()
    


