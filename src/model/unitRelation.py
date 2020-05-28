
import numpy as np
import tensorflow as tf


class UnitRelationPredictor:

    def __init__(self, tokenizer, pick_matrix, log_pick_count):
        self.tokenizer = tokenizer
        self.pick_matrix = pick_matrix
        self.log_pick_count = log_pick_count

    def predict_token(self, unit_token, k=5):
        _, index = tf.math.top_k((self.pick_matrix[unit_token] * self.log_pick_count), k)
        index = index[0].numpy().tolist()
        return index

    def predict_name(self, unit_name, k=5):

        unit_token = self.tokenizer.conv_name_to_token([unit_name])
        tokens = self.predict_token(unit_token, k)
        names = self.tokenizer.conv_token_to_name(tokens)

        return names

    def predict_id(self, unit_id, k=5):

        unit_token = self.tokenizer.conv_id_to_token([unit_id])
        tokens = self.predict_token(unit_token, k)
        ids = self.tokenizer.conv_token_to_id(tokens)

        return ids
