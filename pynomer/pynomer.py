from .nomer_utils import *
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


class NoResultException(Exception):
    pass


def version():
    """
        Show Version.

        Usage::

            version()
        """
    _, res = run_nomer(nomer_cmd=get_nomer_simple_cmd())
    return res


def clean(properties=None):
    """
        Cleans term matcher cache.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            clean()
        """
    _, res = run_nomer(
        nomer_cmd=get_nomer_simple_cmd(
            cmd="clean", properties=get_properties(properties)
        )
    )
    return res


def input_schema(properties=None):
    """
        Show input schema in JSON.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            input_schema()
            input_schema("./new_properties.txt")
        """
    _, res = run_nomer(
        nomer_cmd=get_nomer_simple_cmd(
            cmd="input-schema", properties=get_properties(properties)
        )
    )
    return res


def output_schema(properties=None):
    """
        Show output schema.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            output_schema()
            output_schema("./new_properties.txt")
        """
    _, res = run_nomer(
        nomer_cmd=get_nomer_simple_cmd(
            cmd="output-schema", properties=get_properties(properties)
        )
    )
    return res


def properties(properties=None):
    """
        Lists configuration properties. Can be used to make a local copy and override
        default settings.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            properties()
            properties("./new_properties.txt")
        """
    _, res = run_nomer(
        nomer_cmd=get_nomer_simple_cmd(
            cmd="properties", properties=get_properties(properties)
        )
    )
    return res


def matchers(output_format="tsv", verbose=False):
    """
        Lists supported matcher and (optionally) their descriptions.

        :param o: ["tsv", "json"]  Output format. Default: "tsv"
        :param v: [bool]  If set, matcher descriptions are included for tsv. Default: False

        Usage::

            matchers()
        """
    _, res = run_nomer(
        nomer_cmd=get_nomer_simple_cmd(
            cmd="matchers", verbose=verbose, output_format=output_format
        )
    )
    return res


def validate_term(filepath="", properties=None):
    """
        Validate terms.

        :param filepath: [string]  Path or URL to TaxonCache file. Default: <empty string>
        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            validate_term("https://zenodo.org/record/1213465/files/taxonCacheFirst10.tsv")
        """
    _, res = run_nomer(
        nomer_cmd=get_nomer_validate_cmd(
            cmd="validate-term",
            filepath=filepath,
            properties=get_properties(properties),
        )
    )
    return res


def validate_term_link(filepath="", properties=None):
    """
        Validate term links.

        :param filepath: [string]  Path or URL to TaxonMap file. Default: <empty string>
        :param p: [string]  Path to properties file to override defaults. Default: None

        """
    _, res = run_nomer(
        nomer_cmd=get_nomer_validate_cmd(
            cmd="validate-term-link",
            filepath=filepath,
            properties=get_properties(properties),
        )
    )
    return res


def replace(query="", matcher="globi-taxon-cache", properties=None, echo_opt=""):
    """
        Replace exact term matches in row. The input schema is used
        to select the id and/or name to match to. The output schema is
        used to select the columns to write into.

        :param query: [string]  Query. Default: <empty string>
        :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            replace(query="\tHomo sapiens")
            replace(query="ITIS:180547\t", matcher="globi-enrich")
        """
    _, res = run_nomer(
        get_nomer_match_cmd(
            cmd="replace",
            query=query,
            matcher=matcher,
            properties=get_properties(properties),
            echo_opt=echo_opt,
        )
    )
    return res


def append(
    query="",
    matcher="globi-taxon-cache",
    properties=None,
    output_format="tsv",
    echo_opt="",
):
    """
        Append term match to row using id and name columns specified
        in input schema. Multiple matches result in multiple rows.

        :param query: [string]  Query. Default: <empty string>
        :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
        :param p: [string]  Path to properties file to override defaults. Default: None
        :param o: ["tsv", "json"]  Output format. Default: "tsv"

        Usage::

            append(query="\tHomo sapiens")
            append(query="ITIS:180547\t", matcher="globi-enrich")
        """
    _, res = run_nomer(
        get_nomer_match_cmd(
            cmd="append",
            query=query,
            matcher=matcher,
            properties=get_properties(properties),
            output_format=output_format,
            echo_opt=echo_opt,
        )
    )
    return res


def get_properties(p):
    if p:
        with open(p, "r") as file:
            properties = file.read()
            return properties
    else:
        return p
