
class OutputFormatter:

    def __init__(self, bestiary):
        self.bestiary = bestiary

    def format_pick_id(self, pred_ids, scores):

        result = []
        for i in range(len(pred_ids)):
            info = self.bestiary.get_info(pred_ids[i])
            info["score"] = scores[i]
            result.append(info)

        return result

    def format_pick_name(self, pred_names, scores):

        result = []
        for i in range(len(pred_names)):
            unit_id = self.bestiary.get_id(pred_names[i])
            info = self.bestiary.get_info(unit_id)
            info["score"] = scores[i]
            result.append(info)

        return result
