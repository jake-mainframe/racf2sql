#!/usr/bin/env python3

import sys

import init
import load

racf_file = sys.argv[1]
db_file = sys.argv[2]

init.init_db(db_file)
load.load_racf(racf_file, db_file)
