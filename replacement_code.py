import parent_class as par
import random as r


class replacement(par.cipher):

    def get_key(self):
        alp = list(self._alp)
        r.shuffle(alp)
        return ''.join(alp)


    def encrypt(self, not_enc_tex, key):
        for probeg in self._alp:
            if probeg not in key:
                raise Exception('Ключ неверен')
        if not len(key) == len(self._alp):
            raise Exception('Неверный ключ!')
        enc_tex = ''
        for x in not_enc_tex:
            enc_tex += key[self._alp.index(x)]
        return enc_tex


    def decrypt(self, enc_tex, key):

        for probeg in self._alp:
            if probeg not in key:
                raise Exception('Ключ неверен')
        if not len(key) == len(self._alp):
            raise Exception('Неверный ключ!')
        dec_tex = ''
        for x in enc_tex:
            dec_tex += self._alp[key.index(x)]
        return dec_tex