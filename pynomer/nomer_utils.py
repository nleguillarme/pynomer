import logging
import subprocess
import json
import sys

logger = logging.getLogger(__name__)


class NomerException(Exception):
    pass


# validate-term, validate-term-link
def get_nomer_validate_cmd(filepath="", cmd="validate-term", properties=None):
    if filepath == "":
        raise ValueError("Filepath cannot be empty strings")
    nomer_cmd = "curl -L {} | nomer {}".format(filepath, cmd)
    if properties:
        nomer_cmd = "{} -p {}".format(nomer_cmd, properties)
    return nomer_cmd


# replace, append
def get_nomer_match_cmd(
    query="",
    cmd="append",
    matcher="globi-taxon-cache",
    properties=None,
    output_format=None,
    echo_opt="",
):
    # if id == "" and name == "":
    #     raise ValueError("Id and name cannot be empty strings")
    # query = r"'{}'".format(query)
    nomer_cmd = "echo {} '{}' | nomer {} {} -Xmx4096m -Xms1024m".format(
        echo_opt, query, cmd, matcher
    )
    if properties:
        nomer_cmd = "{} -p {}".format(nomer_cmd, properties)
    if output_format:
        nomer_cmd = "{} -o {}".format(nomer_cmd, output_format)
    return nomer_cmd


def get_nomer_simple_cmd(
    cmd="version", verbose=False, properties=None, output_format=None
):
    nomer_cmd = "nomer {}".format(cmd)
    if properties:
        nomer_cmd = "{} -p {}".format(nomer_cmd, properties)
    if output_format:
        nomer_cmd = "{} -o {}".format(nomer_cmd, output_format)
    if verbose:
        nomer_cmd = "{} -v".format(nomer_cmd)
    return nomer_cmd


def run_nomer(nomer_cmd):
    logger.debug("Run nomer command {}".format(nomer_cmd))
    p = subprocess.Popen(
        nomer_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
    )
    result = p.communicate()[0].decode("utf8")
    rc = p.returncode
    if rc:
        raise NomerException(
            "Command {} got return code {}. This is probably due to nomer throwing an exception.".format(
                nomer_cmd, rc
            )
        )
    logger.debug(
        "Command {} got return code {} and result {}".format(nomer_cmd, rc, result)
    )
    if result:
        return nomer_cmd, result.strip("\n")
    return nomer_cmd, None
