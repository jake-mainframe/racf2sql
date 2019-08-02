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
    init_ustso(c)
    init_uscics(c)
    init_uscopc(c)
    init_uscrsl(c)
    init_usctsl(c)
    init_uslan(c)
    init_usopr(c)
    init_usoprp(c)
    init_uswrk(c)
    init_usomvs(c)
    init_usnetv(c)
    init_usnopc(c)
    init_usndom(c)
    init_usdce(c)
    init_usovm(c)
    init_uslnot(c)
    init_usnds(c)

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

def init_ustso(c):
    c.execute('CREATE TABLE ustso (name TEXT, account TEXT, command TEXT, dest TEXT, hold_class TEXT, job_class TEXT, logon_proc TEXT, logon_size INTEGER, msg_class TEXT, logon_max INTEGER, perf_group INTEGER, sysout_class TEXT, user_data TEXT, unit_name TEXT, seclabel TEXT)')

def init_uscics(c):
    c.execute('CREATE TABLE uscics (name TEXT, opident TEXT, opprty INTEGER, noforce TEXT, timeout TEXT)')

def init_uscopc(c):
    c.execute('CREATE TABLE uscopc (name TEXT, opclass TEXT)')

def init_uscrsl(c):
    c.execute('CREATE TABLE uscrsl (name TEXT, key INTEGER)')

def init_usctsl(c):
    c.execute('CREATE TABLE usctsl (name TEXT, key INTEGER)')

def init_uslan(c):
    c.execute('CREATE TABLE uslan (name TEXT, _primary TEXT, _secondary TEXT)')

def init_usopr(c):
    c.execute('CREATE TABLE usoptr (name TEXT, storage INTEGER, masterauth TEXT, allauth TEXT, sysauth TEXT, ioauth TEXT, consauth TEXT, infoauth TEXT, timestamp TEXT, systemid TEXT, jobid TEXT, msgid TEXT, x TEXT, wtor TEXT, immediate TEXT, critical TEXT, eventual TEXT, info TEXT, nobrodcast TEXT, _all TEXT, jobnames TEXT, jobnamest TEXT, sess TEXT, sesst TEXT, status TEXT, routecode001 TEXT, routecode002 TEXT, routecode003 TEXT, routecode004 TEXT, routecode005 TEXT, routecode006 TEXT, routecode007 TEXT, routecode008 TEXT, routecode009 TEXT, routecode010 TEXT, routecode011 TEXT, routecode012 TEXT, routecode013 TEXT, routecode014 TEXT, routecode015 TEXT, routecode016 TEXT, routecode017 TEXT, routecode018 TEXT, routecode019 TEXT, routecode020 TEXT, routecode021 TEXT, routecode022 TEXT, routecode023 TEXT, routecode024 TEXT, routecode025 TEXT, routecode026 TEXT, routecode027 TEXT, routecode028 TEXT, routecode029 TEXT, routecode030 TEXT, routecode031 TEXT, routecode032 TEXT, routecode033 TEXT, routecode034 TEXT, routecode035 TEXT, routecode036 TEXT, routecode037 TEXT, routecode038 TEXT, routecode039 TEXT, routecode040 TEXT, routecode041 TEXT, routecode042 TEXT, routecode043 TEXT, routecode044 TEXT, routecode045 TEXT, routecode046 TEXT, routecode047 TEXT, routecode048 TEXT, routecode049 TEXT, routecode050 TEXT, routecode051 TEXT, routecode052 TEXT, routecode053 TEXT, routecode054 TEXT, routecode055 TEXT, routecode056 TEXT, routecode057 TEXT, routecode058 TEXT, routecode059 TEXT, routecode060 TEXT, routecode061 TEXT, routecode062 TEXT, routecode063 TEXT, routecode064 TEXT, routecode065 TEXT, routecode066 TEXT, routecode067 TEXT, routecode068 TEXT, routecode069 TEXT, routecode070 TEXT, routecode071 TEXT, routecode072 TEXT, routecode073 TEXT, routecode074 TEXT, routecode075 TEXT, routecode076 TEXT, routecode077 TEXT, routecode078 TEXT, routecode079 TEXT, routecode080 TEXT, routecode081 TEXT, routecode082 TEXT, routecode083 TEXT, routecode084 TEXT, routecode085 TEXT, routecode086 TEXT, routecode087 TEXT, routecode088 TEXT, routecode089 TEXT, routecode090 TEXT, routecode091 TEXT, routecode092 TEXT, routecode093 TEXT, routecode094 TEXT, routecode095 TEXT, routecode096 TEXT, routecode097 TEXT, routecode098 TEXT, routecode099 TEXT, routecode100 TEXT, routecode101 TEXT, routecode102 TEXT, routecode103 TEXT, routecode104 TEXT, routecode105 TEXT, routecode106 TEXT, routecode107 TEXT, routecode108 TEXT, routecode109 TEXT, routecode110 TEXT, routecode111 TEXT, routecode112 TEXT, routecode113 TEXT, routecode114 TEXT, routecode115 TEXT, routecode116 TEXT, routecode117 TEXT, routecode118 TEXT, routecode119 TEXT, routecode120 TEXT, routecode121 TEXT, routecode122 TEXT, routecode123 TEXT, routecode124 TEXT, routecode125 TEXT, routecode126 TEXT, routecode127 TEXT, routecode128 TEXT, logcmdresp TEXT, migrationid TEXT, delopermsg TEXT, retrieve_key TEXT, cmdsys TEXT, ud TEXT, altgrp_id TEXT, auto TEXT, hc TEXT, int TEXT, unkn TEXT)')

def init_usoprp(c):
    c.execute('CREATE TABLE usoprp (name TEXT, system TEXT)')

def init_uswrk(c):
    c.execute('CREATE TABLE uswrk (name TEXT, area_name TEXT, building TEXT, department TEXT, room TEXT, addr_line1 TEXT, addr_line2 TEXT, addr_line3 TEXT, addr_line4 TEXT, account TEXT)')

def init_usomvs(c):
    c.execute('CREATE TABLE usomvs (name TEXT, uid TEXT, home_path TEXT, program TEXT, cputimemax INTEGER, assizemax INTEGER, fileprocmax INTEGER, procusermax INTEGER, threadsmax INTEGER, mmapareamax INTEGER, memlimit TEXT, shmemax TEXT)')

def init_usnetv(c):
    c.execute('CREATE TABLE usnetv (name TEXT, ic TEXT, consname TEXT, ctl TEXT, msgrecvr TEXT, ngfadmn TEXT, ngmfvspn TEXT)')

def init_usnopc(c):
    c.execute('CREATE TABLE usnopc (name TEXT, opclass INTEGER)')

def init_usndom(c):
    c.execute('CREATE TABLE usndom (name TEXT, domains TEXT)')

def init_usdce(c):
    c.execute('CREATE TABLE usdce (name TEXT, uuid TEXT, dce_name TEXT, homecell TEXT, homeuuid TEXT, autologin TEXT)')

def init_usovm(c):
    c.execute('CREATE TABLE usovm (name TEXT, uid TEXT, home_path TEXT, program TEXT, fsroot TEXT)')

def init_uslnot(c):
    c.execute('CREATE TABLE uslnot (name TEXT, sname TEXT)')

def init_usnds(c):
    c.execute('CREATE TABLE usnds (name TEXT, uname TEXT)')
