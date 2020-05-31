
import json
from os import environ
from dotenv import load_dotenv
load_dotenv()


class Bestiary:

    def __init__(self, path):

        self.bestiary = None

        self.unit_names = []
        self.name_id_mapping = {}
        self.units = {}

        self._load_main_json(path)
        self._parse_bestiary()

    def _load_main_json(self, path):
        with open(path) as f:
            self.bestiary = json.load(f)

    def _parse_bestiary(self):

        for unit in self.bestiary:

            # add link prefix
            unit["image_filename"] = "{}/static/herders/images/monsters/{}".format(environ.get('SWARMFARM_URL'), unit["image_filename"])

            unit_id = unit["com2us_id"]
            unit_name = unit["name"].lower()

            # skip unawakened unit
            if unit_id // 10 % 10 == 0:
                continue

            self.name_id_mapping[unit_name] = unit_id
            self.units[unit_id] = unit

        self.unit_names = sorted(self.name_id_mapping.keys())

    def get_info(self, unit_id):
        return self.units[unit_id]

    def get_id(self, unit_name):
        return self.name_id_mapping[unit_name.lower()]

    def search_name(self, query):
        found_names = filter(lambda x: query in x, self.unit_names)
        search_result = list(map(lambda x: self.get_info(self.name_id_mapping[x]), found_names))
        return search_result


if __name__ == "__main__":

    best = Bestiary("../../resource/bestiary.json")
    result = best.search_name("bast")
    print(result)
