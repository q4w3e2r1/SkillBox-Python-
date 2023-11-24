import re
import doctest

def check_password(password):
    """

    >>> check_password("rtG&3FG#Tr^e")
    True
    >>> check_password("a^A1@*@1Aa")
    True
    >>> check_password("oF^a1D@y5%e6")
    True
    >>> check_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True
    >>> check_password("!!!!!!!wqeqweqew^&^&^&")
    False
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$>W0Rd")
    False
    >>> check_password(12331)
    Traceback (most recent call last):
        ...
    Exception
    """
    if not isinstance(password, str):
        raise Exception
    if re.findall(r"^(?=.*[a-z].*[a-z])^(?!.*[,.!?])(?=.*\d)(?=(?:[^$^%@#&*,.!?]*[$^%@#&*]){3})[A-Za-z0-9^$%@#&*]{8,}$", password):
        return True
    else:
        return False


doctest.testmod(verbose=True)


