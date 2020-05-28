
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

    def format_ban_id(self, pred):

        result = []
        for unit_id, score in pred:
            info = self.bestiary.get_info(unit_id)
            info["score"] = score
            result.append(info)

        return result

    def format_ban_name(self, pred):

        result = []
        for unit_name, score in pred:
            unit_id = self.bestiary.get_id(unit_name)
            info = self.bestiary.get_info(unit_id)
            info["score"] = score
            result.append(info)

        return result

    def format_relation_id(self, pred):
        return [self.bestiary.get_info(x) for x in pred]
