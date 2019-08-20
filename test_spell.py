import enchant
import enchant.checker

def spellCheck(data):
    #with open(x, 'r') as myfile:
     #   data = myfile.read()
        
    #print(data)
    data.replace('\n',' ')
    c = []
    s = []
    chkr = enchant.checker.SpellChecker("en_US")
    d = enchant.Dict()
    chkr.set_text(data)
    for err in chkr:
        # print("ERROR: ", err.word)
        c.append(err.word)
        #print(d.suggest(err.word))
        s.append(d.suggest(err.word))
    # print(data)
    # print(s)
    # print(c)
    return data,c,s
