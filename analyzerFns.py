import urllib.request
from bs4 import BeautifulSoup
import re
def sentences(lst):
    l = re.split(r'[.!?]+', lst)
    return len(l)

def dictionary(val):
    #val is a string
    lst = []
    lst = val.split()
    res = {}
    c = []
    for i in lst:
        c.append(lst.count(i))
    res = dict(zip(lst,c))
    return res


    #[a,b,c]
def url(url):
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp.read(), 'html.parser')
    for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text
#res =  {'Apple': 1.99, 'Banana': 0.99, 'Orange': 1.49, 'Cantaloupe': 3.99, 'Grapes': 0.39}
def sortDictionary(res,n):
    x =  sorted(res.items(), key = lambda x : x[1],reverse=True)
    lst =[]
    stopwords =  ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
    j,i=0,0
    while(j!=n):
        if(x[i][0] not in stopwords):
            lst.append(str(x[i][0]) + '-' + str(x[i][1]))
            j+=1
        i+=1
    return lst
#sortDictionary(res)
#print("total words : " , sum(res.values()))
#print("unique words : ", len(res))
#print("no of sentences : ", sentences(text))
