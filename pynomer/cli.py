import urllib
import requests
import json
import pynomer
import click
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class NoResultException(Exception):
    pass


@click.group()
def cli():
    pass


@cli.command()
def version():
    """
        Show Version.

        Usage::

            pynomer version
        """
    click.echo(pynomer.version())


@cli.command()
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
def clean(properties):
    """
        Cleans term matcher cache.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pynomer clean
        """
    click.echo(pynomer.clean(properties))


@cli.command()
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
def input_schema(properties):
    """
        Show input schema in JSON.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pynomer input_schema
            pynomer input_schema -p ./new_properties.txt
        """
    click.echo(pynomer.input_schema(properties))


@cli.command()
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
def output_schema(properties):
    """
        Show output schema.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pynomer output_schema
            pynomer output_schema -p ./new_properties.txt
        """
    click.echo(pynomer.output_schema(properties))


@cli.command()
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
def properties(properties):
    """
        Lists configuration properties. Can be used to make a local copy and override
        default settings.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pynomer properties
            pynomer properties -p ./new_properties.txt
        """
    click.echo(pynomer.properties(properties))


@cli.command()
@click.option(
    "--output-format",
    "-o",
    type=str,
    help="""
            tsv, json""",
    default="tsv",
)
@click.option(
    "--verbose",
    "-v",
    type=bool,
    help="""
            if set, matcher descriptions are included for tsv.""",
    default=False,
)
def matchers(output_format, verbose):
    """
        Lists supported matcher and (optionally) their descriptions.

        :param o: ["tsv", "json"]  Output format. Default: "tsv"
        :param v: [bool]  If set, matcher descriptions are included for tsv. Default: False

        Usage::

            pynomer matchers
        """
    click.echo(pynomer.matchers(output_format, verbose))


@cli.command()
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
@click.argument("filepath", required=True)
def validate_term(filepath, properties):
    """
        Validate terms.

        :param filepath: [string]  Path or URL to TaxonCache file. Default: <empty string>
        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pynomer validate_term https://zenodo.org/record/1213465/files/taxonCacheFirst10.tsv
        """
    click.echo(pynomer.validate_term(filepath, properties))


@cli.command()
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
@click.argument("filepath", required=True)
def validate_term_link(filepath, properties):
    """
        Validate term links.

        :param filepath: [string]  Path or URL to TaxonMap file. Default: <empty string>
        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pynomer validate_term_link
        """
    click.echo(pynomer.validate_term_link(filepath, properties))


@cli.command()
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
@click.option(
    "--matcher",
    "-m",
    type=str,
    help="""
            Default: globi-taxon-cache""",
    default="globi-taxon-cache",
)
@click.option(
    "-e",
    is_flag=True,
    help="""
            Activate echo -e option""",
)
@click.argument("query", required=True, default="")
def replace(query, matcher, properties, e):
    """
        Replace exact term matches in row. The input schema is used
        to select the id and/or name to match to. The output schema is
        used to select the columns to write into.

        :param query: [string]  Query. Default: <empty string>
        :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pynomer replace "\\tHomo sapiens"

            pynomer replace "ITIS:180547\\t" -m globi-enrich
        """
    click.echo(pynomer.replace(query, matcher, properties, echo_opt="-e" if e else ""))


@cli.command()
@click.option(
    "--output-format",
    "-o",
    type=str,
    help="""
            tsv, json""",
    default="tsv",
)
@click.option(
    "--properties",
    "-p",
    type=str,
    help="""
            Path to properties file to override defaults.
            Default: <empty string>""",
    default="",
)
@click.option(
    "--matcher",
    "-m",
    type=str,
    help="""
            Default: globi-taxon-cache""",
    default="globi-taxon-cache",
)
@click.option(
    "-e",
    is_flag=True,
    help="""
            Activate echo -e option""",
)
@click.argument("query", required=True, default="")
def append(query, matcher, properties, output_format, e):
    """
        Append term match to row using id and name columns specified
        in input schema. Multiple matches result in multiple rows.

        :param query: [string]  Query. Default: <empty string>
        :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
        :param p: [string]  Path to properties file to override defaults. Default: None
        :param o: ["tsv", "json"]  Output format. Default: "tsv"

        Usage::

            pynomer append "\\tHomo sapiens"

            pynomer append "ITIS:180547\\t" -m globi-enrich
        """
    click.echo(
        pynomer.append(
            query, matcher, properties, output_format, echo_opt="-e" if e else ""
        )
    )


def main():
    cli()
