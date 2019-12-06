import logging
import subprocess
import json
import sys

# replace, append
def get_nomer_match_cmd(
    id="",
    name="",
    cmd="append",
    matcher="globi-taxon-cache",
    properties=None,
    output_format=None,
):
    if id == "" and name == "":
        raise ValueError("Id and name cannot be empty strings")
    query = r"'{}\t{}'".format(id, name)
    cmd = " ".join(["echo -e", query, "|", "nomer", cmd, matcher])
    if properties:
        cmd = " ".join([cmd, "-p", properties])
    if output_format:
        cmd = " ".join([cmd, "-o", output_format])
    return cmd


def get_nomer_simple_cmd(
    cmd="version", verbose=None, properties=None, output_format=None
):
    cmd = " ".join(["nomer", cmd])
    if properties:
        cmd = " ".join([cmd, "-p", properties])
    if output_format:
        cmd = " ".join([cmd, "-o", output_format])
    if verbose:
        cmd = " ".join([cmd, "-v", verbose])
    return cmd


def get_docker_cmd(nomer_cmd):
    return "docker run --rm nomer-docker {}".format(nomer_cmd)


def run_nomer(nomer_cmd):
    docker_cmd = get_docker_cmd(nomer_cmd)
    p = subprocess.Popen(
        docker_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True
    )
    result = p.communicate()[0].decode("utf8")
    if result:
        return result.strip("\n")
    return None
