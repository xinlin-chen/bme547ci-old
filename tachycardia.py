import re


def is_tachycardic(string_in):
    string = string_in.lower()
    if re.search('tachycardic', string):
        return True
    else:
        return False
