import os
import textwrap
def log_create():
    text = textwrap.dedent(
            """
            "В главном меню": True
            "Выход из программы": True
            "Арифметические операции: ValueError": True
            "Квадратное уравнение: ValueError": True
            "Факториал: ValueError": True
            "Массив: ValueError": True
            "Массивы: Добавление элементов ValueError": True
            "Массивы: Изменение элементов ValueError": True
            "Открыта функция Арифметические операции": True
            "Открыта функция Квадратное уравнение": True
            "Открыта функция Факториал": True
            "Открыта функция Массивы": True
            "Открыта функция Настройки логирования": True
            "Использована функция Арифметические операции": True
            "Использована функция Квадратное уравнение": True
            "Использована функция Факториал": True
            "Использована функция Массивы": True
            "Использована функция Настройки логирования": True
            "Массивы: Поиск по массиву": True
            "Массивы: Добавление элементов": True
            "Массивы: Изменение элементов": True
            "Массивы: Удаление элементов": True
            """
            ).strip()
    saves_folder = "saves"
    os.makedirs(saves_folder, exist_ok=True)
    log_types_file_path = os.path.join(saves_folder, "log_types.txt")
    if os.path.exists(log_types_file_path):
        return 0
    else:
        with open(log_types_file_path,'a', encoding='utf-8') as log_file:
            log_file.write(text)
    return log_file


def log_check(message):
    saves_folder = "saves"
    os.makedirs(saves_folder, exist_ok=True)
    log_types_file_path = os.path.join(saves_folder, "log_types.txt")
    with open(log_types_file_path,'r', encoding='utf-8') as log_file:
        lines = log_file.readlines()
    logs = {}
    for line in lines:
        line = line.strip()
        if '": ' in line:
            key_part, value_part = line.rsplit('": ', 1)
            key = key_part.strip('"')
            value = value_part.strip()
            logs[key] = value

    if message == "Заглушка":
        return logs
    else:
        message_lower = message.strip().lower()
        logs_lower = {k.lower(): v for k, v in logs.items()}
    
        if message_lower in logs_lower:
            if logs_lower[message_lower] == 'True':
                return True
            elif logs_lower[message_lower] == 'False':
                return False
            else:
                return f"Значение для {message} не найдено"
        else:
            return f"{message} не найдено"
    

def log_read():
    message = "Заглушка"
    logs = log_check(message)
    max_key_len = max(len(key) for key in logs.keys())
    result_part = []
    for key, value in logs.items():
        end = f"[ {key.ljust(max_key_len)} ][ {value} ]"
        result_part.append(end)
    result = "\n".join(result_part)
    return print(result)
