
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from ..client import tf_serving


class BanPredictorModel01:
    """
    First version of predict ban by using direct-ban trained model
    """

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.unique_ids = len(tokenizer.token_id_map)

    def predict_ban_score(self, own_team_token, opp_team_token):

        if len(own_team_token) != 5 or len(opp_team_token) != 5:
            raise Exception("Incomplete team")

        own_team = to_categorical(own_team_token, self.unique_ids)
        own_team = np.sum(own_team, axis=0)
        own_team = np.expand_dims(own_team, axis=0)
        own_team = own_team.tolist()

        opp_team = to_categorical(opp_team_token, self.unique_ids)
        opp_team = np.sum(opp_team, axis=0)
        opp_team = np.expand_dims(opp_team, axis=0)
        opp_team = opp_team.tolist()

        y_pred = tf_serving.predict_bans_01(own_team, opp_team)[0]
        score = np.array([y_pred[i] for i in opp_team_token])
        score = score / score.sum(axis=0)
        score = score.tolist()

        return score

    def predict_banned_token(self, own_team_token, opp_team_token):

        score = self.predict_ban_score(own_team_token, opp_team_token)
        result = [(opp_team_token[i], score[i]) for i in range(5)]

        return result

    def predict_banned_name(self, own_team_name, opp_team_name):

        own_team_token = self.tokenizer.conv_name_to_token(own_team_name)
        opp_team_token = self.tokenizer.conv_name_to_token(opp_team_name)

        score = self.predict_ban_score(own_team_token, opp_team_token)
        result = [(opp_team_name[i], score[i]) for i in range(5)]

        return result

    def predict_banned_id(self, own_team_id, opp_team_id):

        own_team_token = self.tokenizer.conv_id_to_token(own_team_id)
        opp_team_token = self.tokenizer.conv_id_to_token(opp_team_id)

        score = self.predict_ban_score(own_team_token, opp_team_token)
        result = [(opp_team_id[i], score[i]) for i in range(5)]

        return result

