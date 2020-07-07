import parent_class as par
import random as r


class permutation(par.cipher):

    def get_key(self):
        try:
            key_len = int(input('Введите длину ключа: '))
        except:
            raise Exception('Ошибка вводного значения!')
        if key_len < 2:
            raise Exception('Малая длина ключа')
        key = [x for x in range(key_len)]
        r.shuffle(key)
        return ' '.join([str(x) for x in key])

    def encrypt(self, not_enc_tex, key):
        if len(not_enc_tex) % len(key.split()) != 0:
            for _ in range(len(key.split()) - len(not_enc_tex) % len(key.split())):
                not_enc_tex += r.choice(self._alp)
        lst_str = self._splt(not_enc_tex, key)
        for i in range(len(lst_str)):
            tmp = ['' for _ in range(len(key.split()))]
            for j in range(len(tmp)):
                tmp[int(key.split()[j])] = lst_str[i][j]
            lst_str[i] = ''.join(tmp)
        return ''.join(lst_str)

    def decrypt(self, enc_tex, key):
        if len(enc_tex) % len(key.split()) != 0:
            raise Exception('Неверный ключ!')
        lst_str = self._splt(enc_tex, key)
        for i in range(len(lst_str)):
            tmp = ['' for _ in range(len(key.split()))]
            for j in range(len(tmp)):
                tmp[j] = lst_str[i][int(key.split()[j])]
            lst_str[i] = ''.join(tmp)
        return ''.join(lst_str)
