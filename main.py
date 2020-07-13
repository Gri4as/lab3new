import replacement_code, permutation_cipher, gamma_code


def gen_key():
    try:
        method = input('Выберите метод для генерации ключа:\n1)Замена\n2)Перестановка\n3)Гаммирование\n\n')
        if not method in ['1', '2', '3']:
            raise Exception('Неверный выбор метода')
        out = open(input('Введите название: ') + '.key', 'w+', encoding='utf-8')
        alp_path = input('Выберите путь до алфавита\n')
        try:
            alp_fle = open(alp_path, 'r', encoding='utf-8')
            alp = alp_fle.read()
            alp_fle.close()
        except:
            raise Exception('Ошибка чтения файла/отсутствие файла')
        if alp_path[len(alp_path) - 5:] != '.alph':
            raise Exception('Неверное расширение алфавита')
        if method == '1':
            dec = replacement_code.replacement(alp)
            out.write(dec.get_key())
        elif method == '2':
            dec = permutation_cipher.permutation(alp)
            out.write(dec.get_key())
        else:
            dec = gamma_code.gamma(alp)
            out.write(dec.get_key())
        out.close()
        print('Дело сделано\n')
    except Exception as e:
        print(e)


def chs_enc_meth():
    method = input('Выберите метод шифрования:\n1)Замена\n2)Перестановка\n3)Гаммирование\n\n')
    if not method in ['1', '2', '3']:
        print('Неверный вариант')
        return
    key_path = input('Выберите путь до файла ключа: ')
    if key_path[len(key_path) - 4:] != '.key':
        print('Неверный формат ключа')
        return
    txt_path = input('Выберите путь до файла текста: ')
    if txt_path[len(txt_path) - 4:] != '.txt':
        print('Неверный формат файла')
        return
    alp_path = input('Выберите путь до алфавита: ')
    if alp_path[len(alp_path)-5: ] != '.alph':
        print('Неверный формат алфавита')
        return
    try:
        key_fle = open(key_path, 'r', encoding='utf-8')
        txt_fle = open(txt_path, 'r', encoding='utf-8')
        alp_fle = open(alp_path, 'r', encoding='utf-8')
        key = key_fle.read()
        txt = txt_fle.read()
        alp = alp_fle.read()
        txt = ' '.join(txt.split('\n'))
        key_fle.close()
        txt_fle.close()
        alp_fle.close()
        out = open(input('Введите название: ') + '.encrypt', 'w+', encoding='utf-8')
        enc = None
        if method == '1':
            enc = replacement_code.replacement(alp)
        elif method == '2':
            enc = permutation_cipher.permutation(alp)
        elif method == '3':
            enc = gamma_code.gamma(alp)
        out.write(method + ':' + enc.encrypt(txt, key))
        out.close()
        print('Операция прошла успешно')
    except Exception as e:
        print(e)
        return


def dec_text():
    key_path = input('Выберите путь до файла ключа: ')
    if key_path[len(key_path) - 4:] != '.key':
        print('Неверный формат ключа')
        return
    txt_path = input('Выберете путь до зашифрованного текста: ')
    if txt_path[len(txt_path) - 8:] != '.encrypt':
        print('Неверный формат файла')
        return
    alp_path = input('Выберете файл алфавита: ')
    if alp_path[len(alp_path) - 5:] != '.alph':
        print('Неверный формат файла')
        return
    try:
        key_fle = open(key_path, 'r', encoding='utf-8')
        txt_fle = open(txt_path, 'r', encoding='utf-8')
        alp_fle = open(alp_path, 'r', encoding='utf-8')
        key = key_fle.read()
        alp = alp_fle.read()
        tmp = txt_fle.read().split(':')
        txt = tmp[1]
        method = tmp[0]
        key_fle.close()
        alp_fle.close()
        txt_fle.close()
        del tmp
        out = open(input('Введите название: ') + '.txt', 'w+', encoding='utf-8')
        dec = None
        if method == '1':
            dec = replacement_code.replacement(alp)
        elif method == '2':
            dec = permutation_cipher.permutation(alp)
        elif method == '3':
            dec = gamma_code.gamma(alp)
        else:
            print('Неверный формат шифра')
            return
        out.write(dec.decrypt(txt, key))
        out.close()
        print('Операция прошла успешно. Возвращение в меню...')
    except Exception as e:
        print(e)
        return


def cry_dec():
    print('1)Зашифровать\n2)Расшифровать\n')
    cod_or_dec = input()
    if cod_or_dec == '1':
        chs_enc_meth()
    elif cod_or_dec == '2':
        dec_text()
    else:
        return


def main_menu():
    print('Главное меню\n1)Зашифровать/расшифровать\n2)Сгенерировать ключ\n')
    choosen = input()
    if choosen == '1':
        cry_dec()
    elif choosen == '2':
        try:
            gen_key()
        except Exception as e:
            print(e)
    else:
        exit()


while True:
    main_menu()
