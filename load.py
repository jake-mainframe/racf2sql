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
