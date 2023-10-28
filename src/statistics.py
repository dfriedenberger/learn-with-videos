

LEVEL_MAP = {
    "A1" : 1,
    "A2" : 2,
    "B1" : 10,
    "B2" : 20,
    "C1" : 50,
    "XX" : 99
}


def get_max_level(phrase):
    phrase_level = 0
    level = "A0"
    for word in  phrase["words"]:
        if not word['is_vocabulary']:
            continue
        word_level = LEVEL_MAP[word['level']]
        if word_level > phrase_level:
            phrase_level = word_level
            level = word['level']
    return level

def cluster_by_level(video):

    levels = {}
    for phrase in video.dataset:
        level = get_max_level(phrase)
        if level not in levels:
            levels[level] = []
        levels[level].append(phrase['text'])

    return levels

def cluster_by_pos(video):
    pos = {}
    for phrase in video.dataset:
        for word in  phrase["words"]:
            if word['pos'] not in pos:
                pos[word['pos']] = set()
            pos[word['pos']].add(word['text'])
    return pos
