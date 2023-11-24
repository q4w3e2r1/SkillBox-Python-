import re
import doctest

def check_password(password):
    """
    >>> check_password("20 января 1806")
    True
    >>> check_password("1924, July 25")
    True
    >>> check_password("26/09/1635")
    True
    >>> check_password("3.1.1506")
    True
    >>> check_password("25.08-1002")
    False
    >>> check_password("декабря 19, 1838")
    False
    >>> check_password("8.20.1973")
    False
    >>> check_password("Jun 7, -1563")
    False
    >>> check_password("31 февраля 2023")
    False
    >>> check_password("31 июня 2015")
    False
    >>> check_password(124125432)
    Traceback (most recent call last):
        ...
    Exception
    """
    if not isinstance(password, str):
        raise Exception
    if re.findall(r"^((?:[1-9]|[1-2]\d|30|31)/(?:[1-9]|0[1-9]|10|11|12)/\d{4})$|^((?:[1-9]|[1-2]\d|30|31)\.(?:[1-9]|0[1-9]|10|11|12)\.\d{4})$|^(\d{1,4}\,\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря|January|February|March|April|May|June|July|August|September|October|November|December)\s(?:[1-9]|[1-2]\d|30|31))$|^((?:[1-9]|[1-2]\d|30|31)\s(?:января|марта|мая|июля|августа|октября|декабря|January|March|May|July|August|October||December)\s\d{1,4})$|^((?:[1-9]|[1-2]\d|30)\s(?:|апреля|июня|сентября|ноября|April|June|September|November|)\s\d{1,4})$|^((?:[1-9]|[1]\d|2[0-8]|)\s(?:февраля|February)\s\d{1,4})$",
                  password):
        return True
    else:
        return False


doctest.testmod(verbose=True)