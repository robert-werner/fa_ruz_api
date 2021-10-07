LATIN_CYRILLIC_MAP = {
    'А': 'А',  # A
    'B': 'В',  # B
    'C': 'С',  # C
    'E': 'Е',  # E
    'H': 'Н',  # H
    'K': 'К',  # K
    'M': 'М',  # M
    'O': 'О',  # O
    'P': 'Р',  # P
    'T': 'Т',  # T
    'X': 'Х',  # X
    'Y': 'У',  # Y (questionable)
    'a': 'а',  # a
    'c': 'с',  # c
    'e': 'е',  # e
    'o': 'о',  # o
    'p': 'р',  # p
    'x': 'х',  # x
    'y': 'у'  # y
}

CYRILLIC_LATIN_MAP = {v: k for k, v in LATIN_CYRILLIC_MAP.items()}


def letterflip(string, reverse=True):
    """
    This monkey patch performs a replacement of latin letters to same looking russian letters.
    """
    if reverse:
        return "".join(CYRILLIC_LATIN_MAP.get(c, c) for c in string)
    else:
        return "".join(LATIN_CYRILLIC_MAP.get(c, c) for c in string)
