from .create_all_files import write_log
def caesar_ascii(start_string, bias):
    if not isinstance(bias, (int)):
        write_log("Шифр Цезаря (ASCII): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
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
            return "\u001b[33m[ Внимание: Выход за границы (Смещение < 65 либо > 122) ]\u001b[0m"
        B.append(n)
    #print("[ Смещенные значения символов по таблице ASCII ]",B)
    
    for c in B:
        c = chr(c)
        C.append(c)

    result = "".join(C)
    return result

def caesar_dictionary(text, shift):
    if not isinstance(shift, (int)):
        write_log("Шифр Цезаря (Словарь): ValueError", "Ошибка: Введено не числовое значение")
        return "\033[31m[ Ошибка: Введено недопустимое значение ]\033[0m"
    result = ""
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
        'Z': 26
        }
    num_to_char = {v: k for k, v in dc.items()}
    
    for char in text:
        if char.isalpha():
            is_lower = char.islower()
            base_char = char.upper()
            base_num = dc[base_char]
            shifted_num = (base_num + shift - 1) % 26 + 1
            shifted_char = num_to_char[shifted_num]
            result += shifted_char.lower() if is_lower else shifted_char
        else:
            result += char
    return result
