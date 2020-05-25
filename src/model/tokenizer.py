
import numpy as np
import pickle

token_id_mons_id_mapping = {}
mons_id_token_id_mapping = {}
monster_name_id_mapping = {}
monster_id_name_mapping = {}


class Tokenizer:

    def __init__(self):
        self.token_id_map = token_id_mons_id_mapping
        self.id_token_map = mons_id_token_id_mapping
        self.name_id_map = monster_name_id_mapping
        self.id_name_map = monster_id_name_mapping
        self.validity_check()

    def validity_check(self):
        if self.token_id_map is None:
            raise Exception("unknown token_id_map")
        if self.id_token_map is None:
            raise Exception("unknown id_token_map")
        if self.name_id_map is None:
            raise Exception("unknown name_id_map")
        if self.id_name_map is None:
            raise Exception("unknown id_name_map")

    def conv_token_to_id(self, tokens):
        return [self.token_id_map[x] if x in self.token_id_map else 0 for x in tokens]

    def conv_token_to_name(self, tokens):
        ids = self.conv_token_to_id(tokens)
        return self.conv_id_to_name(ids)

    def conv_id_to_token(self, mons_ids):
        return [self.id_token_map[x] if x in self.id_token_map else 0 for x in mons_ids]

    def conv_id_to_name(self, mons_ids):
        return [self.id_name_map[x] if x in self.id_name_map else '' for x in mons_ids]

    def conv_name_to_token(self, names):
        ids = self.conv_name_to_id(names)
        return self.conv_id_to_token(ids)

    def conv_name_to_id(self, names):
        return [self.name_id_map[x] if x in self.name_id_map else 0 for x in names]
