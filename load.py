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
