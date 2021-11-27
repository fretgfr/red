# holds helper functions

def convert_yn(string):
    if string.lower() == 'yes':
        return True
    else:
        return False

def convert_01(number: int) -> bool:
    if number == 1:
        return True
    else:
        return False

def convert_tf(boolean: bool) -> int:
    if boolean:
        return 1
    else:
        return 0

def convert_01_yn(number: int) -> str:
    if number == 1:
        return 'Yes'
    else:
        return 'No'