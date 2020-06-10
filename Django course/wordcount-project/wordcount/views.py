from django.http import HttpResponse
from django.shortcuts import render
import operator

def Home(request):
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def Count(request):
    fulltext = request.GET['UserText']
    wordlist = fulltext.split()
    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            #Increase
            wordDictionary[word] += 1
        else:
            #add to dictionary
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'Count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':sortedWords})