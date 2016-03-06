import nltk
from nltk.corpus import sentiwordnet as swn

ps = nltk.stem.porter.PorterStemmer()
lemma = nltk.wordnet.WordNetLemmatizer()

            
##data
sen='Volkswagen Group to recall 323,700 diesel cars in India'
##

def post(sen):
    z=nltk.pos_tag(sen)
    print(z)
    return z

#Stemme
def stemm(word):
    return word,ps.stem(word)

#Lemmatizer
def lemm(word):
    lemma.lemmatize(word)

    
def sentival(word,pospeach,posi):
    try:
            li=swn.senti_synset(word+'.'+pospeach+'.'+posi)
            return [li.obj_score(),li.pos_score(),li.neg_score()]
    except:
        return [0,0,0]

pos=0
hno=0
def start(sen):
    arr=[]
    sen1=sen.lower().split()
    noise=[',',"'",'.','-',]
    senarry=[i.strip() for i in sen1 if i not in noise]
    l=post(senarry)
    za=[0,0,0]
    for i in l:
        w,v=i
        r,w=stemm(w)
        print(r)
        v=v[0].lower()
        x,y,z=sentival(w,v,str(pos))
        #print(x,y,z)
        print(y,z)
        za=[za[0]+x,za[1]+y,za[2]+z,]
    #print('For Day 1 Headline {}'.format(hno),end='')
    #print(za)
    return za

with open('Bill.txt') as news:
    l=news.readlines()
    final=[0,0,0]
    for i in l:
        if i:
            hno=hno+1
            x,y,z=start(i)
            final=[final[1]+y,final[2]+z]
            #final=[final[0]+x,final[1]+y,final[2]+z]
    print('Finally For Day 1'+str(final))
