from time import localtime, strftime

def simple_time():
    current_time = strftime("%d.%m.%Y %H:%M:%S", localtime())
    return current_time
