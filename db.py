import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None

def create_task(conn, task):
    sql = ''' INSERT INTO tutorial_ticket(id,plugin_id,date,hostname,ip_address,plugin_name)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def main():
    database = "db.sqlite3"
    conn  = create_connection(database)
    with conn:
        task = ('6','97000','2019-01-07 13:02:15','sbibpl_gns.ad.trw.com','192.168.1.1','NFS Vulnerability')
        create_task(conn, task)

if __name__ == '__main__':
    main()