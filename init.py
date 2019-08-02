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
    init_gpovm(c)
    init_gptme(c)
    init_gpcsd(c)
    init_usbd(c)
    init_uscat(c)
    init_uscla(c)
    init_usgcon(c)
    init_usinstd(c)
    init_uscon(c)
    init_usrsf(c)
    init_uscert(c)
    init_usnmap(c)
    init_usdmap(c)
    init_usdfp(c)

    conn.commit()
    conn.close()

def init_gpbd(c):
    c.execute('CREATE TABLE gpbd (name TEXT, supgrp_id TEXT, create_date TEXT, owner_id TEXT, uacc TEXT, notermuacc TEXT, install_data TEXT, model TEXT, universal TEXT)')

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

def init_gpovm(c):
    c.execute('CREATE TABLE gpovm (name TEXT, gid TEXT)')

def init_gptme(c):
    c.execute('CREATE TABLE gptme (name TEXT, role TEXT)')

def init_gpcsd(c):
    c.execute('CREATE TABLE gpcsd (name TEXT, type TEXT, key TEXT, value TEXT)')

def init_usbd(c):
    c.execute('CREATE TABLE usbd (name TEXT, create_date TEXT, owner_id TEXT, adsp TEXT, special TEXT, oper TEXT, revoke TEXT, grpacc TEXT, pwd_interval INTEGER, pwd_date TEXT, programmer TEXT, defgrp_id TEXT, lastjob_time TEXT, lastjob_date TEXT, install_data TEXT, uaudit TEXT, auditor TEXT, nopwd TEXT, oidcard TEXT, pwd_gen INTEGER, revoke_cnt INTEGER, model TEXT, seclevel INTEGER, revoke_date TEXT, resume_date DATE, access_sun TEXT, access_mon TEXT, access_tue TEXT, access_wed TEXT, access_thu TEXT, access_fri TEXT, access_sat TEXT, start_time TEXT, end_time TEXT, seclabel TEXT, attribs TEXT, pwdenv_exists TEXT, pwd_asis TEXT, phr_date TEXT, phr_gen INTEGER, cert_seqn INTEGER, pphenv_exists TEXT)')

def init_uscat(c):
    c.execute('CREATE TABLE uscat (name TEXT, category INTEGER)')

def init_uscla(c):
    c.execute('CREATE TABLE uscla (name TEXT, class TEXT)')

def init_usgcon(c):
    c.execute('CREATE TABLE usgcon (name TEXT, grp_id TEXT)')

def init_usinstd(c):
    c.execute('CREATE TABLE usinstd (name TEXT, usr_name TEXT, usr_data TEXT, usr_flag TEXT)')

def init_uscon(c):
    c.execute('CREATE TABLE uscon (name TEXT, grp_id TEXT, connect_date TEXT, owner_id TEXT, lastcon_time TEXT, lastcon_date TEXT, uacc TEXT, init_cnt INTEGER, grp_adsp TEXT, grp_special TEXT, grp_oper TEXT, revoke TEXT, grp_acc TEXT, notermuacc TEXT, grp_audit TEXT, revoke_date TEXT, resume_date TEXT)')

def init_usrsf(c):
    c.execute('CREATE TABLE usrsf (name TEXT, targ_node TEXT, targ_user_id TEXT, version INTEGER, peer TEXT, managing TEXT, managed TEXT, remote_pend TEXT, local_pend TEXT, pwd_sync TEXT, rem_refusal TEXT,  define_date TEXT, define_time TEXT, accept_date TEXT, accept_time TEXT, creator_id TEXT)')

def init_uscert(c):
    c.execute('CREATE TABLE uscert (name TEXT, cert_name TEXT, certlabl TEXT)')

def init_usnmap(c):
    c.execute('CREATE TABLE usnmap (name TEXT, label TEXT, map_name TEXT)')

def init_usdmap(c):
    c.execute('CREATE TABLE usdmap (name TEXT, label TEXT, map_name TEXT)')

def init_usdfp(c):
    c.execute('CREATE TABLE usdfp (name TEXT, dataappl TEXT, dataclas TEXT, mgmtclas TEXT, storclas TEXT)')
