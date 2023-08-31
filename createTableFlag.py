from connectDB import cur, conn

def dropTblFlag() :
    sql = "drop table flag"
    cur.execute(sql)
    conn.commit()

def createTblFlag() :
    sql = "create table flag ("
    col1 = "순번 int, 국가코드 char(2),"
    col2 = "이미지 mediumblob,"
    col3 = "primary key(국가코드),"
    col4 = "foreign key(국가코드) references worldPopulation(국가코드))"
    op = "default charset=utf8"

    sql = sql + col1 + col2 + col3 + col4 + op

    cur.execute(sql)
    conn.commit()


try :
    dropTblFlag()
except Exception as e :
    print(e)
    
createTblFlag()
    
