import math
import random
#VERBS
with open ("verbs.txt","r") as myfile:
    verbs = myfile.read().replace('\n','/')

verbs=verbs.split('/')
verbs.pop()
verbs.pop()

total_verbs = len(verbs)/3

#NOUNS
with open ("nouns.txt","r") as myfile:
    nouns = myfile.read().replace('\n',' ')

nouns=nouns.split()
total_nouns = len(nouns)

#PRONOUNS
with open ("pronouns.txt","r") as myfile:
    pronouns = myfile.read().replace('\n',' ')

pronouns = pronouns.split()
total_pronouns = len(pronouns)

#PREPOSITIONS
with open ("prepositions.txt","r") as myfile:
    prepositions = myfile.read().replace('\n',' ')

prepositions = prepositions.split();
total_prepositions = len(prepositions)

#CONJUNCTIONS
with open ("conjunctions.txt","r") as myfile:
    conjunctions = myfile.read().replace('\n',' ')

conjunctions = conjunctions.split()
total_conjunctions = len(conjunctions)

#ADJECTIVES
with open ("adjectives.txt","r") as myfile:
    adjectives = myfile.read().replace('\n',' ')

adjectives = adjectives.split()
total_adjectives = len(adjectives)

#ADVERB
with open ("adverbs.txt","r") as myfile:
    adverbs = myfile.read().replace('\n',' ')

adverbs = adverbs.split()
total_adverbs = len(adverbs)

#INTERJECTIONS
with open ("interjections.txt","r") as myfile:
    interjections = myfile.read().replace('\n',' ')

interjections = interjections.split()

total_interjections = len(interjections)


def genSentence():
    inter_chance = random.random()
    sentence = ""

    if (inter_chance > 0.9):
        sentence = sentence + interjections[math.floor(total_adverbs*random.random())]
        sentence = sentence + ", "

    #either pronoun, adverb or noun
    word_choice = random.random()

    if (word_choice < 0.3):
        sentence = sentence + pronouns[math.floor(total_pronouns*random.random())] + " "
    elif (word_choice < 0.6):
        sentence = sentence + adverbs[math.floor(total_adverbs*random.random())] + " "
    elif (word_choice < 1):
        if (random.random() > .69):
            sentence = sentence + adjectives[math.floor(total_adjectives*random.random())] + " "
        sentence = sentence + nouns[math.floor(total_nouns*random.random())] + " "

    sentence = sentence + verbs[math.floor(total_verbs*random.random())] + " "

    #preposition+adjective+noun, pronoun+adjective+noun or conjunction+pronoun+noun+adverb+verb+pronoun
    end_choice = random.random()
    if (end_choice < 0.4):
        sentence = sentence + prepositions[math.floor(total_prepositions*random.random())] + " " + adjectives[math.floor(total_adjectives*random.random())] + " " + nouns[math.floor(total_nouns*random.random())]
    elif (end_choice < 0.8):
        sentence = sentence + pronouns[math.floor(total_pronouns*random.random())] + " " + adjectives[math.floor(total_adjectives*random.random())] + " " + nouns[math.floor(total_nouns*random.random())]
    else:
        sentence = sentence + conjunctions[math.floor(total_conjunctions*random.random())] + " " + pronouns[math.floor(total_pronouns*random.random())] + " " + nouns[math.floor(total_nouns*random.random())] + adverbs[math.floor(total_adverbs*random.random())] + " " + verbs[math.floor(total_verbs*random.random())] + " " + pronouns[math.floor(total_pronouns*random.random())]

    return sentence
