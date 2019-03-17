class Token:
    def __init__(self, token_in_dict):
        self.morph = token_in_dict.get('morph')
        self.pos = token_in_dict.get('pos')
        self.begin_index = token_in_dict.get('beginIndex')
        self.end_index = token_in_dict.get('endIndex')

    def get_morph(self):
        return self.morph

    def get_pos(self):
        return self.pos

    def get_begin_index(self):
        return self.begin_index

    def get_end_index(self):
        return self.end_index

    def __str__(self):
        return "{}/{}".format(self.morph, self.pos)

    def __repr__(self):
        return self.__str__()


class Pair:
    def __init__(self, pair_in_dict):
        self.first = pair_in_dict.get('first')
        self.second = pair_in_dict.get('second')

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def __str__(self):
        return "{}/{}".format(self.first, self.second)

    def __repr__(self):
        return self.__str__()
