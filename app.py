
from flask import Flask, request, jsonify, abort
from flask_cors import CORS

from src.client import tf_serving
from src.model.tokenizer import Tokenizer
from loader import model_pick, model_ban_01, model_ban_02, bestiary, output_formatter, model_friend, model_counterpick

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def test():

    if request.method == 'GET':
        return request.args
    elif request.method == 'POST':
        return request.get_json()
    else:
        return "OK"


@app.route('/api/predictor/pick/', methods=['POST'])
def predict_pick():

    input_json = request.get_json()

    if input_json["type"] == "id":
        preds, scores = model_pick.predict_next_picks_id(input_json["input"], k=input_json["k"])
        result = output_formatter.format_pick_id(preds, scores)

    elif input_json["type"] == "name":
        preds, scores = model_pick.predict_next_picks_name(input_json["input"], k=input_json["k"])
        result = output_formatter.format_pick_name(preds, scores)

    else:
        abort(400)

    return {"result": result}


@app.route('/api/predictor/pick/simulate', methods=['GET', 'POST'])
def simulate_pick():
    pred = model_pick.simulate_picks([])
    return {"result": pred}


@app.route('/api/predictor/ban/v1/', methods=['POST'])
def predict_ban_01():

    input_json = request.get_json()

    if input_json["type"] == "id":
        pred = model_ban_01.predict_banned_id(input_json["team"], input_json["opponent"])
        result = output_formatter.format_ban_id(pred)

    elif input_json["type"] == "name":
        pred = model_ban_01.predict_banned_name(input_json["team"], input_json["opponent"])
        result = output_formatter.format_ban_name(pred)

    else:
        abort(400)

    return {"result": result}


@app.route('/api/predictor/ban/v2/', methods=['POST'])
def predict_ban_02():

    input_json = request.get_json()

    if input_json["type"] == "id":
        pred = model_ban_02.predict_banned_id(input_json["team"], input_json["opponent"])
        result = output_formatter.format_ban_id(pred)

    elif input_json["type"] == "name":
        pred = model_ban_02.predict_banned_name(input_json["team"], input_json["opponent"])
        result = output_formatter.format_ban_name(pred)

    else:
        abort(400)

    return {"result": result}


@app.route('/api/predictor/friend/<unit_id>', methods=['GET'])
def predict_friend(unit_id):

    if unit_id is not None:
        pred = model_friend.predict_id(int(unit_id))
        result = output_formatter.format_relation_id(pred)
        return {"result": result}

    else:
        abort(400)


@app.route('/api/predictor/counterpick/<unit_id>', methods=['GET'])
def predict_counterpick(unit_id):

    if unit_id is not None:
        pred = model_counterpick.predict_id(int(unit_id))
        result = output_formatter.format_relation_id(pred)
        return {"result": result}

    else:
        abort(400)


@app.route('/api/search', methods=['GET', 'POST'])
def search_name():

    if request.method == 'GET':
        return search_name_GET(request)
    elif request.method == 'POST':
        return search_name_POST(request)
    else:
        abort(400)


def search_name_GET(request):
    query = request.args.get('query')
    result = bestiary.search_name(query)
    return {"result": result}


def search_name_POST(request):
    input_json = request.get_json()
    query = input_json["query"]
    result = bestiary.search_name(query)
    return {"result": result}


if __name__ == "__main__":
    app.run()
