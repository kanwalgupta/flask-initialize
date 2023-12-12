import psycopg2

def build_connection(database, user, password):
    return psycopg2.connect(database= database, user=user, password = password)

def get_cursor(conn):
    return conn.cursor()

def add_records(cursor, table, columns, values):
    cursor.execute(f'INSERT INTO {table} ({",".join(columns)}) VALUES {tuple(values)}')

def drop_records(cursor, table):
   try:
    cursor.execute(f'TRUNCATE {table} RESTART IDENTITY')
   except Exception as e:
    breakpoint()
    ex =e

def close_conn(conn):
    conn.close()