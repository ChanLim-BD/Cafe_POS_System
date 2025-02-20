from jamo import h2j, j2hcj

def get_initial_consonant(name):
    return ''.join([j2hcj(h2j(c))[0] for c in name if '\uac00' <= c <= '\ud7a3'])