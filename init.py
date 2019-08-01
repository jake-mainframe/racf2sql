import sqlite3

def init_db(filename):
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    init_gpbd(c)

    conn.commit()
    conn.close()

def init_gpbd(c):
    c.execute('CREATE TABLE gpbd (name TEXT, supgrp_id TEXT, create_date TEXT, owner_id TEXT, uacc TEXT, notermuacc INTEGER, install_data TEXT, model CHAR, universal INTEGER)')
