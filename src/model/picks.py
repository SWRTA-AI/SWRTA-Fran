
import numpy as np
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences

from ..client import tf_serving


class PickPredictorModel:

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def predict_next_picks_name(self, name_sequence, k=5):

        token_sequence = self.tokenizer.conv_name_to_token(name_sequence)
        picks, score = self.predict_next_picks_token(token_sequence, k)
        chosen_names = self.tokenizer.conv_token_to_name(picks)

        return chosen_names, score

    def predict_next_picks_id(self, id_sequence, k=5):

        token_sequence = self.tokenizer.conv_id_to_token(id_sequence)
        picks, score = self.predict_next_picks_token(token_sequence, k)
        chosen_ids = self.tokenizer.conv_token_to_id(picks)

        return chosen_ids, score

    def predict_next_picks_token(self, token_sequence, k=5):

        if len(token_sequence) < 1 or token_sequence[0] != 1:
            token_sequence.insert(0, 1)

        x_input = pad_sequences([token_sequence], maxlen=10, padding="post", value=0, dtype="int32")
        x_input = x_input.tolist()

        y_pred = tf_serving.predict_picks(x_input)[0][len(token_sequence) - 1]

        score, sampled_ids = tf.math.top_k(y_pred, k=k*2)
        sampled_ids = [x for x in sampled_ids.numpy() if x not in token_sequence]

        chosen_token = sampled_ids[:k]
        chosen_score = score[:k].numpy().tolist()

        return chosen_token, chosen_score

    def simulate_picks(self, name_sequence):

        result = []

        # Generate sequence
        for _ in range((10 - len(name_sequence))):
            next_pick = self.predict_next_picks_name(name_sequence, k=1)[0]
            name_sequence.append(next_pick)

        # Display flow section
        name_sequence.insert(0, '[START]')
        name_sequence.append('[END]')
        for x in range(0, len(name_sequence)-2, 2):
            p1 = name_sequence[x]
            p2 = name_sequence[x+1]
            p3 = name_sequence[x+2]
            p4 = name_sequence[x+3]
            result.append("{} {} => {} {}".format(p1, p2, p3, p4))

        # Display team
        team_1 = [name_sequence[i] for i in [1, 4, 5, 8, 9]]
        team_2 = [name_sequence[i] for i in [2, 3, 6, 7, 10]]
        result.append("\nteam 1 : {}\nteam 2 : {}".format(" ".join(team_1), " ".join(team_2)))

        return "\n".join(result)
