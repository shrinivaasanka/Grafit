##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
# Course Authored By:
# --------------------------------------------------------------------------------------------------------
# K.Srinivasan
# Krishna iResearch FOSS - http://www.krishna-iresearch.org
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://acadpdrafts.readthedocs.io/en/latest/
# --------------------------------------------------------------------------------------------------------

from collections import defaultdict
import csv
from QuestionAnswering import create_sentence_PoS_dict_from_treebank
import itertools
import numpy as np
import operator
import WordNetPath

def synthesize_chomsky_sentences(sentence_template=[], corpus="../../../../../asfer-github-code/python-src/NeuronRainApps/QuestionAnswering/words_pos.csv",treebankdatasets=["wsj_0002.mrg","wsj_0003.mrg","wsj_0004.mrg","wsj_0005.mrg"],max_templates=2,max_sentences=20,threshold_wordnet_distance=100,dictionary_template=False,perplexity_algorithm="None"):
    PennTreebankPoS={"CC":"Coordinating conjunction",
            "CD":"Cardinal number",
            "DT":"Determiner",
            "EX":"Existential there",
            "FW":"Foreign word",
            "IN":"Preposition or subordinating conjunction",
            "JJ":"Adjective",
            "JJR":"Adjective, comparative",
            "JJS":"Adjective, superlative",
            "LS":"List item marker",
            "MD":"Modal",
            "NN":"Noun, singular or mass",
            "NNS":"Noun, plural",
            "NNP":"Proper noun, singular",
            "NNPS":"Proper noun, plural",
            "PDT":"Predeterminer",
            "POS":"Possessive ending",
            "PRP":"Personal pronoun",
            "PRP$":"Possessive pronoun",
            "RB":"Adverb",
            "RBR":"Adverb, comparative",
            "RBS":"Adverb, superlative",
            "RP":"Particle",
            "SYM":"Symbol",
            "TO":"to",
            "UH":"Interjection",
            "VB":"Verb, base form",
            "VBD":"Verb, past tense",
            "VBG":"Verb, gerund or present participle",
            "VBN":"Verb, past participle",
            "VBP":"Verb, non-3rd person singular present",
            "VBZ":"Verb, 3rd person singular present",
            "WDT":"Wh-determiner",
            "WP":"Wh-pronoun",
            "WP$":"Possessive wh-pronoun",
            "WRB":"Wh-adverb"}
    number_of_sentences=0
    listofsentences=[]
    corpus_PoS2Vocabulary_dict=defaultdict(list)
    merit2sentence_dict=defaultdict(list)
    with open(corpus, newline='') as wordsposcsv:
        wordsposreader = csv.reader(wordsposcsv, delimiter=',')
        for row in wordsposreader:
            corpus_PoS2Vocabulary_dict[row[2]].append(row[1])
    print("PoS-words corpus keys:",corpus_PoS2Vocabulary_dict.keys())
    print("Penn Treebank PoS keys:",PennTreebankPoS.keys())
    missing=set(corpus_PoS2Vocabulary_dict.keys()).symmetric_difference(set(PennTreebankPoS.keys()))
    print("List of PoS not present in PoS-words corpus (and hence marked blank in sentences):",missing)
    if dictionary_template:
        list_of_sentence_PoS_iterables=create_sentence_PoS_dict_from_treebank(datasets=treebankdatasets)
    else:
        list_of_sentence_PoS_iterables=create_sentence_PoS_dict_from_treebank(datasets=treebankdatasets,returnasarray=True)
    #for template in np.random.permutation(list_of_sentence_PoS_iterables[:max_templates]):
    for template in list_of_sentence_PoS_iterables[:max_templates]:
        templaterepr=str(template)
        print("----------------------------------------------------------------")
        print("template :",templaterepr)
        print("----------------------------------------------------------------")
        if dictionary_template:
            templatecopy=template.copy()
            for PoS in corpus_PoS2Vocabulary_dict.keys():
                 templatecopy[PoS]=np.random.permutation(corpus_PoS2Vocabulary_dict[PoS]).tolist()
            templatevalues=[]
            templatekeys=[]
            templatecopy.pop('pos_tag',None)
            for PoS,words in templatecopy.items():
                if words==[]:
                    templatecopy[PoS]=["<"+PoS+">"]
                    templatevalues.append(["<"+PoS+">"])
                else:
                    templatevalues.append(words)
                    templatekeys.append(PoS)
            print("filled template:",templatecopy)
            print("templatekeys (inorder traversed (flattened) PoS grammar tree dict template):",templatekeys)
            print("dict templatevalues:",templatevalues)
        else:
            templatecopy=template.copy()
            for pos_words in templatecopy:
                for PoS in corpus_PoS2Vocabulary_dict.keys():
                    if pos_words[0] == PoS:
                        pos_words[1]=np.random.permutation(corpus_PoS2Vocabulary_dict[PoS]).tolist()
            templatevalues=[]
            templatekeys=[]
            for pos_words in templatecopy:
                if pos_words[1]==[]:
                    pos_words[1]=["<"+pos_words[0]+">"]
                    templatevalues.append(["<"+pos_words[0]+">"])
                else:
                    templatevalues.append(pos_words[1])
                    templatekeys.append(pos_words[0])
            print("templatekeys (inorder traversed (flattened) PoS grammar tree array template):",templatekeys)
            print("array templatevalues:",templatevalues)
        for product in itertools.product(*templatevalues):
            if perplexity_algorithm=="WordNet":
                from RecursiveGlossOverlap_Classifier import RecursiveGlossOverlapGraph, RecursiveGlossOverlap_Classify
                wordnet_distance=find_wordnet_distance(product)
                if wordnet_distance[0] < threshold_wordnet_distance:
                    sentence=" ".join(product)
                    print("Sentence ",number_of_sentences,":",sentence," for PoS template ",templaterepr)
                    print("Part-of-speech mapping of Sentence ",number_of_sentences," printed for validation:",part_of_speech_mapping(templatekeys,product))
                    rgograph=RecursiveGlossOverlapGraph(sentence)
                    rgographcomplexity=RecursiveGlossOverlap_Classify(sentence)
                    print("Sentence intrinsic merit:",rgograph[1])
                    print("Sentence RGO Graph complexity:",rgographcomplexity)
                    merit2sentence_dict[rgograph[1]].append(sentence)
            else:
                sentence=" ".join(product)
                print("Sentence ",number_of_sentences,":",sentence," for PoS template ",templaterepr)
                listofsentences.append(sentence)
            number_of_sentences += 1
            if number_of_sentences >= max_sentences:
                     break
        if perplexity_algorithm=="WordNet":
            sorted_by_merit = sorted(list(merit2sentence_dict.items()), key=operator.itemgetter(1), reverse=True)
            print("Chomsky Sentences synthesized - Sorted by merit:",sorted_by_merit)
        else:
            print("Chomsky Sentences synthesized :",listofsentences)


def part_of_speech_mapping(pos,words):
    pos_words_dict={}
    for key,value in zip(pos,words):
        pos_words_dict[key]=value
    return pos_words_dict

def find_wordnet_distance(sentencetoks):
    totaldistance=0
    totalpairs=0
    for x in range(len(sentencetoks)-2):
        distance = WordNetPath.path_between(sentencetoks[x],sentencetoks[x+1])
        #print("distance=",distance)
        totaldistance += len(distance)
        totalpairs += 1
    averagedistance = totaldistance/totalpairs
    print("totaldistance:",totaldistance,",averagedistance:",averagedistance)
    return (totaldistance, averagedistance) 

if __name__=="__main__":
    print("------------Array Templates-------------------")
    synthesize_chomsky_sentences(max_sentences=5,threshold_wordnet_distance=10,dictionary_template=False)
    print("------------Dictionary Templates-------------------")
    synthesize_chomsky_sentences(max_sentences=5,threshold_wordnet_distance=10,dictionary_template=True)
