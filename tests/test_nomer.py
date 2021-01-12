from context import NomerClient
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def nomer_client():
    yield NomerClient(base_url="http://localhost:5000/")


# def test_version(nomer_client):
#     assert nomer_client.version() == "0.1.8"
#
#
# def test_clean(nomer_client):
#     assert nomer_client.clean() == None


def test_input_schema(nomer_client):
    assert (
        nomer_client.input_schema()
        == '[{"column":0,"type":"externalId"},{"column": 1,"type":"name"}]'
    )


def test_input_schema_with_file(nomer_client):
    assert (
        nomer_client.input_schema(p="./tests/properties.test")
        == '[{"column":0,"type":"name"},{"column": 1,"type":"externalId"}]'
    )


def test_output_schema(nomer_client):
    assert (
        nomer_client.output_schema()
        == '[{"column":0,"type":"externalId"},{"column": 1,"type":"name"}]'
    )


def test_output_schema_with_file(nomer_client):
    assert (
        nomer_client.output_schema(p="./tests/properties.test")
        == '[{"column":0,"type":"name"},{"column": 1,"type":"externalId"}]'
    )


def test_properties(nomer_client):
    assert (
        nomer_client.properties()[0:51]
        == "nomer.append.schema.output.example.taxon.rank.order"
    )


def test_matchers(nomer_client):
    assert nomer_client.matchers().split("\n")[0] == "ala-taxon"


def test_matchers_json(nomer_client):
    assert json.loads(nomer_client.matchers(o="json"))[0]["name"] == "nbn-taxon-id"


def test_replace_id(nomer_client):
    assert nomer_client.replace(id="EOL:327955").split("\t")[1] == "Homo sapiens"


def test_replace_name(nomer_client):
    assert nomer_client.replace(name="Homo sapiens").split("\t")[0] == "EOL:327955"


def test_append_id(nomer_client):
    assert nomer_client.append(id="EOL:327955").split("\t")[4] == "Homo sapiens"


def test_append_name(nomer_client):
    assert nomer_client.append(name="Homo sapiens").split("\t")[3] == "EOL:327955"


def test_append_wikidata_taxon_id_web(nomer_client):
    assert nomer_client.append(id="EOL:327955", matcher="wikidata-taxon-id-web") != None
