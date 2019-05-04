import click
from settings import MONGO_HOST, MONGO_PORT

@click.command()
@click.option('--progname', prompt="Programe Name")
def main(progname):
    click.echo(progname)
    
if __name__ == "__main__":
    pass