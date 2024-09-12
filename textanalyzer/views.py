# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')


def analyze_char(request):
    djchar = request.GET.get('text', 'default')
    charcount = request.GET.get('charcount', 'off')

    if charcount == "on":
        analyzed_char = len(djchar)
        params = {'purpose': 'Character Count', 'charcount': analyzed_char}
        return render(request, 'analyze_char.html', params)
    
    else:
        return HttpResponse('Error')


def analyze_vowel(request):
    djvowel = request.GET.get('text', 'default')
    vowels = request.GET.get('vowels', 'off')

    if vowels == "on":
        analyzed_vowel = 0
        analyzed_cons = 0
        for char in djvowel:
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                analyzed_vowel += 1

            else:
                analyzed_cons += 1
        params = {'purpose': 'Vowel Count', 'vowelcount': analyzed_vowel, 'conscount': analyzed_cons}
        return render(request, 'analyze_vowel.html', params)
    
    else:
        return HttpResponse('Error')


def removepunc(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")


def charcount(request):
    # Get the text
    djchar = request.GET.get('text', 'default')
    print(djchar)
    #Analyze the text
    return HttpResponse("analyze_char")


def vowels(request):
   # Get the text
    djvow = request.GET.get('text', 'default')
    print(djvow)
    #Analyze the text
    return HttpResponse("analyze_vowels")



