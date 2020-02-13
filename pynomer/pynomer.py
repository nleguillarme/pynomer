import urllib
import requests
import json


class NoResultException(Exception):
    pass


class NomerClient:
    def __init__(self, base_url):
        """
        Usage::

            from pynomer import NomerClient

            client = NomerClient(base_url="http://localhost:5000/")
        """
        self.base_url = base_url

    def version(self):
        """
        Show Version.

        Usage::

            client.version()
        """
        res = self.run_nomer(nomer_cmd="version")
        return res["result"]

    def clean(self, p=None):
        """
        Cleans term matcher cache.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            client.clean()
        """
        res = self.run_nomer(nomer_cmd="clean", p=self.get_properties(p))
        return res["result"]

    def input_schema(self, p=None):
        """
        Show input schema in JSON.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            client.input_schema()
            p = "./new_properties.txt"
            client.input_schema(p=p)
        """
        res = self.run_nomer(nomer_cmd="input_schema", p=self.get_properties(p))
        return res["result"]

    def output_schema(self, p=None):
        """
        Show output schema.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            client.output_schema()
            p = "./new_properties.txt"
            client.output_schema(p=p)
        """
        res = self.run_nomer(nomer_cmd="output_schema", p=self.get_properties(p))
        return res["result"]

    def properties(self, p=None):
        """
        Lists configuration properties. Can be used to make a local copy and override
        default settings.

        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            pn.properties()
            p = "./new_properties.txt"
            client.properties(p=p)
        """
        res = self.run_nomer(nomer_cmd="properties", p=self.get_properties(p))
        return res["result"]

    def matchers(self, o="tsv", v=False):
        """
        Lists supported matcher and (optionally) their descriptions.

        :param o: ["tsv", "json"]  Output format. Default: "tsv"
        :param v: [bool]  If set, matcher descriptions are included for tsv. Default: False

        Usage::

            client.matchers()
        """
        res = self.run_nomer(nomer_cmd="matchers", v=v, o=o)
        return res["result"]

    def replace(self, id="", name="", matcher="globi-taxon-cache", p=None):
        """
        Replace exact term matches in row. The input schema is used
        to select the id and/or name to match to. The output schema is
        used to select the columns to write into.

        :param id: [string]  External id. Default: <empty string>
        :param name: [string]  Name. Default: <empty string>
        :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
        :param p: [string]  Path to properties file to override defaults. Default: None

        Usage::

            client.replace(name="Homo sapiens")
            client.replace(id="ITIS:180547", matcher="globi-enrich")
        """
        res = self.run_nomer(
            nomer_cmd="replace",
            id=id,
            name=name,
            matcher=matcher,
            p=self.get_properties(p),
        )
        return res["result"]

    def append(self, id="", name="", matcher="globi-taxon-cache", p=None, o="tsv"):
        """
        Append term match to row using id and name columns specified
        in input schema. Multiple matches result in multiple rows.

        :param id: [string]  External id. Default: <empty string>
        :param name: [string]  Name. Default: <empty string>
        :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
        :param p: [string]  Path to properties file to override defaults. Default: None
        :param o: ["tsv", "json"]  Output format. Default: "tsv"

        Usage::

            client.append(name="Homo sapiens")
            client.append(id="ITIS:180547", matcher="globi-enrich")
        """
        res = self.run_nomer(
            nomer_cmd="append",
            id=id,
            name=name,
            matcher=matcher,
            p=self.get_properties(p),
            o=o,
        )
        return res["result"]

    def get_properties(self, p):
        if p != None:
            with open(p, "r") as file:
                properties = file.read()
                return properties
        else:
            return p

    def run_nomer(self, nomer_cmd="version", **kwargs):
        url = "{}{}?{}".format(self.base_url, nomer_cmd, urllib.parse.urlencode(kwargs))
        resp = requests.get(url)
        resp.raise_for_status()
        self.check_ctype(resp.headers["Content-Type"])
        return resp.json()

    def check_ctype(self, x, ctype="application/json"):
        if x != ctype:
            raise NoResultException("Content-Type do not equal " + ctype)
