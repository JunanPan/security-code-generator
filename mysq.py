import pymysql
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test1')
    return conn

def insert(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()
def query(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    if results:
        print('Already exists, cannot be inserted')
        print(type(results))  # 返回<class 'tuple'> tuple元组类型
        print(results)
    else:
        print('available')
    conn.commit()
    cur.close()
    conn.close()

sql = 'INSERT INTO fangweima VALUES(%s);'
new_code='223542'
insert(sql,new_code)
sql = 'SELECT * FROM fangweima WHERE code='+'\''+'43'+'\''
query(sql,None)