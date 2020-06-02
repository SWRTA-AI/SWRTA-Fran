
import pickle
import numpy as np

from src.model.picks import PickPredictorModel
from src.model.bans_01 import BanPredictorModel01
from src.model.bans_02 import BanPredictorModel02
from src.model.unitRelation import UnitRelationPredictor
from src.util.bestiary import Bestiary
from src.util.output_formatter import OutputFormatter

tokenizer = pickle.load(open("pickle/tokenizer.pkl", "rb"))
model_pick = PickPredictorModel(tokenizer)
model_ban_01 = BanPredictorModel01(tokenizer)
model_ban_02 = BanPredictorModel02(tokenizer)
bestiary = Bestiary("resource/bestiary.json")
output_formatter = OutputFormatter(bestiary)

pick_together_matrix = np.load("pickle/pick_matrix.npy")
counter_pick_matrix = np.load("pickle/counterpick_matrix.npy")
log_pick_count = np.load("pickle/log_pick_count.npy")
pick_count = np.load("pickle/pick_count.npy")

model_friend = UnitRelationPredictor(
    tokenizer=tokenizer,
    pick_matrix=pick_together_matrix,
    pick_count=pick_count,
    log_pick_count=log_pick_count
)

model_counterpick = UnitRelationPredictor(
    tokenizer=tokenizer,
    pick_matrix=counter_pick_matrix,
    pick_count=pick_count,
    log_pick_count=log_pick_count
)
