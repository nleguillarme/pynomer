from .nomer_utils import *


def version():
    """
    Show Version.

    Usage::

        import pynomer as pn
        pn.version()
    """
    return run_nomer(get_nomer_simple_cmd())


def clean(p=None):
    """
    Cleans term matcher cache.

    :param p: [string]  Path to properties file to override defaults. Default: None

    Usage::

        import pynomer as pn
        pn.clean()
    """
    return run_nomer(get_nomer_simple_cmd(cmd="clean", properties=p))


def input_schema(p=None):
    """
    Show input schema in JSON.

    :param p: [string]  Path to properties file to override defaults. Default: None

    Usage::

        import pynomer as pn
        pn.input_schema()
    """
    return run_nomer(get_nomer_simple_cmd(cmd="input-schema", properties=p))


def output_schema(p=None):
    """
    Show output schema.

    :param p: [string]  Path to properties file to override defaults. Default: None

    Usage::

        import pynomer as pn
        pn.output_schema()
    """
    return run_nomer(get_nomer_simple_cmd(cmd="output-schema", properties=p))


def properties(p=None):
    """
    Lists configuration properties. Can be used to make a local copy and override
    default settings.

    :param p: [string]  Path to properties file to override defaults. Default: None

    Usage::

        import pynomer as pn
        pn.properties()
        new_properties = "./path/to/a/property_file"
        pn.properties(p=new_properties)
    """
    return run_nomer(get_nomer_simple_cmd(cmd="properties", properties=p))


def matchers(o="tsv", v=False):
    """
    Lists supported matcher and (optionally) their descriptions.

    :param o: ["tsv", "json"]  Output format. Default: "tsv"
    :param v: [bool]  If set, matcher descriptions are included for tsv. Default: False

    Usage::

        import pynomer as pn
        pn.matchers()
    """
    return run_nomer(get_nomer_simple_cmd(cmd="matchers", verbose=v, output_format=o))


def replace(id="", name="", matcher="globi-taxon-cache", p=None):
    """
    Replace exact term matches in row. The input schema is used
    to select the id and/or name to match to. The output schema is
    used to select the columns to write into.

    :param id: [string]  External id. Default: <empty string>
    :param name: [string]  Name. Default: <empty string>
    :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
    :param p: [string]  Path to properties file to override defaults. Default: None

    Usage::

        import pynomer as pn
        pn.replace(name="Homo sapiens")
        pn.replace(id="ITIS:180547", matcher="globi-enrich")
    """
    return run_nomer(
        get_nomer_match_cmd(
            cmd="replace", id=id, name=name, matcher=matcher, properties=p
        )
    )


def append(id="", name="", matcher="globi-taxon-cache", p=None, o="tsv"):
    """
    Append term match to row using id and name columns specified
    in input schema. Multiple matches result in multiple rows.

    :param id: [string]  External id. Default: <empty string>
    :param name: [string]  Name. Default: <empty string>
    :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
    :param p: [string]  Path to properties file to override defaults. Default: None
    :param o: ["tsv", "json"]  Output format. Default: "tsv"

    Usage::

        import pynomer as pn
        pn.append(name="Homo sapiens")
        pn.append(id="ITIS:180547", matcher="globi-enrich")
    """
    return run_nomer(
        get_nomer_match_cmd(
            cmd="append",
            id=id,
            name=name,
            matcher=matcher,
            properties=p,
            output_format=o,
        )
    )
