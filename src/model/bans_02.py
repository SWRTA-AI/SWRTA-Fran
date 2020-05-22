
import numpy as np
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from ..client import tf_serving


class BanPredictorModel02:
    """
    Second version of predict ban by using opponent-winning-chance score
    """

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.unique_ids = len(tokenizer.token_id_map)

    def predict_ban_score(self, own_team_token, opp_team_token):

        own_team_onehot = to_categorical([own_team_token], self.unique_ids)
        own_team_onehot = np.sum(own_team_onehot, axis=1)
        own_team_onehot = np.tile(own_team_onehot, [5, 1])
        own_team_onehot = own_team_onehot.tolist()

        opp_team_onehot = to_categorical([opp_team_token], self.unique_ids)
        opp_team_onehot = np.sum(opp_team_onehot, axis=1)
        opp_team_onehot = np.tile(opp_team_onehot, [5, 1])
        opp_team_onehot = opp_team_onehot.tolist()

        for i in range(5):
            opp_team_onehot[i][opp_team_token[i]] = 0

        score = tf_serving.predict_bans_02(own_team_onehot, opp_team_onehot)
        score = (1 - np.array(score).flatten())
        score = score / score.sum()
        score = score.tolist()

        return score

    def predict_banned_name(self, own_team_name, opp_team_name):

        own_team_token = self.tokenizer.conv_name_to_token(own_team_name)
        opp_team_token = self.tokenizer.conv_name_to_token(opp_team_name)

        score = self.predict_ban_score(own_team_token, opp_team_token)
        result = [(opp_team_name[i], score[i]) for i in range(5)]

        return result

    def predict_banned_token(self, own_team_token, opp_team_token):

        score = self.predict_ban_score(own_team_token, opp_team_token)
        result = [(opp_team_token[i], score[i]) for i in range(5)]

        return result

    def predict_banned_id(self, own_team_id, opp_team_id):

        own_team_token = self.tokenizer.conv_id_to_token(own_team_id)
        opp_team_token = self.tokenizer.conv_id_to_token(opp_team_id)

        score = self.predict_ban_score(own_team_token, opp_team_token)
        result = [(opp_team_id[i], score[i]) for i in range(5)]

        return result
