# RACF Unload to SQLite

Using the RACF Database Unload Utility [`IRRDBU00`](https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.1.0/com.ibm.zos.v2r1.icha700/dbuh2.htm) one can obtain a flat-file representation of a RACF Database. This makes it very easy to transmit the DB off the Mainframe.

Unfortunately, the flat file is not particularly easy to query. Scripts exist that can process this format, but only for Microsoft Excel, Microsoft Access, and various z/OS-only utilities. As we would like to perform offline analysis of the data in an easily queriable format, these will not do.

These scripts resolve this by translating the flat file into a SQLite database, which is an easily queryable standard.

## Usage

1. Obtain the RACF unload database. See documentation on `IRRDBU00` for how to do this or consult your local Mainframe operator.
2. In this directory, execute `run.py unload_file sqlite_file` where `unload_file` is your RACF unload flat file and `sqlite_file` is the file you want to output the database to.
3. Enjoy.

This script can currently *only* process one RACF unload file into one sqlite database, in one go. Interruptions and multiple files are not supported. This should be relatively easy to fix if necessary, but in the meantime, if you have multiple unload files (e.g. because of a split RACF database), concatenating them together into one really big file *should* work, but I haven't actually tried it.

## Development

The format of the script is almost entirely based on IBM's documentation on the [`IRRDBU00` output format](https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.1.0/com.ibm.zos.v2r1.icha300/format.htm).

In order to amend the script to fix an issue with the processing of a record or in order to implement a new record type, the following steps should be taken:

1. In `init.py` identify where the record type's `init_` function is called, and modify or create it appropriately. (Note: the records are ordered in the same way they appear in IBM's documentation for added readability.)
2. In `load.py` identify where the record type's `process_` function is called, and modify or create it appropriately. (Note: the records and their fields are also ordered the same as in the documentation).

**NOTE:** The substrings used in `load.py` have their start index **one lower than IBM's documentation**. This is intentional, and is the case because of differences between IBM's documentation and how Python processes substrings.

The output of these scripts is intentionally designed to closely match the format of the DB itself (or at least of the unload file) to ensure there is minimal complexity.

Specifically:
- Each table name is the same as the record field prefix for that table in IBM's docs.
- Each column nane is the same as the name of the field in IBM's docs, without the table prefix.

So, if IBM defined a record type with a field called `ASDF_POTATO`, then that field would go into column `potato` in table `asdf`. This hopefully means that users can mostly just use IBM's documentation to figure out what queries they want to make. The only exception is column names like `primary` which get an underscore prefixed (e.g. becomes `_primary`) so as to avoid conflicts with SQL keywords.
