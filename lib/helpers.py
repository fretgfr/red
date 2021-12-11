# holds helper functions

def convert_yn(string: str) -> bool:
    """Converts Yes/No to True or False

    Args:
        string (str): [description]

    Returns:
        bool: True if Yes, False if No
    """
    if string.lower() == 'yes':
        return True
    else:
        return False

def convert_01(number: int) -> bool:
    """Converts 0/1 to True or False

    Args:
        number (int): The number to convert

    Returns:
        bool: 1 if True, 0 if False
    """
    if number == 1:
        return True
    else:
        return False

def convert_tf(boolean: bool) -> int:
    """Converts True/False to 0/1

    Args:
        boolean (bool): The boolean to convert

    Returns:
        int: 1 if True, 0 if False
    """    
    if boolean:
        return 1
    else:
        return 0

def convert_01_yn(number: int) -> str:
    """Converts 0/1 to Yes/No

    Args:
        number (int): The number to convert

    Returns:
        str: Yes if 1, No if 0
    """    
    if number == 1:
        return 'Yes'
    else:
        return 'No'