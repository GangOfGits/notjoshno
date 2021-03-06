from pyodbc import connect as py_connect
from yaml import load

with open("server.yaml", "r") as stream:
    credentials = load(stream)["credentials"]
    server = credentials["server"]
    database = credentials["database"]
    uid = credentials["uid"]
    password = credentials["password"]

def connect():
    return py_connect("Driver={ODBC Driver 13 for SQL Server}"
                      ";Server="+ server + ",1433"
                      ";Database=" + database +
                      ";Uid=" + uid + "@" + database +
                      ";Pwd=" + password +
                      ";Encrypt=yes"
                      ";TrustServerCertificate=no"
                      ";Connection Timeout=30"
                      ";")