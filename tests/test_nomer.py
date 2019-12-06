import pynomer as pn
import json


def test_version():
    assert pn.version() == "0.1.8"


def test_clean():
    assert pn.clean() == None


def test_input_schema():
    assert (
        pn.input_schema()
        == '[{"column":0,"type":"externalId"},{"column": 1,"type":"name"}]'
    )


def test_output_schema():
    assert (
        pn.output_schema()
        == '[{"column":0,"type":"externalId"},{"column": 1,"type":"name"}]'
    )


def test_properties():
    assert (
        pn.properties()[0:51] == "nomer.append.schema.output.example.taxon.rank.order"
    )


def test_matchers():
    assert pn.matchers().split("\n")[0] == "ala-taxon"


def test_matchers_json():
    assert json.loads(pn.matchers(o="json"))[0]["name"] == "nbn-taxon-id"


def test_replace_id():
    assert pn.replace(id="EOL:327955").split("\t")[1] == "Homo sapiens"


def test_replace_name():
    assert pn.replace(name="Homo sapiens").split("\t")[0] == "EOL:327955"


def test_append_id():
    assert pn.append(id="EOL:327955").split("\t")[4] == "Homo sapiens"


def test_append_name():
    assert pn.append(name="Homo sapiens").split("\t")[3] == "EOL:327955"
