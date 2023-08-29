import os

try :
    import pymysql
except ImportError :
    os.system('pip install pymysql')

try :
    conn = pymysql.connect(host='13.124.160.231',
                     port= 52583,
                     user='kig2929kig',
                     password='ansan',
                     db='com3100',
                     charset='utf8')
    db_info = conn.get_server_info()
    print('mysql version : ', db_info)
    cur = conn.cursor()
except Exception as e :
    print('mysql error : ', e)

