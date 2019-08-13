import sqlite3

def load_racf(unload, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    with open(unload) as fp:
        for line in fp:
            process(line, c)
    conn.commit()
    conn.close()

def process(l, c):
    if len(l) < 4:
        print(f"WARN: Unexpected short line:\n\t{l}")
        return

    record_type = l[0:4]

    if record_type ==   "0100":
        process_gpbd(l, c)
    elif record_type == "0101":
        process_gpsgrp(l, c)
    elif record_type == "0102":
        process_gpmem(l, c)
    elif record_type == "0103":
        process_gpinstd(l, c)
    elif record_type == "0110":
        process_gpdfp(l, c)
    elif record_type == "0120":
        process_gpomvs(l, c)
    elif record_type == "0130":
        process_gpovm(l, c)
    elif record_type == "0141":
        process_gptme(l, c)
    elif record_type == "0151":
        process_gpcsd(l, c)
    elif record_type == "0200":
        process_usbd(l, c)
    elif record_type == "0201":
        process_uscat(l, c)
    elif record_type == "0202":
        process_uscla(l, c)
    elif record_type == "0203":
        process_usgcon(l, c)
    elif record_type == "0204":
        process_usinstd(l, c)
    elif record_type == "0205":
        process_uscon(l, c)
    elif record_type == "0206":
        process_usrsf(l, c)
    elif record_type == "0207":
        process_uscert(l, c)
    elif record_type == "0208":
        process_usnmap(l, c)
    elif record_type == "0209":
        process_usdmap(l, c)
    elif record_type == "020A":
        process_usmfa(l, c)
    elif record_type == "020B":
        process_usmpol(l, c)
    elif record_type == "0210":
        process_usdfp(l, c)
    elif record_type == "0220":
        process_ustso(l, c)
    elif record_type == "0230":
        process_uscics(l, c)
    elif record_type == "0231":
        process_uscopc(l, c)
    elif record_type == "0232":
        process_uscrsl(l, c)
    elif record_type == "0233":
        process_usctsl(l, c)
    elif record_type == "0240":
        process_uslan(l, c)
    elif record_type == "0250":
        process_usopr(l, c)
    elif record_type == "0251":
        process_usoprp(l, c)
    elif record_type == "0260":
        process_uswrk(l, c)
    elif record_type == "0270":
        process_usomvs(l, c)
    elif record_type == "0280":
        process_usnetv(l, c)
    elif record_type == "0281":
        process_usnopc(l, c)
    elif record_type == "0282":
        process_usndom(l, c)
    elif record_type == "0290":
        process_usdce(l, c)
    elif record_type == "02A0":
        process_usovm(l, c)
    elif record_type == "02B0":
        process_uslnot(l, c)
    elif record_type == "02C0":
        process_usnds(l, c)
    elif record_type == "02D0":
        process_uskerb(l, c)
    elif record_type == "02E0":
        process_usproxy(l, c)
    elif record_type == "02F0":
        process_useim(l, c)
    elif record_type == "02G1":
        process_uscsd(l, c)
    elif record_type == "1210":
        process_usmfac(l, c)
    elif record_type == "0400":
        process_dsbd(l, c)
    elif record_type == "0401":
        process_dscat(l, c)
    elif record_type == "0402":
        process_dscacc(l, c)
    elif record_type == "0403":
        process_dsvol(l, c)
    elif record_type == "0404":
        process_dsacc(l, c)
    elif record_type == "0405":
        process_dsinstd(l, c)
    elif record_type == "0410":
        process_dsdfp(l, c)
    elif record_type == "0421":
        process_dstme(l, c)
    else:
        print(f"WARN: Uncategorised/unknown line:\n\t{l}")

def process_gpbd(l, c):
    v = (
        l[5:13],      #GPBD_NAME:         Group name as taken from the profile name.
        l[14:22],     #GPBD_SUPGRP_ID:    Name of the superior group to this group.
        l[23:33],     #GPBD_CREATE_DATE:  Date that the group was defined.
        l[34:42],     #GPBD_OWNER_ID:     The user ID or group name which owns the profile.
        l[43:51],     #GPBD_UACC:         The default universal access. Valid values are NONE for all groups other than the IBM®-defined VSAMDSET group which has CREATE.
        l[52:56],     #GPBD_NOTERMUACC:   Indicates if the group must be specifically authorized to use a particular terminal through the use of the PERMIT command.
        l[57:312],    #GPBD_INSTALL_DATA: Installation-defined data.
        l[313:357],   #GPBD_MODEL:        Data set profile that is used as a model for this group.
        l[358:362],   #GPBD_UNIVERSAL:    Indicates if the group has the UNIVERSAL attribute.
    )
    c.execute("INSERT INTO gpbd VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0100) Group Basic Data Record processed.")

def process_gpsgrp(l, c):
    v = (
        l[5:13],      #GPSGRP_NAME:       Group name as taken from the profile name.
        l[14:22],     #GPSGRP_SUBGRP_ID:  The name of a subgroup within the group.
    )
    c.execute("INSERT INTO gpsgrp VALUES (?, ?)", v)
    print("INFO: (0101) Group Subgroups Record processed.")

def process_gpmem(l, c):
    v = (
        l[5:13],      #GPMEM_NAME:        Group name as taken from the profile name.
        l[14:22],     #GPMEM_MEMBER_ID:   A user ID within the group.
        l[23:31],     #GPMEM_AUTH:        Indicates the authority that the user ID has within the group. Valid values are USE, CONNECT, JOIN, and CREATE.
    )
    c.execute("INSERT INTO gpmem VALUES (?, ?, ?)", v)
    print("INFO: (0102) Group Members Record processed.")

def process_gpinstd(l, c):
    v = (
        l[5:13],      #GPINSTD_NAME:      Group name as taken from the profile name.
        l[14:22],     #GPINSTD_USR_NAME:  The name of the installation-defined field.
        l[23:278],    #GPINSTD_USR_DATA:  The data for the installation-defined field.
        l[279:287],   #GPINSTD_USR_FLAG:  The flag for the installation-defined field in the form X<cc>.
    )
    c.execute("INSERT INTO gpinstd VALUES(?, ?, ?, ?)", v)
    print("INFO: (0103) Group Installation Data Record processed.")

def process_gpdfp(l, c):
    v = (
        l[5:13],      #GPDFP_NAME         Group name as taken from the profile name.
        l[14:22],     #GPDFP_DATAAPPL     Default application name for the group.
        l[23:31],     #GPDFP_DATACLAS     Default data class for the group.
        l[32:40],     #GPDFP_MGMTCLAS     Default management class for the group.
        l[41:49],     #GPDFP_STORCLAS     Default storage class for the group.
    )
    c.execute("INSERT INTO gpdfp VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0110) Group DFP Data Record processed.")

def process_gpomvs(l, c):
    v = (
        l[5:13],      #GPOMVS_NAME        Group name as taken from the profile name.
        l[14:24],     #GPOMVS_GID         OMVS z/OS UNIX group identifier (GID) associated with the group name from the profile.
    )
    c.execute("INSERT INTO gpomvs VALUES(?, ?)", v)
    print("INFO: (0120) Group OMVS Data Record processed.")

def process_gpovm(l, c):
    v = (
        l[5:13],      #GPOVM_NAME         Group name as taken from the profile name.
        l[14:24],     #GPOVM_GID          OpenExtensions group identifier (GID) associated with the group name from the profile.
    )
    c.execute("INSERT INTO gpovm VALUES(?, ?)", v)
    print("INFO: (0130) Group OVM Data Record processed.")

def process_gptme(l, c):
    v = (
        l[5:13],      #GPTME_NAME         Group name as taken from the profile name.
        l[14:260],    #GPTME_ROLE         Role profile name.
    )
    c.execute("INSERT INTO gptme VALUES(?, ?)", v)
    print("INFO: (0141) Group TME Record processed.")

def process_gpcsd(l, c):
    v = (
        l[5:13],      #GPCSD_NAME         Group name.
        l[14:18],     #GPCSD_TYPE         Data type for the custom field. Valid values are CHAR, FLAG, HEX, NUM.
        l[19:51],     #GPCSD_KEY          Custom field keyword; maximum length = 8.
        l[52:1152],   #GPCSD_VALUE        Custom field value.
    )
    c.execute("INSERT INTO gpcsd VALUES(?, ?, ?, ?)", v)
    print("INFO: (0151) Group CSDATA Custom Fields Record processed.")

def process_usbd(l, c):
    v = (
        l[5:13],      #USBD_NAME          User ID as taken from the profile name.
        l[14:24],     #USBD_CREATE_DATE   The date that the profile was created.
        l[25:33],     #USBD_OWNER_ID      The user ID or group name that owns the profile.
        l[34:38],     #USBD_ADSP          Does the user have the ADSP attribute?
        l[39:43],     #USBD_SPECIAL       Does the user have the SPECIAL attribute?
        l[44:48],     #USBD_OPER          Does the user have the OPERATIONS attribute?
        l[49:53],     #USBD_REVOKE        Is the user REVOKEd?
        l[54:58],     #USBD_GRPACC        Does the user have the GRPACC attribute?
        l[59:62],     #USBD_PWD_INTERVAL  The number of days that the user's password can be used.
        l[63:73],     #USBD_PWD_DATE      The date that the password was last changed.
        l[74:94],     #USBD_PROGRAMMER    The name associated with the user ID.
        l[95:103],    #USBD_DEFGRP_ID     The default group associated with the user.
        l[104:112],   #USBD_LASTJOB_TIME  The last recorded time that the user entered the system.
        l[113:123],   #USBD_LASTJOB_DATE  The last recorded date that the user entered the system.
        l[124:379],   #USBD_INSTALL_DATA  Installation-defined data.
        l[380:384],   #USBD_UAUDIT        Do all RACHECK and RACDEF SVCs cause logging?
        l[385:389],   #USBD_AUDITOR       Does this user have the AUDITOR attribute?
        l[390:394],   #USBD_NOPWD         "YES" indicates that this user ID can log on without a password using OID card. "NO" indicates that this user must specify a password. "PRO" indicates a protected user ID. "PHR" indicates that the user has a password phrase. See also z/OS Security Server RACF Security Administrator's Guide.
        l[395:399],   #USBD_OIDCARD       Does this user have OIDCARD data?
        l[400:403],   #USBD_PWD_GEN       The current password generation number.
        l[404:407],   #USBD_REVOKE_CNT    The number of unsuccessful logon attempts.
        l[408:452],   #USBD_MODEL         The data set model profile name.
        l[453:456],   #USBD_SECLEVEL      The user's security level.
        l[457:467],   #USBD_REVOKE_DATE   The date that the user will be revoked.
        l[468:478],   #USBD_RESUME_DATE   The date that the user will be resumed.
        l[479:483],   #USBD_ACCESS_SUN    Can the user access the system on Sunday?
        l[484:488],   #USBD_ACCESS_MON    Can the user access the system on Monday?
        l[489:493],   #USBD_ACCESS_TUE    Can the user access the system on Tuesday?
        l[494:498],   #USBD_ACCESS_WED    Can the user access the system on Wednesday?
        l[499:503],   #USBD_ACCESS_THU    Can the user access the system on Thursday?
        l[504:508],   #USBD_ACCESS_FRI    Can the user access the system on Friday?
        l[509:513],   #USBD_ACCESS_SAT    Can the user access the system on Saturday?
        l[514:522],   #USBD_START_TIME    After what time can the user log on?
        l[523:531],   #USBD_END_TIME      After what time can the user not log on?
        l[532:540],   #USBD_SECLABEL      The user's default security label.
        l[541:549],   #USBD_ATTRIBS       Other user attributes (RSTD for users with RESTRICTED attribute).
        l[550:554],   #USBD_PWDENV_EXISTS Has a PKCS#7 envelope been created for the user's current password?
        l[555:559],   #USBD_PWD_ASIS      Should the password be evaluated in the case entered?
        l[560:570],   #USBD_PHR_DATE      The date the password phrase was last changed.
        l[571:574],   #USBD_PHR_GEN       The current password phrase generation number.
        l[575:585],   #USBD_CERT_SEQN     Sequence number that is incremented whenever a certificate for the user is added, deleted, or altered. The starting value might not be 0.
        l[586:590],   #USBD_PPHENV_EXISTS Has the user's current password phrase been PKCS#7 enveloped for possible retrieval?
    )
    c.execute("INSERT INTO usbd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0200) User Basic Data Record processed.")

def process_uscat(l, c):
    v = (
        l[5:13],      #USCAT_NAME         User ID as taken from the profile name.
        l[14:19],     #USCAT_CATEGORY     Category to which the user has access.
    )
    c.execute("INSERT INTO uscat VALUES(?, ?)", v)
    print("INFO: (0201) User Categories Record processed.")

def process_uscla(l, c):
    v = (
        l[5:13],      #USCLA_NAME         User ID as taken from the profile name.
        l[14:22],     #USCLA_CLASS        A class in which the user is allowed to define profiles.
    )
    c.execute("INSERT INTO uscla VALUES(?, ?)", v)
    print("INFO: (0202) User Classes Record processed.")

def process_usgcon(l, c):
    v = (
        l[5:13],      #USGCON_NAME        User ID as taken from the profile name.
        l[14:22],     #USGCON_GRP_ID      The group with which the user is associated.
    )
    c.execute("INSERT INTO usgcon VALUES(?, ?)", v)
    print("INFO: (0203) User Group Connections Record processed.")

def process_usinstd(l, c):
    v = (
        l[5:13],      #USINSTD_NAME       User ID as taken from the profile name.
        l[14:22],     #USINSTD_USR_NAME   The name of the installation-defined field.
        l[23:278],    #USINSTD_USR_DATA   The data for the installation-defined field.
        l[279:287],   #USINSTD_USR_FLAG   The flag for the installation-defined field in the form X<cc>.
    )
    c.execute("INSERT INTO usinstd VALUES(?, ?, ?, ?)", v)
    print("INFO: (0204) User Installation Data Record processed.")

def process_uscon(l, c):
    v = (
        l[5:13],      #USCON_NAME         User ID as taken from the profile name.
        l[14:22],     #USCON_GRP_ID       The group name.
        l[23:33],     #USCON_CONNECT_DATE The date that the user was connected.
        l[34:42],     #USCON_OWNER_ID     The owner of the user-group connection.
        l[43:51],     #USCON_LASTCON_TIME Time that the user last connected to this group.
        l[52:62],     #USCON_LASTCON_DATE Date that the user last connected to this group.
        l[63:71],     #USCON_UACC         The default universal access authority for all new resources the user defines while connected to the specified group. Valid values are NONE, READ, UPDATE, CONTROL, and ALTER.
        l[72:77],     #USCON_INIT_CNT     The number of RACINITs issued for this user/group combination.
        l[78:82],     #USCON_GRP_ADSP     Does this user have the ADSP attribute in this group?
        l[83:87],     #USCON_GRP_SPECIAL  Does this user have GROUP-SPECIAL in this group?
        l[88:92],     #USCON_GRP_OPER     Does this user have GROUP-OPERATIONS in this group?
        l[93:97],     #USCON_REVOKE       Is this user revoked?
        l[98:102],    #USCON_GRP_ACC      Does this user have the GRPACC attribute?
        l[103:107],   #USCON_NOTERMUACC   Does this user have the NOTERMUACC attribute in this group?
        l[108:112],   #USCON_GRP_AUDIT    Does this user have the GROUP-AUDITOR attribute in this group?
        l[113:123],   #USCON_REVOKE_DATE  The date that the user's connection to the group will be revoked.
        l[123:134],   #USCON_RESUME_DATE  The date that the user's connection to the group will be resumed.
    )
    c.execute("INSERT INTO uscon VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0205) User Connect Data Record processed.")

def process_usrsf(l, c):
    v = (
        l[5:13],      #USRSF_NAME         User ID as taken from the profile name.
        l[14:22],     #USRSF_TARG_NODE    Target node name.
        l[23:31],     #USRSF_TARG_USER_ID Target user ID.
        l[32:35],     #USRSF_VERSION      Version of this record.
        l[36:40],     #USRSF_PEER         Is this a peer user ID?
        l[41:45],     #USRSF_MANAGING     Is USRSF_NAME managing this ID?
        l[46:50],     #USRSF_MANAGED      Is USRSF_NAME being managed by this ID?
        l[51:55],     #USRSF_REMOTE_PEND  Is this remote RACF association pending?
        l[56:60],     #USRSF_LOCAL_PEND   Is this local RACF association pending?
        l[61:65],     #USRSF_PWD_SYNC     Is there password synchronization with this user ID?
        l[66:70],     #USRSF_REM_REFUSAL  Was a system error encountered on the remote system?
        l[71:81],     #USRSF_DEFINE_DATE  GMT date stamp for when this record was defined.
        l[82:97],     #USRSF_DEFINE_TIME  GMT time stamp for when this record was defined.
        l[98:108],    #USRSF_ACCEPT_DATE  GMT date stamp when this association was approved or refused. Based on the REMOTE_REFUSAL bit setting.
        l[109:124],   #USRSF_ACCEPT_TIME  GMT time stamp when this association was approved or refused. Based on the REMOTE_REFUSAL bit setting.
        l[125:133],   #USRSF_CREATOR_ID   User ID who created this entry.
    )
    c.execute("INSERT INTO usrsf VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0206) User RRSF Data Record processed.")

def process_uscert(l, c):
    v = (
        l[5:13],      #USCERT_NAME        User ID as taken from the profile name.
        l[14:260],    #USCERT_CERT_NAME   Digital certificate name.
        l[261:293],   #USCERT_CERTLABL    Digital certificate label.
    )
    c.execute("INSERT INTO uscert VALUES(?, ?, ?)", v)
    print("INFO: (0207) User Certificate Name Record processed.")

def process_usnmap(l, c):
    v = (
        l[5:13],      #USNMAP_NAME        User ID as taken from the profile name.
        l[14:46],     #USNMAP_LABEL       The label associated with this mapping.
        l[47:293],    #USNMAP_MAP_NAME    The name of the DIGTNMAP profile associated with this user.
    )
    c.execute("INSERT INTO usnmap VALUES(?, ?, ?)", v)
    print("INFO: (0208) User Associated Mappings Record processed.")

def process_usdmap(l, c):
    v = (
        l[5:13],      #USDMAP_NAME        User ID as taken from the profile name.
        l[14:46],     #USDMAP_LABEL       The label associated with this mapping.
        l[47:293],    #USDMAP_MAP_NAME    The name of the IDIDMAP profile associated with this user. Note: This value is stored in the RACF database in UTF-8 format. If possible, database unload changes this value to the EBCDIC format. If not possible, hexadecimal values are produced.
    )
    c.execute("INSERT INTO usdmap VALUES(?, ?, ?)", v)
    print("INFO: (0209) User Associated Distributed Mappings Record processed.")

def process_usmfa(l, c):
    v = (
        l[5:13],      #USMFA_NAME         User ID as taken from the profile name.
        l[14:34],     #USMFA_FACTOR_NAME  Factor name.
        l[35:54],     #USMFA_FACTOR_ACTIVE  Factor active date. Will be blank if factor is not ACTIVE.
    )
    c.execute("INSERT INTO usmfa VALUES(?, ?, ?)", v)
    print("INFO: (020A) User MFA Factor Data Record processed.")

def process_usmpol(l, c):
    v = (
        l[5:13],      #USMPOL_NAME        User ID as taken from the profile name.
        l[14:34],     #USMPOL_POLICY_NAME MFA Policy name.
    )
    c.execute("INSERT INTO usmpol VALUES(?, ?)", v)
    print("INFO: (020B) User MFA Policies Record processed.")

def process_usdfp(l, c):
    v = (
        l[5:13],      #USDFP_NAME         User ID as taken from the profile name.
        l[14:22],     #USDFP_DATAAPPL     Default application name for the user.
        l[23:31],     #USDFP_DATACLAS     Default data class for the user.
        l[32:40],     #USDFP_MGMTCLAS     Default management class for the user.
        l[41:49],     #USDFP_STORCLAS     Default storage class for the user.
    )
    c.execute("INSERT INTO usdfp VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0210) User DFP Data Record processed.")

def process_ustso(l, c):
    v = (
        l[5:13],      #USTSO_NAME         User ID as taken from the profile name.
        l[14:54],     #USTSO_ACCOUNT      The default account number.
        l[55:135],    #USTSO_COMMAND      The command issued at LOGON.
        l[136:144],   #USTSO_DEST         The default destination identifier.
        l[145:146],   #USTSO_HOLD_CLASS   The default hold class.
        l[147:148],   #USTSO_JOB_CLASS    The default job class.
        l[149:157],   #USTSO_LOGON_PROC   The default logon procedure.
        l[158:168],   #USTSO_LOGON_SIZE   The default logon region size.
        l[169:170],   #USTSO_MSG_CLASS    The default message class.
        l[171:181],   #USTSO_LOGON_MAX    The maximum logon region size.
        l[182:192],   #USTSO_PERF_GROUP   The performance group associated with the user.
        l[193:194],   #USTSO_SYSOUT_CLASS The default sysout class.
        l[195:203],   #USTSO_USER_DATA    The TSO user data, in hexadecimal in the form X<cccc>.
        l[204:212],   #USTSO_UNIT_NAME    The default SYSDA device.
        l[213:221],   #USTSO_SECLABEL     The default logon security label.
    )
    c.execute("INSERT INTO ustso VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0220) User TSO Data Record processed.")

def process_uscics(l, c):
    v = (
        l[5:13],      #USCICS_NAME        User ID as taken from the profile name.
        l[14:17],     #USCICS_OPIDENT     The CICS operator identifier.
        l[18:23],     #USCICS_OPPRTY      The CICS operator priority.
        l[24:28],     #USCICS_NOFORCE     Is the extended recovery facility (XRF) NOFORCE option in effect?
        l[29:34],     #USCICS_TIMEOUT     The terminal time-out value. Expressed in hh:mm
    )
    c.execute("INSERT INTO uscics VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0230) User CICS Data Record processed.")

def process_uscopc(l, c):
    v = (
        l[5:13],      #USCOPC_NAME        User ID as taken from the profile name.
        l[14:17],     #USCOPC_OPCLASS     The class associated with the CICS operator.
    )
    c.execute("INSERT INTO uscopc VALUES(?, ?)", v)
    print("INFO: (0231) User CICS Operator Classes Record processed.")

def process_uscrsl(l, c):
    v = (
        l[5:13],      #USCRSL_NAME        User ID as taken from the profile name.
        l[14:19],     #USCRSL_KEY         RSL key number.
    )
    c.execute("INSERT INTO uscrsl VALUES(?, ?)", v)
    print("INFO: (0232) User CICS RSL Keys Record processed.")

def process_usctsl(l, c):
    v = (
        l[5:13],      #USCTSL_NAME        User ID as taken from the profile name.
        l[14:19],     #USCTSL_KEY         TSL key number.
    )
    c.execute("INSERT INTO usctsl VALUES(?, ?)", v)
    print("INFO: (0233) User CICS TSL Keys Record processed.")

def process_uslan(l, c):
    v = (
        l[5:13],      #USLAN_NAME         User ID as taken from the profile name.
        l[14:17],     #USLAN_PRIMARY      The primary language for the user.
        l[18:21],     #USLAN_SECONDARY    The secondary language for the user.
    )
    c.execute("INSERT INTO uslan VALUES(?, ?, ?)", v)
    print("INFO: (0240) User Language Data Record processed.")

def process_usopr(l, c):
    v = (
        l[5:13],      #USOPR_NAME         User ID as taken from the profile name.
        l[14:19],     #USOPR_STORAGE      The number of megabytes of storage that can be used for message queuing.
        l[20:24],     #USOPR_MASTERAUTH   Does this user have MASTER console authority?
        l[25:29],     #USOPR_ALLAUTH      Does this user have ALL console authority?
        l[30:34],     #USOPR_SYSAUTH      Does this user have SYSAUTH console authority?
        l[35:39],     #USOPR_IOAUTH       Does this user have I/O console authority?
        l[40:44],     #USOPR_CONSAUTH     Does this user have CONS console authority?
        l[45:49],     #USOPR_INFOAUTH     Does this user have INFO console authority?
        l[50:54],     #USOPR_TIMESTAMP    Do console messages contain a timestamp?
        l[55:59],     #USOPR_SYSTEMID     Do console messages contain a system ID?
        l[60:64],     #USOPR_JOBID        Do console messages contain a job ID?
        l[65:69],     #USOPR_MSGID        Do console messages contain a message ID?
        l[70:74],     #USOPR_X            Are the job name and system name to be suppressed for messages issued from the JES3 global processor?
        l[75:79],     #USOPR_WTOR         Does the console receive WTOR messages?
        l[80:84],     #USOPR_IMMEDIATE    Does the console receive immediate messages?
        l[85:89],     #USOPR_CRITICAL     Does the console receive critical event messages?
        l[90:94],     #USOPR_EVENTUAL     Does the console receive eventual event messages?
        l[95:99],     #USOPR_INFO         Does the console receive informational messages?
        l[100:104],   #USOPR_NOBRODCAST   Are broadcast messages to this console suppressed?
        l[105:109],   #USOPR_ALL          Does the console receive all messages?
        l[110:114],   #USOPR_JOBNAMES     Are job names monitored?
        l[115:119],   #USOPR_JOBNAMEST    Are job names monitored with timestamps displayed?
        l[120:124],   #USOPR_SESS         Are user IDs displayed with each TSO initiation and termination?
        l[125:129],   #USOPR_SESST        Are user IDs and timestamps displayed with each TSO initiation and termination?
        l[130:134],   #USOPR_STATUS       Are data set names and dispositions displayed with each data set that is freed?
        l[135:139],   #USOPR_ROUTECODE001 Is this console enabled for route code 001?
        l[135:139],   #USOPR_ROUTECODE001 Is this console enabled for route code 001
        l[140:144],   #USOPR_ROUTECODE002 Is this console enabled for route code 002
        l[145:149],   #USOPR_ROUTECODE003 Is this console enabled for route code 003
        l[150:154],   #USOPR_ROUTECODE004 Is this console enabled for route code 004
        l[155:159],   #USOPR_ROUTECODE005 Is this console enabled for route code 005
        l[160:164],   #USOPR_ROUTECODE006 Is this console enabled for route code 006
        l[165:169],   #USOPR_ROUTECODE007 Is this console enabled for route code 007
        l[170:174],   #USOPR_ROUTECODE008 Is this console enabled for route code 008
        l[175:179],   #USOPR_ROUTECODE009 Is this console enabled for route code 009
        l[180:184],   #USOPR_ROUTECODE010 Is this console enabled for route code 010
        l[185:189],   #USOPR_ROUTECODE011 Is this console enabled for route code 011
        l[190:194],   #USOPR_ROUTECODE012 Is this console enabled for route code 012
        l[195:199],   #USOPR_ROUTECODE013 Is this console enabled for route code 013
        l[200:204],   #USOPR_ROUTECODE014 Is this console enabled for route code 014
        l[205:209],   #USOPR_ROUTECODE015 Is this console enabled for route code 015
        l[210:214],   #USOPR_ROUTECODE016 Is this console enabled for route code 016
        l[215:219],   #USOPR_ROUTECODE017 Is this console enabled for route code 017
        l[220:224],   #USOPR_ROUTECODE018 Is this console enabled for route code 018
        l[225:229],   #USOPR_ROUTECODE019 Is this console enabled for route code 019
        l[230:234],   #USOPR_ROUTECODE020 Is this console enabled for route code 020
        l[235:239],   #USOPR_ROUTECODE021 Is this console enabled for route code 021
        l[240:244],   #USOPR_ROUTECODE022 Is this console enabled for route code 022
        l[245:249],   #USOPR_ROUTECODE023 Is this console enabled for route code 023
        l[250:254],   #USOPR_ROUTECODE024 Is this console enabled for route code 024
        l[255:259],   #USOPR_ROUTECODE025 Is this console enabled for route code 025
        l[260:264],   #USOPR_ROUTECODE026 Is this console enabled for route code 026
        l[265:269],   #USOPR_ROUTECODE027 Is this console enabled for route code 027
        l[270:274],   #USOPR_ROUTECODE028 Is this console enabled for route code 028
        l[275:279],   #USOPR_ROUTECODE029 Is this console enabled for route code 029
        l[280:284],   #USOPR_ROUTECODE030 Is this console enabled for route code 030
        l[285:289],   #USOPR_ROUTECODE031 Is this console enabled for route code 031
        l[290:294],   #USOPR_ROUTECODE032 Is this console enabled for route code 032
        l[295:299],   #USOPR_ROUTECODE033 Is this console enabled for route code 033
        l[300:304],   #USOPR_ROUTECODE034 Is this console enabled for route code 034
        l[305:309],   #USOPR_ROUTECODE035 Is this console enabled for route code 035
        l[310:314],   #USOPR_ROUTECODE036 Is this console enabled for route code 036
        l[315:319],   #USOPR_ROUTECODE037 Is this console enabled for route code 037
        l[320:324],   #USOPR_ROUTECODE038 Is this console enabled for route code 038
        l[325:329],   #USOPR_ROUTECODE039 Is this console enabled for route code 039
        l[330:334],   #USOPR_ROUTECODE040 Is this console enabled for route code 040
        l[335:339],   #USOPR_ROUTECODE041 Is this console enabled for route code 041
        l[340:344],   #USOPR_ROUTECODE042 Is this console enabled for route code 042
        l[345:349],   #USOPR_ROUTECODE043 Is this console enabled for route code 043
        l[350:354],   #USOPR_ROUTECODE044 Is this console enabled for route code 044
        l[355:359],   #USOPR_ROUTECODE045 Is this console enabled for route code 045
        l[360:364],   #USOPR_ROUTECODE046 Is this console enabled for route code 046
        l[365:369],   #USOPR_ROUTECODE047 Is this console enabled for route code 047
        l[370:374],   #USOPR_ROUTECODE048 Is this console enabled for route code 048
        l[375:379],   #USOPR_ROUTECODE049 Is this console enabled for route code 049
        l[380:384],   #USOPR_ROUTECODE050 Is this console enabled for route code 050
        l[385:389],   #USOPR_ROUTECODE051 Is this console enabled for route code 051
        l[390:394],   #USOPR_ROUTECODE052 Is this console enabled for route code 052
        l[395:399],   #USOPR_ROUTECODE053 Is this console enabled for route code 053
        l[400:404],   #USOPR_ROUTECODE054 Is this console enabled for route code 054
        l[405:409],   #USOPR_ROUTECODE055 Is this console enabled for route code 055
        l[410:414],   #USOPR_ROUTECODE056 Is this console enabled for route code 056
        l[415:419],   #USOPR_ROUTECODE057 Is this console enabled for route code 057
        l[420:424],   #USOPR_ROUTECODE058 Is this console enabled for route code 058
        l[425:429],   #USOPR_ROUTECODE059 Is this console enabled for route code 059
        l[430:434],   #USOPR_ROUTECODE060 Is this console enabled for route code 060
        l[435:439],   #USOPR_ROUTECODE061 Is this console enabled for route code 061
        l[440:444],   #USOPR_ROUTECODE062 Is this console enabled for route code 062
        l[445:449],   #USOPR_ROUTECODE063 Is this console enabled for route code 063
        l[450:454],   #USOPR_ROUTECODE064 Is this console enabled for route code 064
        l[455:459],   #USOPR_ROUTECODE065 Is this console enabled for route code 065
        l[460:464],   #USOPR_ROUTECODE066 Is this console enabled for route code 066
        l[465:469],   #USOPR_ROUTECODE067 Is this console enabled for route code 067
        l[470:474],   #USOPR_ROUTECODE068 Is this console enabled for route code 068
        l[475:479],   #USOPR_ROUTECODE069 Is this console enabled for route code 069
        l[480:484],   #USOPR_ROUTECODE070 Is this console enabled for route code 070
        l[485:489],   #USOPR_ROUTECODE071 Is this console enabled for route code 071
        l[490:494],   #USOPR_ROUTECODE072 Is this console enabled for route code 072
        l[495:499],   #USOPR_ROUTECODE073 Is this console enabled for route code 073
        l[500:504],   #USOPR_ROUTECODE074 Is this console enabled for route code 074
        l[505:509],   #USOPR_ROUTECODE075 Is this console enabled for route code 075
        l[510:514],   #USOPR_ROUTECODE076 Is this console enabled for route code 076
        l[515:519],   #USOPR_ROUTECODE077 Is this console enabled for route code 077
        l[520:524],   #USOPR_ROUTECODE078 Is this console enabled for route code 078
        l[525:529],   #USOPR_ROUTECODE079 Is this console enabled for route code 079
        l[530:534],   #USOPR_ROUTECODE080 Is this console enabled for route code 080
        l[535:539],   #USOPR_ROUTECODE081 Is this console enabled for route code 081
        l[540:544],   #USOPR_ROUTECODE082 Is this console enabled for route code 082
        l[545:549],   #USOPR_ROUTECODE083 Is this console enabled for route code 083
        l[550:554],   #USOPR_ROUTECODE084 Is this console enabled for route code 084
        l[555:559],   #USOPR_ROUTECODE085 Is this console enabled for route code 085
        l[560:564],   #USOPR_ROUTECODE086 Is this console enabled for route code 086
        l[565:569],   #USOPR_ROUTECODE087 Is this console enabled for route code 087
        l[570:574],   #USOPR_ROUTECODE088 Is this console enabled for route code 088
        l[575:579],   #USOPR_ROUTECODE089 Is this console enabled for route code 089
        l[580:584],   #USOPR_ROUTECODE090 Is this console enabled for route code 090
        l[585:589],   #USOPR_ROUTECODE091 Is this console enabled for route code 091
        l[590:594],   #USOPR_ROUTECODE092 Is this console enabled for route code 092
        l[595:599],   #USOPR_ROUTECODE093 Is this console enabled for route code 093
        l[600:604],   #USOPR_ROUTECODE094 Is this console enabled for route code 094
        l[605:609],   #USOPR_ROUTECODE095 Is this console enabled for route code 095
        l[610:614],   #USOPR_ROUTECODE096 Is this console enabled for route code 096
        l[615:619],   #USOPR_ROUTECODE097 Is this console enabled for route code 097
        l[620:624],   #USOPR_ROUTECODE098 Is this console enabled for route code 098
        l[625:629],   #USOPR_ROUTECODE099 Is this console enabled for route code 099
        l[630:634],   #USOPR_ROUTECODE100 Is this console enabled for route code 100
        l[635:639],   #USOPR_ROUTECODE101 Is this console enabled for route code 101
        l[640:644],   #USOPR_ROUTECODE102 Is this console enabled for route code 102
        l[645:649],   #USOPR_ROUTECODE103 Is this console enabled for route code 103
        l[650:654],   #USOPR_ROUTECODE104 Is this console enabled for route code 104
        l[655:659],   #USOPR_ROUTECODE105 Is this console enabled for route code 105
        l[660:664],   #USOPR_ROUTECODE106 Is this console enabled for route code 106
        l[665:669],   #USOPR_ROUTECODE107 Is this console enabled for route code 107
        l[670:674],   #USOPR_ROUTECODE108 Is this console enabled for route code 108
        l[675:679],   #USOPR_ROUTECODE109 Is this console enabled for route code 109
        l[680:684],   #USOPR_ROUTECODE110 Is this console enabled for route code 110
        l[685:689],   #USOPR_ROUTECODE111 Is this console enabled for route code 111
        l[690:694],   #USOPR_ROUTECODE112 Is this console enabled for route code 112
        l[695:699],   #USOPR_ROUTECODE113 Is this console enabled for route code 113
        l[700:704],   #USOPR_ROUTECODE114 Is this console enabled for route code 114
        l[705:709],   #USOPR_ROUTECODE115 Is this console enabled for route code 115
        l[710:714],   #USOPR_ROUTECODE116 Is this console enabled for route code 116
        l[715:719],   #USOPR_ROUTECODE117 Is this console enabled for route code 117
        l[720:724],   #USOPR_ROUTECODE118 Is this console enabled for route code 118
        l[725:729],   #USOPR_ROUTECODE119 Is this console enabled for route code 119
        l[730:734],   #USOPR_ROUTECODE120 Is this console enabled for route code 120
        l[735:739],   #USOPR_ROUTECODE121 Is this console enabled for route code 121
        l[740:744],   #USOPR_ROUTECODE122 Is this console enabled for route code 122
        l[745:749],   #USOPR_ROUTECODE123 Is this console enabled for route code 123
        l[750:754],   #USOPR_ROUTECODE124 Is this console enabled for route code 124
        l[755:759],   #USOPR_ROUTECODE125 Is this console enabled for route code 125
        l[760:764],   #USOPR_ROUTECODE126 Is this console enabled for route code 126
        l[765:769],   #USOPR_ROUTECODE127 Is this console enabled for route code 127
        l[770:774],   #USOPR_ROUTECODE128 Is this console enabled for route code 128
        l[775:783],   #USOPR_LOGCMDRESP   Specifies the logging of command responses received by the extended operator. Valid values are SYSTEM, NO, and blank.
        l[784:788],   #USOPR_MIGRATIONID  Is this extended operator to receive a migration ID?
        l[789:797],   #USOPR_DELOPERMSG   Does this extended operator receive delete operator messages? Valid values are NORMAL, ALL, and NONE.
        l[798:806],   #USOPR_RETRIEVE_KEY Specifies a retrieval key used for searching. A null value is indicated by NONE.
        l[807:815],   #USOPR_CMDSYS       The name of the system that the extended operator is connected to for command processing.
        l[816:820],   #USOPR_UD           Is this operator to receive undeliverable messages?
        l[821:829],   #USOPR_ALTGRP_ID    The default group associated with this operator.
        l[830:834],   #USOPR_AUTO         Is this operator to receive messages automated within the sysplex?
        l[835:839],   #USOPR_HC           Is this operator to receive messages that are directed to hardcopy?
        l[840:844],   #USOPR_INT          Is this operator to receive messages that are directed to console ID zero?
        l[845:849],   #USOPR_UNKN         Is this operator to receive messages which are directed to unknown console IDs?
    )
    c.execute("INSERT INTO usopr VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0250) User OPERPARM Data Record processed.")

def process_usoprp(l, c):
    v = (
        l[5:13],      #USOPRP_NAME        User ID as taken from the profile name.
        l[14:22],     #USOPRP_SYSTEM      System name.
    )
    c.execute("INSERT INTO usoprp VALUES(?, ?)", v)
    print("INFO: (0251) User OPERPARM Scope Record processed.")

def process_uswrk(l, c):
    v = (
        l[5:13],      #USWRK_NAME         User ID as taken from the profile name.
        l[14:74],     #USWRK_AREA_NAME    Area for delivery.
        l[75:135],    #USWRK_BUILDING     Building for delivery.
        l[136:196],   #USWRK_DEPARTMENT   Department for delivery.
        l[197:257],   #USWRK_ROOM         Room for delivery.
        l[258:318],   #USWRK_ADDR_LINE1   Address line 1.
        l[319:379],   #USWRK_ADDR_LINE2   Address line 2.
        l[380:440],   #USWRK_ADDR_LINE3   Address line 3.
        l[441:501],   #USWRK_ADDR_LINE4   Address line 4.
        l[502:757],   #USWRK_ACCOUNT      Account number.
    )
    c.execute("INSERT INTO uswrk VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0260) User WORKATTR Data Record processed.")

def process_usomvs(l, c):
    v = (
        l[5:13],      #USOMVS_NAME        User name as taken from the profile name.
        l[14:24],     #USOMVS_UID         z/OS UNIX user identifier (UID) associated with the user name from the profile.
        l[25:1048],   #USOMVS_HOME_PATH   HOME PATH associated with the z/OS UNIX user identifier (UID).
        l[1049:2072], #USOMVS_PROGRAM     Default Program associated with the z/OS UNIX user identifier (UID).
        l[2073:2083], #USOMVS_CPUTIMEMAX  Maximum CPU time associated with the UID.
        l[2084:2094], #USOMVS_ASSIZEMAX   Maximum address space size associated with the UID.
        l[2095:2105], #USOMVS_FILEPROCMAX Maximum active or open files associated with the UID.
        l[2106:2116], #USOMVS_PROCUSERMAX Maximum number of processes associated with the UID.
        l[2117:2127], #USOMVS_THREADSMAX  Maximum number of threads associated with the UID.
        l[2128:2138], #USOMVS_MMAPAREAMAX Maximum mappable storage amount associated with the UID.
        l[2139:2148], #USOMVS_MEMLIMIT    Maximum size of non-shared memory
        l[2149:2158], #USOMVS_SHMEMAX     Maximum size of shared memory
    )
    c.execute("INSERT INTO usomvs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0270) User OMVS Data Record processed.")

def process_usnetv(l, c):
    v = (
        l[5:13],      #USNETV_NAME        User ID as taken from profile name
        l[14:269],    #USNETV_IC          Command list processed at logon
        l[270:278],   #USNETV_CONSNAME    Default console name
        l[279:287],   #USNETV_CTL         CTL value: GENERAL, GLOBAL, or SPECIFIC
        l[288:292],   #USNETV_MSGRECVR    Eligible to receive unsolicited messages?
        l[293:297],   #USNETV_NGMFADMN    Authorized to NetView graphic monitoring facility?
        l[299:306],   #USNETV_NGMFVSPN    Value of view span options
    )
    c.execute("INSERT INTO usnetv VALUES (?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0280) User NETVIEW Segment Record processed.")

def process_usnopc(l, c):
    v = (
        l[5:13],      #USNOPC_NAME        User ID as taken from the profile name
        l[14:19],     #USNOPC_OPCLASS     OPCLASS value from 1 to 2040
    )
    c.execute("INSERT INTO usnopc VALUES (?, ?)", v)
    print("INFO: (0281) User OPCLASS Record processed.")

def process_usndom(l, c):
    v = (
        l[5:13],      #USNDOM_NAME        User ID as taken from the profile name
        l[14:19],     #USNDOM_DOMAINS     DOMAIN value.
    )
    c.execute("INSERT INTO usndom VALUES (?, ?)", v)
    print("INFO: (0282) User DOMAINS Record processed.")

def process_usdce(l, c):
    v = (
        l[5:13],      #USDCE_NAME         RACF user name as taken from the profile name.
        l[14:50],     #USDCE_UUID         DCE UUID associated with the user name from the profile.
        l[51:1074],   #USDCE_DCE_NAME     DCE principal name associated with this user.
        l[1075:2098], #USDCE_HOMECELL     Home cell name.
        l[2099:2135], #USDCE_HOMEUUID     Home cell UUID.
        l[2136:2140], #USDCE_AUTOLOGIN    Is this user eligible for an automatic DCE login?
    )
    c.execute("INSERT INTO usdce VALUES (?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0290) User DCE Data Record processed.")

def process_usovm(l, c):
    v = (
        l[5:13],      #USOVM_NAME         User name as taken from the profile name.
        l[14:24],     #USOVM_UID          User identifier (UID) associated with the user name from the profile.
        l[25:1048],   #USOVM_HOME_PATH    Home path associated with the user identifier (UID).
        l[1049:2072], #USOVM_PROGRAM      Default program associated with the user identifier (UID).
        l[2073:3096], #USOVM_FSROOT       File system root for this user.
    )
    c.execute("INSERT INTO usovm VALUES (?, ?, ?, ?, ?)", v)
    print("INFO: (02A0) User OVM Data Record processed.")

def process_uslnot(l, c):
    v = (
        l[5:13],      #USLNOT_NAME        User ID as taken from the profile name.
        l[14:78],     #USLNOT_SNAME       LNOTES short name associated with the user ID.
    )
    c.execute("INSERT INTO uslnot VALUES(?, ?)", v)
    print("INFO: (02B0) User LNOTES Data Record processed.")

def process_usnds(l, c):
    v = (
        l[5:13],      #USNDS_NAME         User ID as taken from the profile name.
        l[14:260],    #USNDS_UNAME        NDS user name associated with the user ID.
    )
    c.execute("INSERT INTO usnds VALUES(?, ?)", v)
    print("INFO: (02C0) User NDS Data Record processed.")

def process_uskerb(l, c):
    v = (
        l[5:13],      #USKERB_NAME        RACF user name as taken from the profile.
        l[14:254],    #USKERB_KERBNAME    The Kerberos principal name.
        l[255:265],   #USKERB_MAX_LIFE    Maximum ticket life.
        l[266:269],   #USKERB_KEY_VERS    Current key version.
        l[270:274],   #USKERB_ENCRYPT_DES Is key encryption using DES enabled?
        l[275:279],   #USKERB_ENCRYPT_DES3  Is key encryption using DES3 enabled?
        l[280:284],   #USKERB_ENCRYPT_DESD  Is key encryption using DES with derivation enabled?
        l[285:289],   #USKERB_ENCRPT_A128 Is key encryption using AES128 enabled?
        l[290:294],   #USKERB_ENCRPT_A256 Is key encryption using AES256 enabled?
        l[350:358],   #USKERB_KEY_FROM    Key source. Valid values are PASSWORD or PHRASE.
    )
    c.execute("INSERT INTO uskerb VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (02D0) User KERB Data Record processed.")

def process_usproxy(l, c):
    v = (
        l[5:13],      #USPROXY_NAME       RACF user name as taken from the profile name.
        l[14:1037],   #USPROXY_LDAP_HOST  LDAP server URL.
        l[1038:2061], #USPROXY_BIND_DN    LDAP BIND distinguished name.
    )
    c.execute("INSERT INTO usproxy VALUES(?, ?, ?)", v)
    print("INFO: (02E0) User PROXY Record processed.")

def process_useim(l, c):
    v = (
        l[5:13],      #USEIM_NAME         User name.
        l[14:260],    #USEIM_LDAPPROF     EIM LDAPBIND profile name.
    )
    c.execute("INSERT INTO useim VALUES(?, ?)", v)
    print("INFO: (02F0) User EIM Data Record processed.")

def process_uscsd(l, c):
    v = (
        l[5:13],      #USCSD_NAME         User name.
        l[14:18],     #USCSD_TYPE         Data type for the custom field. Valid values are CHAR, FLAG, HEX, NUM.
        l[19:51],     #USCSD_KEY          Custom field keyword; maximum length = 8.
        l[52:1152],   #USCSD_VALUE        Custom field value.
    )
    c.execute("INSERT INTO uscsd VALUES(?, ?, ?, ?)", v)
    print("INFO: (02G1) User CSDATA Custom Fields Record processed.")

def process_usmfac(l, c):
    v = (
        l[5, 13],     #USMFAC_NAME        User ID as taken from the profile name.
        l[14:34],     #USMFAC_FACTOR_NAME Factor name.
        l[35:55],     #USMFAC_TAG_NAME    The tag name associated with the factor.
        l[56:1080],   #USMFAC_TAG_VALUE   Tag value associated with the tag name.
    )
    c.execute("INSERT INTO usmfac VALUES (?, ?, ?, ?)", v)
    print("INFO: (1210) User MFA Factor Tags Data Record processed.")

def process_dsbd(l, c):
    v = (
        l[5:49],      #DSBD_NAME          Data set name as taken from the profile name.
        l[50:56],     #DSBD_VOL           Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:61],     #DSBD_GENERIC       Is this a generic profile?
        l[62:72],     #DSBD_CREATE_DATE   Date the profile was created.
        l[73:81],     #DSBD_OWNER_ID      The user ID or group name that owns the profile.
        l[82:92],     #DSBD_LASTREF_DATE  The date that the data set was last referenced.
        l[93:103],    #DSBD_LASTCHG_DATE  The date that the data set was last changed.
        l[104:109],   #DSBD_ALTER_CNT     The number of times that the data set was accessed with ALTER authority.
        l[110:115],   #DSBD_CONTROL_CNT   The number of times that the data set was accessed with CONTROL authority.
        l[116:121],   #DSBD_UPDATE_CNT    The number of times that the data set was accessed with UPDATE authority.
        l[122:127],   #DSBD_READ_CNT      The number of times that the data set was accessed with READ authority.
        l[128:136],   #DSBD_UACC          The universal access of this data set. Valid values are NONE, EXECUTE, READ, UPDATE, CONTROL, and ALTER.
        l[137:141],   #DSBD_GRPDS         Is this a group data set?
        l[142:150],   #DSBD_AUDIT_LEVEL   Indicates the level of resource-owner-specified auditing that is performed. Valid values are ALL, SUCCESS, FAIL, and NONE.
        l[151:159],   #DSBD_GRP_ID        The connect group of the user who created this data set.
        l[160:168],   #DSBD_DS_TYPE       The type of the data set. Valid values are VSAM, NONVSAM, TAPE, and MODEL.
        l[169:172],   #DSBD_LEVEL         The level of the data set.
        l[173:181],   #DSBD_DEVICE_NAME   The EBCDIC name of the device type on which the data set resides.
        l[182:190],   #DSBD_GAUDIT_LEVEL  Indicates the level of auditor-specified auditing that is performed. Valid values are ALL, SUCCESS, FAIL, and NONE.
        l[191:446],   #DSBD_INSTALL_DATA  Installation-defined data.
        l[447:455],   #DSBD_AUDIT_OKQUAL  The resource-owner-specified successful access audit qualifier. This is set to blanks if AUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[456:464],   #DSBD_AUDIT_FAQUAL  The resource-owner-specified failing access audit qualifier. This is set to blanks if AUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[465:473],   #DSBD_GAUDIT_OKQUAL The auditor-specified successful access audit qualifier. This is set to blanks if GAUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[474:482],   #DSBD_GAUDIT_FAQUAL The auditor-specified failing access audit qualifier. This is set to blanks if GAUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[483:487],   #DSBD_WARNING       Does this data set have the WARNING attribute?
        l[488:491],   #DSBD_SECLEVEL      The data set security level.
        l[492:500],   #DSBD_NOTIFY_ID     User ID that is notified when violations occur.
        l[501:506],   #DSBD_RETENTION     Retention period of the data set.
        l[507:511],   #DSBD_ERASE         For a DASD data set, is this data set scratched when the data set is deleted?
        l[512:520],   #DSBD_SECLABEL      Security label of the data set.
    )
    c.execute("INSERT INTO dsbd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0400) Data Set Basic Data Record processed.")

def process_dscat(l, c):
    v = (
        l[5:49],      #DSCAT_NAME         Data set name as taken from the profile name.
        l[50:56],     #DSCAT_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:62],     #DSCAT_CATEGORY     Category associated with this data set.
    )
    c.execute("INSERT INTO dscat VALUES(?, ?, ?)", v)
    print("INFO: (0401) Data Set Categories Record processed.")

def process_dscacc(l, c):
    v = (
        l[5:49],      #DSCACC_NAME        Data set name as taken from the profile name.
        l[50:56],     #DSCACC_VOL         Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:65],     #DSCACC_CATYPE      The type of conditional access checking that is being performed. Valid values are APPCPORT, PROGRAM, CONSOLE, TERMINAL, JESINPUT, and SERVAUTH.
        l[66:74],     #DSCACC_CANAME      The name of a conditional access element that is permitted access.
        l[75:83],     #DSCACC_AUTH_ID     The user ID or group name that is authorized to the data set.
        l[84:92],     #DSCACC_ACCESS      The access of the conditional access element/user combination. Valid values are NONE, EXECUTE, READ, UPDATE, CONTROL, and ALTER.
        l[93:98],     #DSCACC_ACCESS_CNT  The number of times that the data set was accessed.
        l[99:107],    #DSCACC_NET_ID      The network name when DSCACC_CATYPE is APPCPORT.
        l[108:352],   #DSCACC_CACRITERIA  The IP name when DSCACC_CATYPE is SERVAUTH.
    )
    c.execute("INSERT INTO dscacc VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0402) Data Set Conditional Access Record processed.")

def process_dsvol(l, c):
    v = (
        l[5:49],      #DSVOL_NAME         Data set name as taken from the profile name.
        l[50:56],     #DSVOL_VOL          Volume upon which this data set resides.
        l[57:63],     #DSVOL_VOL_NAME     A volume upon which the data set resides.
    )
    c.execute("INSERT INTO dsvol VALUES(?, ?, ?)", v)
    print("INFO: (0403) Data Set Volumes Record processed.")

def process_dsacc(l, c):
    v = (
        l[5:49],      #DSACC_NAME         Data set name as taken from the profile name.
        l[50:56],     #DSACC_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:65],     #DSACC_AUTH_ID      The user ID or group name that is authorized to the data set.
        l[66:74],     #DSACC_ACCESS       The access allowed to the user. Valid values are NONE, EXECUTE, READ, UPDATE, CONTROL, and ALTER.
        l[75:80],     #DSACC_ACCESS_CNT   The number of times that the data set was accessed.
    )
    c.execute("INSERT INTO dsacc VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0404) Data Set Access Record processed.")

def process_dsinstd(l, c):
    v = (
        l[5:49],      #DSINSTD_NAME       Data set name as taken from the profile name.
        l[50:56],     #DSINSTD_VOL        Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:65],     #DSINSTD_USR_NAME   The name of the installation-defined field.
        l[66:321],    #DSINSTD_USR_DATA   The data for the installation-defined field.
        l[322:330],   #DSINSTD_USR_FLAG   The flag for the installation-defined field in the form X<cc>.
    )
    c.execute("INSERT INTO dsinstd VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0405) Data Set Installation Data Record processed.")

def process_dsdfp(l, c):
    v = (
        l[5:49],      #DSDFP_NAME         Data set name as taken from the profile name.
        l[50:56],     #DSDFP_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile. 
        l[57:65],     #DSDFP_RESOWNER_ID  The resource owner of the data set.
        l[66:130],    #DSDFP_DATAKEY      The label of the ICSF key that is used to encrypt the data of any newly allocated data set.
    )
    c.execute("INSERT INTO dsdfp VALUES(?, ?, ?, ?)", v)
    print("INFO: (0410) Data Set DFP Data Record processed.")

def process_dstme(l, c):
    v = (
        l[5:49],      #DSTME_NAME         Data set name as taken from the profile name.
        l[50:56],     #DSTME_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:303],    #DSTME_ROLE_NAME    Role profile name.
        l[304:312],   #DSTME_ACCESS_AUTH  Access permission to this resource as defined by the role.
        l[313:321],   #DSTME_COND_CLASS   Class name for conditional access.
        l[322, 568],  #DSTME_COND_PROF    Resource profile for conditional access.
    )
    c.execute("INSERT INTO dstme VALUES(?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0421) Data Set TME Role Record processed.")
