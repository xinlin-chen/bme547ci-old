import re

def is_tachycardic(string_in):
    string = string_in.lower()
    if re.search('tachycardic', string):
        print('True')
        return True
    else:
        print('False')
        return False
