import sqlite3

def init_db(filename):
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    init_gpbd(c)
    init_gpsgrp(c)
    init_gpmem(c)
    init_gpinstd(c)
    init_gpdfp(c)
    init_gpomvs(c)

    conn.commit()
    conn.close()

def init_gpbd(c):
    c.execute('CREATE TABLE gpbd (name TEXT, supgrp_id TEXT, create_date TEXT, owner_id TEXT, uacc TEXT, notermuacc INTEGER, install_data TEXT, model CHAR, universal INTEGER)')

def init_gpsgrp(c):
    c.execute('CREATE TABLE gpsgrp (name TEXT, subgrp_id TEXT)')

def init_gpmem(c):
    c.execute('CREATE TABLE gpmem (name TEXT, member_id TEXT, auth TEXT)')

def init_gpinstd(c):
    c.execute('CREATE TABLE gpinstd (name TEXT, usr_name TEXT, usr_data TEXT, usr_flag TEXT)')

def init_gpdfp(c):
    c.execute('CREATE TABLE gpdfp (name TEXT, dataappl TEXT, dataclas TEXT, mgmtclas TEXT, storclas TEXT)')

def init_gpomvs(c):
    c.execute('CREATE TABLE gpomvs (name TEXT, gid TEXT)')
