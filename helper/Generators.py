import random

NOUNS = ['BROOD', 'WARDEN', 'HOUSE', 'KNIFE', 'SHAPE',
         'CHARITY', 'LEGION', 'CITY', 'SHADOW', 'MIDNIGHT',
         'FRONT', 'RATIONS', 'WHISPER', 'SORROW',
         'SHADOW', 'PETITIONER', 'OUTBREAK', 'SLAB', 'CONFIDENCE',
         'SIGNAL', 'THREAT', 'QUESTION']
ADJECTIVES = ['LUCENT', 'ETERNAL', 'LIGHT', 'FIRST', 'FINAL',
              'HIGH', 'RED', 'LAST', 'SILENT', 'NAMELESS',
              'COLD', 'SPARE', 'VENGEFUL', 'SWEET']
VERBS = ['SUNDERED', 'DOOMED', 'PERFECTED', 'WHISPERING', 'KEPT',
         'SCATTER', 'VEILED', 'LOADED']
KEYS = ['TANK', 'KEY', 'PRIMIS', 'VICTIS', 'TAKEO', 'VODKA',
        'HALO', 'RING', 'ARBITER', 'BOMB', 'FLOOD', 'ARRAY',
        'MAJESTIC', 'LOGIC', 'RIVEN', 'WITNESS', 'RHULK', 'DROWN']

def genplaintext():
    mode = random.randint(0, 1)
    noun = NOUNS[random.randint(0, len(NOUNS)-1)]
    if mode == 0:
        adj = ADJECTIVES[random.randint(0, len(ADJECTIVES)-1)]
        return f"{adj} {noun}"
    else:
        verb = VERBS[random.randint(0, len(VERBS)-1)]
        return f"{verb} {noun}"

def genkey():
    return KEYS[random.randint(0, len(KEYS)-1)]

def genkeyorder(key: str):
    output = ""
    key = list(key)
    while len(key) > 0:
        rand_index = random.randint(0, len(key) - 1)
        output += key[rand_index]
        key.pop(rand_index)
    return output
