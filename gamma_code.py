import parent_class as par
import random as r


class gamma(par.cipher):

    def get_key(self):
        try:
            len_key = int(input('Введите длину ключа: '))
        except:
            raise Exception('Ошибка вводных данных')
        if len_key < 2:
            raise Exception('Малая длина ключа')
        return ' '.join([str(r.randint(0, len(self._alp))) for _ in range(len_key)])

    def encrypt(self, not_enc_tex, key):
        if len(not_enc_tex) % len(key.split()) != 0:
            for _ in range(len(key.split()) - len(not_enc_tex) % len(key.split())):
                not_enc_tex += r.choice(self._alp)
        lst_str = self._splt(not_enc_tex, key) # делим строку на подстроки ключевой длины
        for i in range(len(lst_str)): # для каждого символа из длины строки
            tmp = ['' for _ in range(len(key.split()))] # пустой временный массив длины слова
            for j in range(len(lst_str[i])): # для каждого символа длины строки
                # каждый элемент во временном массиве вычисляется по свойству:
                # К индексу j буквы прибавляется j элемент ключа
                # от суммы берется остаток от деления на длину алфавита - это и есть индекс нового символа
                tmp[j] = self._alp[(self._alp.index(lst_str[i][j]) + int(key.split()[j])) % len(self._alp)]
            # временная переменная склеивается в i слово
            lst_str[i] = ''.join(tmp)
        # измененные подстроки склеиваются в текст-результат
        return ''.join(lst_str)

    def decrypt(self, enc_tex, key):
        if len(enc_tex) % len(key.split()) != 0:
            raise Exception('Неверный ключ!')
        lst_str = self._splt(enc_tex, key)
        for i in range(len(lst_str)):
            tmp = ['' for _ in range(len(key.split()))]
            for j in range(len(lst_str[i])):
                tmp[j] = self._alp[self._alp.index(lst_str[i][j]) - int(key.split()[j])]
            lst_str[i] = ''.join(tmp)
        return ''.join(lst_str)