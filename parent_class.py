from abc import ABC, abstractmethod


class cipher(ABC):

    def __init__(self, in_al):
        self._alp = in_al

    def _splt(self, inp_tex, key):
        res = []
        for i in range(0, len(inp_tex), len(key.split())):
            res.append(inp_tex[i:i + len(key.split())])
        return res

    @abstractmethod
    def encrypt(self, not_enc_tex, key):
        pass

    @abstractmethod
    def decrypt(self, enc_tex, key):
        pass

    @abstractmethod
    def get_key(self):
        pass