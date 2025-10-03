from .create_all_files import write_log
def caesar_ascii(start_string, bias):
    if not isinstance(bias, (int)):
        write_log("Шифр Цезаря (ASCII): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Ошибка: Введено недопустимое значение"
        bias = "-"
        result = "-"
    else:
        er_message = "Успешно"
        ascii_char = ""
        A = []
        B = []
        C = []
    
        for char in start_string:
            ascii_char = ord(char)
            A.append(ascii_char)
        #print("[ Значения символов по таблице ASCII           ]",A)

        for value in A:
            n = (value + bias)
            if n < 65 or n > 122:
                write_log("Шифр Цезаря (ASCII): ValueError", "Внимание: Выход за границы (Смещение < 65 либо > 122)")
                er_message = "Внимание: Выход за границы (Смещение <65 либо >122)"
                result = "-"
                return er_message, result
            else:
                B.append(n)
        #print("[ Смещенные значения символов по таблице ASCII ]",B)
    
        for c in B:
            c = chr(c)
            C.append(c)
        
        result = "".join(C)
    return er_message, result

#caesar_ascii("apple", -800)
def caesar_dictionary(text, shift):
    if not isinstance(shift, (int)):
        result = "-"
        write_log("Шифр Цезаря (Словарь): ValueError", "Ошибка: Введено не числовое значение")
        er_message = "Ошибка: Введено недопустимое значение"
        shift = "-"
    else:
        result = ""
        er_message = "Успешно"
        dc = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26,
            'А': 27,
            'Б': 28,
            'В': 29,
            'Г': 30,
            'Д': 31,
            'З': 32,
            'И': 33,
            'Й': 34,
            'К': 35,
            'Л': 36,
            'М': 37,
            'Н': 38,
            'О': 39,
            'П': 40,
            'Р': 41,
            'С': 42,
            'Т': 43,
            'У': 44,
            'Ф': 45,
            'Х': 46,
            'Ц': 47,
            'Ч': 48,
            'Ш': 49,
            'Щ': 50,
            'Ъ': 51,
            'Ы': 52,
            'Ь': 53,
            'Э': 54,
            'Ю': 55,
            'Я': 56,
            '1': 57,
            '2': 58,
            '3': 59,
            '4': 60,
            '5': 61,
            '6': 62,
            '7': 63,
            '8': 64,
            '9': 65,
            '0': 66,
            }
        num_to_char = {v: k for k, v in dc.items()}
    
        for char in text:
            if char.isalpha():
                is_lower = char.islower()
                base_char = char.upper()
                base_num = dc[base_char]
                shifted_num = (base_num + shift - 1) % 66 + 1
                shifted_char = num_to_char[shifted_num]
                result += shifted_char.lower() if is_lower else shifted_char
            else:
                result += char
    return er_message, result
