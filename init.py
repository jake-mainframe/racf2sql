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
    init_usmfa(c)
    init_usmpol(c)
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
    init_uskerb(c)
    init_usproxy(c)
    init_useim(c)
    init_uscsd(c)
    init_usmfac(c)
    init_dsbd(c)
    init_dscat(c)
    init_dscacc(c)
    init_dsvol(c)
    init_dsacc(c)
    init_dsinstd(c)
    init_dsdfp(c)
    init_dstme(c)
    init_grbd(c)
    init_grtvol(c)
    init_grcat(c)
    init_grmem(c)
    init_grvol(c)
    init_gracc(c)
    init_grinstd(c)
    init_grcacc(c)
    init_grfltr(c)
    init_grdmap(c)
    init_grses(c)
    init_grsese(c)
    init_grdlf(c)
    init_grdlfj(c)
    init_grsign(c)
    init_grst(c)
    init_grsv(c)
    init_grcert(c)
    init_certr(c)
    init_keyr(c)
    init_grtme(c)
    init_grtmec(c)
    init_grtmer(c)
    init_grtmeg(c)
    init_grtmee(c)
    init_grkerb(c)
    init_grproxy(c)

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

def init_usmfa(c):
    c.execute('CREATE TABLE usmfa (name TEXT, factor_name TEXT, factor_active TEXT)')

def init_usmpol(c):
    c.execute('CREATE TABLE usmpol (name TEXT, policy_name TEXT)')

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

def init_uskerb(c):
    c.execute('CREATE TABLE uskerb (name TEXT, kerbname TEXT, max_life INTEGER, key_vers INTEGER, encrypt_des TEXT, encrypt_des3 TEXT, encrypt_desd TEXT, encrypt_a128 TEXT, encrypt_a256 TEXT, key_from TEXT)')

def init_usproxy(c):
    c.execute('CREATE TABLE usproxy (name TEXT, ldap_host TEXT, bind_dn TEXT)')

def init_useim(c):
    c.execute('CREATE TABLE useim (name TEXT, ldapprof TEXT)')

def init_uscsd(c):
    c.execute('CREATE TABLE uscsd (name TEXT, type TEXT, key TEXT, value TEXT)')

def init_usmfac(c):
    c.execute('CREATE TABLE usmfac (name TEXT, factor_name TEXT, tag_name TEXT, tag_value TEXT)')

def init_dsbd(c):
    c.execute('CREATE TABLE dsbd (name TEXT, vol TEXT, generic TEXT, create_date TEXT, owner_id TEXT, lastref_date TEXT, lastchg_date TEXT, alter_cnt INTEGER, control_cnt INTEGER, update_cnt INTEGER, read_cnt INTEGER, uacc TEXT, grpds TEXT, audit_level TEXT, grp_id TEXT, ds_type TEXT, level INTEGER, device_name TEXT, gaudit_level TEXT, install_data TEXT, audit_okqual TEXT, audit_faqual TEXT, gaudity_okqual TEXT, gaudit_faqual TEXT, warning TEXT, seclevel INTEGER, notify_id TEXT, retention INTEGER, erase TEXT, seclabel TEXT)')

def init_dscat(c):
    c.execute('CREATE TABLE dscat (name TEXT, vol TEXT, category INTEGER)')

def init_dscacc(c):
    c.execute('CREATE TABLE dscacc (name TEXT, vol TEXT, catype TEXT, caname TEXT, auth_id TEXT, access TEXT, access_cnt INTEGER, net_id TEXT, cacriteria TEXT)')

def init_dsvol(c):
    c.execute('CREATE TABLE dsvol (name TEXT, vol TEXT, vol_name TEXT)')

def init_dsacc(c):
    c.execute('CREATE TABLE dsacc (name TEXT, vol TEXT, auth_id TEXT, access TEXT, access_cnt INTEGER)')

def init_dsinstd(c):
    c.execute('CREATE TABLE dsinstd (name TEXT, vol TEXT, usr_name TEXT, usr_data TEXT, usr_flag TEXT)')

def init_dsdfp(c):
    c.execute('CREATE TABLE dsdfp (name TEXT, vol TEXT, resowner_id TEXT, datakey TEXT)')

def init_dstme(c):
    c.execute('CREATE TABLE dstme (name TEXT, vol TEXT, role_name TEXT, access_auth TEXT, cond_class TEXT, cond_prof TEXT)')

def init_grbd(c):
    c.execute('CREATE TABLE grbd (name TEXT, class_name TEXT, generic TEXT, class INTEGER, create_date TEXT, owner_id TEXT, lastref_date TEXT, lastchg_date TEXT, alter_cnt INTEGER, control_cnt INTEGER, update_cnt INTEGER, read_cnt INTEGER, uacc TEXT, audit_level TEXT, level INTEGER, gaudit_level TEXT, install_data TEXT, audit_okqual TEXT, audit_faqual TEXT, gaudit_okqual TEXT, gaudit_faqual TEXT, warning TEXT, singleds TEXT, auto TEXT, tvtoc TEXT, notify_id TEXT, access_sun TEXT, access_mon TEXT, access_tue TEXT, access_wed TEXT, access_thu TEXT, access_fri TEXT, access_sat TEXT, start_time TEXT, end_time TEXT, zone_offset TEXT, zone_direct TEXT, seclevel INTEGER, appl_data TEXT, seclabel TEXT)')

def init_grtvol(c):
    c.execute('CREATE TABLE grtvol (name TEXT, class_name TEXT, sequence INTEGER, create_date TEXT, discrete TEXT, intern_name TEXT, intern_vols TEXT, create_name TEXT)')

def init_grcat(c):
    c.execute('CREATE TABLE grcat (name TEXT, class_name TEXT, category INTEGER)')

def init_grmem(c):
    c.execute('CREATE TABLE grmem (name TEXT, class_name TEXT, member TEXT, global_acc TEXT, pads_data TEXT, vol_name TEXT, vmevent_data TEXT, seclevel INTEGER, category INTEGER)')

def init_grvol(c):
    c.execute('CREATE TABLE grvol (name TEXT, class_name TEXT, vol_name TEXT)')

def init_gracc(c):
    c.execute('CREATE TABLE gracc (name TEXT, class_name TEXT, auth_id TEXT, access TEXT, access_cnt INTEGER)')

def init_grinstd(c):
    c.execute('CREATE TABLE grinstd (name TEXT, class_name TEXT, usr_name TEXT, usr_data TEXT, usr_flag TEXT)')

def init_grcacc(c):
    c.execute('CREATE TABLE grcacc (name TEXT, class_name TEXT, catype TEXT, caname TEXT, auth_id TEXT, access TEXT, access_cnt INTEGER, net_id TEXT, cacriteria TEXT)')

def init_grfltr(c):
    c.execute('CREATE TABLE grfltr (name TEXT, class_name TEXT, label TEXT, status TEXT, user TEXT, create_name TEXT)')

def init_grdmap(c):
    c.execute('CREATE TABLE grdmap (name TEXT, class_name TEXT, label TEXT, user TEXT, didreg TEXT)')

def init_grses(c):
    c.execute('CREATE TABLE grses (name TEXT, class_name TEXT, session_key TEXT, locked TEXT, key_date TEXT, key_interval INTEGER, sls_fail INTEGER, max_fail INTEGER, convsec TEXT)')

def init_grsese(c):
    c.execute('CREATE TABLE grsese (name TEXT, class_name TEXT, entity_name TEXT, fail_cnt INTEGER)')

def init_grdlf(c):
    c.execute('CREATE TABLE grdlf (name TEXT, class_name TEXT, retain TEXT)')

def init_grdlfj(c):
    c.execute('CREATE TABLE grdlfj (name TEXT, class_name TEXT, job_name TEXT)')

def init_grsign(c):
    c.execute('CREATE TABLE grsign (name TEXT, class_name TEXT, protection TEXT)')

def init_grst(c):
    c.execute('CREATE TABLE grst (name TEXT, class_name TEXT, user_id TEXT, group_id TEXT, trusted TEXT, privileged TEXT, trace TEXT)')

def init_grsv(c):
    c.execute('CREATE TABLE grsv (name TEXT, class_name TEXT, script_name TEXT, parm_name TEXT)')

def init_grcert(c):
    c.execute('CREATE TABLE grcert (name TEXT, class_name TEXT, start_date TEXT, start_time TEXT, end_date TEXT, end_time TEXT, key_type TEXT, key_size INTEGER, last_serial TEXT, ring_seqn INTEGER, gen_req TEXT)')

def init_certr(c):
    c.execute('CREATE TABLE certr (name TEXT, class_name TEXT, ring_name TEXT)')

def init_keyr(c):
    c.execute('CREATE TABLE keyr (name TEXT, class_name TEXT, cert_name TEXT, cert_usage TEXT, cert_default TEXT, cert_label TEXT)')

def init_grtme(c):
    c.execute('CREATE TABLE grtme (name TEXT, class_name TEXT, parent TEXT)')

def init_grtmec(c):
    c.execute('CREATE TABLE grtmec (name TEXT, class_name TEXT, child TEXT)')

def init_grtmer(c):
    c.execute('CREATE TABLE grtmer (name TEXT, class_name TEXT, origin_role TEXT, prof_class TEXT, prof_name TEXT, access_auth TEXT, cond_class TEXT, cond_prof TEXT)')

def init_grtmeg(c):
    c.execute('CREATE TABLE grtmeg (name TEXT, class_name TEXT, _group TEXT)')

def init_grtmee(c):
    c.execute('CREATE TABLE grtmee (name TEXT, class_name TEXT, role_name TEXT, access_auth TEXT, cond_class TEXT, cond_prof TEXT)')

def init_grkerb(c):
    c.execute('CREATE TABLE grkerb (name TEXT, class_name TEXT, kerbname TEXT, min_life INTEGER, max_life INTEGER, def_life INTEGER, key_vers INTEGER, encrypt_des TEXT, encrypt_des3 TEXT, encrypt_desd TEXT, encrypt_a128 TEXT, encrypt_a256 TEXT, encrypt_a128sha2 TEXT, encrypt_a256sha2 TEXT, chkaddrs TEXT)')

def init_grproxy(c):
    c.execute('CREATE TABLE grproxy (name TEXT, class_name TEXT, ldap_host TEXT, bind_dn TEXT)')
