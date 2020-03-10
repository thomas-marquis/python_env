import requests
import click
import textwrap

version = '0.1.0'
API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=version)
def main():
    click.echo('starting...')
    click.echo('started !')

    with requests.get(API_URL) as res:
        res.raise_for_status()
        data = res.json()

    title = data['title']
    extract = data['extract']

    click.secho(title, fg='green')
    click.echo(textwrap.fill(extract))


if __name__ == "__main__":
    main()
