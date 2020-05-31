
import json
import requests
import numpy as np
from os import environ
from dotenv import load_dotenv
load_dotenv()


def predict_picks(inputs):

    r = requests.post(environ.get('TF_SERVING_URL') + "/predict_picks:predict", json={
        "inputs": inputs
    })

    output = json.loads(r.content.decode('utf-8'))
    return output["outputs"]


def predict_bans_01(input_team, input_opponent):

    r = requests.post(environ.get('TF_SERVING_URL') + "/predict_bans_01:predict", json={
        "inputs": {
            "input_team": input_team,
            "input_opponent": input_opponent
        }
    })

    output = json.loads(r.content.decode('utf-8'))
    return output["outputs"]


def predict_bans_02(input_team, input_opponent):

    r = requests.post(environ.get('TF_SERVING_URL') + "/predict_bans_02:predict", json={
        "inputs": {
            "input_team": input_team,
            "input_opponent": input_opponent
        }
    })

    output = json.loads(r.content.decode('utf-8'))
    return output["outputs"]
