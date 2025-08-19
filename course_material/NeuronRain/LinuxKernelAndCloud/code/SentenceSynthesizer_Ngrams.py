import requests
import pprint
from collections import defaultdict
import operator

def get_ngrams_and_synthesize_sentence(query="hello+*"):
    freq2ngrams=defaultdict(int)
    r = requests.get('https://api.ngrams.dev/eng/search?query='+query+'&flags=cs\'')
    try:
        ngrams = r.json()["ngrams"]
        #pprint.pprint(ngrams)
    except:
        print("No matching ngrams")
        return
    sentencesdict={}
    if len(ngrams) > 0:
        for ng in ngrams:
            reltotalmatchcount=ng["relTotalMatchCount"]
            filledupsentence=""
            for ngramtokendict in ng["tokens"]:
                filledupsentence+=ngramtokendict['text']+" "
            sentencesdict[reltotalmatchcount]=filledupsentence
        print("---------------------------- Blank filled sentences for:" + query + " (sorted by probability) -------------")
        sortedsentencesdict=sorted(list(sentencesdict.items()), key=operator.itemgetter(1), reverse=True)
        pprint.pprint(sortedsentencesdict)
        return sortedsentencesdict

if __name__=="__main__":
    get_ngrams_and_synthesize_sentence(query="You+*+an+*+person")
    get_ngrams_and_synthesize_sentence(query="I+*+you+*+me")
    get_ngrams_and_synthesize_sentence(query="Large+*+models")

