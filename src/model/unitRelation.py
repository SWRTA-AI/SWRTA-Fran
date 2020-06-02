
import numpy as np


class UnitRelationPredictor:

    THRESHOLD = 150

    def __init__(self, tokenizer, pick_matrix, pick_count, log_pick_count):
        self.tokenizer = tokenizer
        self.pick_matrix = pick_matrix
        self.pick_count = pick_count
        self.log_pick_count = log_pick_count

    def predict_token(self, unit_token, k=5):

        if self.pick_count[unit_token] < self.THRESHOLD:
            return []

        score = -(self.pick_matrix[unit_token] * self.log_pick_count)[0]
        index = np.argpartition(score, k)[:k].tolist()
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
