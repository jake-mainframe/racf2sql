import click
from racf2sql.dispatch import populate_db

@click.command()
@click.argument('unload')
@click.argument('database')
@click.option('-a', '--append', is_flag=True, help='Append to existing database')
def cli(unload, database, append):
    """Process the UNLOAD file and output it in SQLite format to DATABASE."""
    populate_db(unload, database, append)
    click.secho('Done!', fg='green')