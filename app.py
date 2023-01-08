from difflib import SequenceMatcher


def alg(a, b):
    return SequenceMatcher(None, a, b).ratio()
