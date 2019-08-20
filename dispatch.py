import sqlite3
import click
from init import init_db
from load import load_racf

def populate_db(unload, db, append=False):
    if needs_init(db):
        click.secho("INFO: Database not initialised; running initialisation.")
        init_db(db)
        click.secho("INFO: Initialisation complete; processing unload file.", fg='green')
        load_racf(unload, db)
    elif not append:
        click.secho("ERROR: Database already initialised; run with --append flag to allow appending of db content.", fg='red', bold=True)
        exit(1)
    else:
        click.secho("INFO: Database already initialised; appending unload file to existing db.", fg='green')
        load_racf(unload, db)

def needs_init(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for t in c.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='gpbd'"):
        return False
    return True