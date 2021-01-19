from flask import Flask, jsonify, make_response, url_for, request
import pynomer
from datetime import datetime
import logging
import sys
import os

app = Flask(__name__)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)


# @app.before_first_request
# def load_cache():
#     app.logger.info("Clean taxon cache")
#     run_nomer(nomer_cmd=get_nomer_simple_cmd(cmd="clean"))
#     app.logger.info("Load taxon cache")
#     run_nomer(get_nomer_match_cmd(cmd="append", id="GBIF:1"))
#     app.logger.info("Ready to start server")


@app.route("/")
def index():
    return """
      <h1>Nomer in Docker!</h1>
      <p>A web-app for running Nomer inside Docker.</p>
      """


@app.route("/version", methods=["GET"])
def version():
    """
    Show Version.
    """
    cmd, result = pynomer.version()
    return get_response(cmd, result)


@app.route("/clean", methods=["GET"])
def clean():
    """
    Cleans term matcher cache.
    :param p: [string]  Path to properties file to override defaults. Default: None
    """
    p = request.args.get("p", "None")
    p = get_properties(p)

    cmd, result = pynomer.clean(properties=p)
    return get_response(cmd, result)


@app.route("/matchers", methods=["GET"])
def matchers():
    """
    Lists supported matcher and (optionally) their descriptions.
    :param o: ["tsv", "json"]  Output format. Default: "tsv"
    :param v: [bool]  If set, matcher descriptions are included for tsv. Default: False
    """
    o = request.args.get("o", "tsv")
    v = request.args.get("v", "")

    cmd, result = pynomer.matchers(output_format=o, verbose=v)
    return get_response(cmd, result)


@app.route("/replace", methods=["GET"])
def replace():
    """
    Replace exact term matches in row. The input schema is used
    to select the id and/or name to match to. The output schema is
    used to select the columns to write into.
    :param query: [string]  Query. Default: <empty string>
    :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
    :param p: [string]  Path to properties file to override defaults. Default: None
    """

    query = request.args.get("query", "")
    matcher = request.args.get("matcher", "globi-taxon-cache")
    p = request.args.get("p", "None")
    p = get_properties(p)
    e = False

    cmd, result = pynomer.replace(
        query=query, matcher=matcher, properties=p, echo_opt="-e" if e else ""
    )
    return get_response(cmd, result)


@app.route("/append", methods=["GET"])
def append():
    """
    Append term match to row using id and name columns specified
    in input schema. Multiple matches result in multiple rows.
    :param query: [string]  Query. Default: <empty string>
    :param matcher: [string]  Selected matcher. Default: "globi-taxon-cache"
    :param p: [string]  Path to properties file to override defaults. Default: None
    :param o: ["tsv", "json"]  Output format. Default: "tsv"
    """
    query = request.args.get("query", "")
    matcher = request.args.get("matcher", "globi-taxon-cache")
    p = request.args.get("p", "None")
    p = get_properties(p)
    o = request.args.get("o", "tsv")
    e = False

    cmd, result = pynomer.append(
        query=query,
        matcher=matcher,
        properties=p,
        output_format=o,
        echo_opt="-e" if e else "",
    )
    return get_response(cmd, result)


@app.route("/input_schema", methods=["GET"])
def input_schema():
    """
    Show input schema in JSON.
    :param p: [string]  Path to properties file to override defaults. Default: None
    """
    p = request.args.get("p", "None")
    p = get_properties(p)

    cmd, result = pynomer.input_schema(properties=p)
    return get_response(cmd, result)


@app.route("/output_schema", methods=["GET"])
def output_schema():
    """
    Show output schema.
    :param p: [string]  Path to properties file to override defaults. Default: None
    """
    p = request.args.get("p", "None")
    p = get_properties(p)

    cmd, result = pynomer.output_schema(properties=p)
    return get_response(cmd, result)


@app.route("/properties", methods=["GET"])
def properties():
    """
    Lists configuration properties. Can be used to make a local copy and override
    default settings.
    :param p: [string]  Path to properties file to override defaults. Default: None
    """
    p = request.args.get("p", "None")
    p = get_properties(p)

    cmd, result = pynomer.properties(properties=p)
    return get_response(cmd, result)


@app.route("/validate_term", methods=["GET"])
def validate_term():
    """
    Validate terms.
    :param p: [string]  Path to properties file to override defaults. Default: None
    """
    filepath = request.args.get("filepath", "")
    p = request.args.get("p", "None")
    p = get_properties(p)

    cmd, result = pynomer.validate_term(filepath, properties=p)
    return get_response(cmd, result)


@app.route("/validate_term_link", methods=["GET"])
def validate_term_link():
    """
    Validate term links.
    :param p: [string]  Path to properties file to override defaults. Default: None
    """
    filepath = request.args.get("filepath", "")
    p = request.args.get("p", "None")
    p = get_properties(p)

    cmd, result = pynomer.validate_term_link(filepath, properties=p)
    return get_response(cmd, result)


def get_response(cmd, cmd_result):
    headers = {}
    return make_response(
        jsonify(
            {
                "command": cmd,
                "result": cmd_result,
                "tstamp": datetime.utcnow().timestamp(),
                "endpoints": {"url_index": url_for("index", _external=True)},
            }
        ),
        200,
        headers,
    )


def get_properties(p):
    p = p if p != "None" else None
    if p:
        path = os.path.join(os.getcwd(), "input_properties")
        with open(path, "w") as f:
            app.logger.debug(f"Create new file {path} with content {p}")
            f.write(p)
        return path
    return p


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="9090")
