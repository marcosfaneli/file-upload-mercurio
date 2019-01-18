import psycopg2
from common.config import USERNAME, HOST, DBNAME, PASSWORD


def get_conexao():
    path = "host='{}' dbname='{}' user='{}' password='{}'".format(HOST, DBNAME, USERNAME, PASSWORD)
    conn = psycopg2.connect(path)

    return conn
