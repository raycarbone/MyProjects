# module lexicon.py

def scan(word_list):
    '''Pass a directive into scan and get back a tuple of what kind of directive it is along with the directive
    '''
    lexi = {
    'direction': ['north', 'south', 'east', 'west'],
    'verb': ['go', 'stop', 'kill', 'eat', 'fart'],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
    'noun': ['door', 'bear', 'princess', 'cabinet'],
     }

    tuplelist = []
    words = word_list.split()

    count = 0
    for word in words:
        try:
            tuplelist.append(('number', int(word)))
        except ValueError:
            for key in lexi.keys():
                if word in lexi[key]:
                    tuplelist.append((key, word))
        count += 1
        if len(tuplelist) != count:
            tuplelist.append(('error', word))
            count = len(tuplelist)


    return tuplelist





