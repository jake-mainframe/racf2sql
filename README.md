# RACF Unload to SQLite

A collection of scripts which translate the RACF unload database into a big friendly SQLite database, which can then be queried.

The emitted DB is in a format that resembles the [format of the unload files](https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.1.0/com.ibm.zos.v2r1.icha300/format.htm) as closely as possible to make it easy to maintain and understand using the IBM documentation on the subject.
