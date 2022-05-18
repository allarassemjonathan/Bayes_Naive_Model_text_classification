import  os
import math

STOP_WORDS = set(
    """
    a about above across after afterwards again against all almost alone along
    already also although always am among amongst amount an and another any anyhow
    anyone anything anyway anywhere are around as at b c d e f g h i j k l m n o p q r s t u v w x y z
    back be became because become becomes becoming been before beforehand behind
    being below beside besides between beyond both bottom but by
    call can cannot ca could
    did do does doing done down due during
    each eight either eleven else elsewhere empty enough even ever every
    everyone everything everywhere except
    few fifteen fifty first five for former formerly forty four from front full
    further
    get give go
    had has have he hence her here hereafter hereby herein hereupon hers herself
    him himself his how however hundred
    i if in indeed into is it its itself
    keep
    last latter latterly least less
    just
    made make many may me meanwhile might mine more moreover most mostly move much
    must my myself
    name namely neither never nevertheless next nine no nobody none noone nor not
    nothing now nowhere
    of off often on once one only onto or other others otherwise our ours ourselves
    out over own
    part per perhaps please put
    quite
    rather re really regarding
    same say says said see seem seemed seeming seems serious several she should show side
    since six sixty so some somehow someone something sometime sometimes somewhere
    still such
    take ten than that the their them themselves then thence there thereafter
    thereby therefore therein thereupon these they third this those though three
    through throughout thru thus to the together too top toward towards twelve twenty
    two
    under until up unless upon us used using
    various very very via was we well were what whatever when whence whenever where
    whereafter whereas whereby wherein whereupon wherever whether which while
    whither who whoever whole whom whose why will with within without would
    yet you your yours yourself yourselves
    """.split()
)

def update_distribution(filename, category):
    dico = load_distribution(category)
    if dico==None:
        dico = {}
    text = open(filename, 'r', encoding = "ISO-8859-1").read().lower()
    punc = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º­¨0123456789!→°()-[]{};:'"«»\,+<>./?@#$%^&*_~©'''
    for x in text:
        if x in punc:
            text = text.replace(x,' ')
    arr = text.split(' ')
    numbers = "0 1 2 3 4 5 6 7 8 9 ( )"
    numbers_arr = numbers.split(" ")
    keys = [word for word in arr if not word in STOP_WORDS]
    keys = [word for word in keys for el in word if not el in numbers_arr]
    for e in keys:
        if e in dico.keys():
                dico[e]=dico[e]+1
        else:
                dico[e] = 1
                
    fi = open("model_" + category + ".txt", 'w', encoding = "ISO-8859-1")
    
    dico = {k:v for k,v in sorted(dico.items(), key = lambda item: item[1])}
    for i in dico.keys():
        fi.write(i + ' ' + str(dico[i]) + '\n')
        
    fi.close()


def load_distribution(category):
    dico = {}
    f = open("model_" + category + ".txt", 'r', encoding= "ISO-8859-1")
    for line in f.readlines():
        temp = line.split(" ")
        if len(temp)>1:
            dico[temp[0]] = int(temp[1])
    return dico

def learn(category):
    files = [el for el in os.listdir(category + '_articles\\') if el[0:7] == 'article']
    for file in files:
        update_distribution(category + '_articles\\' + file, category)

def predict(name):
    text = open(name, 'r', encoding="ISO-8859-1").read().lower()
    punc = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º­¨0123456789!→°()-[]{};:'"«»\,+<>./?@#$%^&*_~©'''
    for x in text:
        if x in punc:
            text = text.replace(x,' ')
    arr = text.split(' ')
    numbers = "0 1 2 3 4 5 6 7 8 9 ( )"
    numbers_arr = numbers.split(" ")
    keys = [word for word in arr if not word in STOP_WORDS]
    keys = [word for word in keys for el in word if not el in numbers_arr]
    
    lists = []
    cats = ["politics", "sport", "science"]
    for cat in cats:
        dico = load_distribution(cat)
        lists.append(dico)
        
    sumlist = []
    suma = 0
    for dico in lists:
        for el in dico.keys():
            suma = suma + dico[el]
        sumlist.append(suma)
        suma = 0
    
    scores = []
    temp = 0
    for i in range(len(lists)):
        dico = lists[i]
        for el in keys:
            if el in dico.keys():
                temp = temp + (dico[el]/sumlist[i])
        scores.append(temp)
        temp = 0

    print(scores)
        

#update_distribution("sport_articles\\article1.txt", category)
#print(load_distribution(category))
#categories = ["politics", "sport", "science"]
#for cat in categories:
#    learn(cat)
    
predict("test.txt")
