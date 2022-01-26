# self-made

# pip install requests
# pip install django-shortcuts

# import urllib.request
# from urllib import request
import requests
from django.http import HttpResponse  # for response via Http
from django.shortcuts import render   # for templates
# from django.shortcuts import render, redirect
# import urllib.request
# from urllib.request import urlopen

# def index(request):
#     return HttpResponse("<h1> Hey there!! </h1>")
# ------------------------------------------------------------------------------------------------------

# to display the content of a text file
# def index(request):
#     file = open("text_utilities/one.txt", "r+")
#     return HttpResponse(file.read())
#     file.close() 
# -------------------------------------------------------------------------------------------------------

# to link a site in django
# def index(request):
#     # return HttpResponse("About me?? ") 
#     return HttpResponse('''<h1> Hey there!! </h1> <ahref = "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> youtube </a>''')
# -------------------------------------------------------------------------------------------------------

# directs to another page loading
# def about(request):
#     return HttpResponse("About me?? ")  
# --------------------------------------------------------------------------------------------------------

# pipelining
# def index(request):
#     return HttpResponse("Home")

# def remove_punctuation(reuqest):
#     return HttpResponse("Remove punctuation")

# def CapFirst(reuqest):
#     return HttpResponse("Capitalize first")

# def NewLineRemover(reuqest):
#     return HttpResponse("Removes new line")

# def SpaceRemover(reuqest):
#     return HttpResponse("Removes space")

# def CharCount(reuqest):
#     return HttpResponse("Counts the character <a href = '/''> back </a>")
# ----------------------------------------------------------------------------------------------------------

# to create button
# def index(request):
#     # a = (" <button> <ahref = "/remove_punctuation"> About </a> ")
#     a = (''' <button> <ahref = "/remove_punctuation"> About </a> ''')
#     return HttpResponse(a)
# -----------------------------------------------------------------------------------------------------------

#  creating templates in general
# def index(request):
#     parameters = {'Name': 'Solcae', 'Year': '2020'}
#     # return render(request, 'index.html')
#     return render(request, 'index.html', parameters)
#     Type this in the body of index.html for parameters --> {{Name}} is in {{Year}}
# -----------------------------------------------------------------------------------------------------------

# creating template for text utlities
# def index(request):
#     return render(request, 'index.html')

# def remove_punctuation(reuqest):
#     # print(requests.GET.get('text', 'default'))
#     print(requests.get('text', 'default'))
#     # TextFromUser = requests.GET.get('text', 'default')
#     # TextFromUser = requests.get('text', 'default')
#     # print(TextFromUser)
#     return HttpResponse("Remove punctuation")
# ------------------------------------------------------------------------------------------------------------

# to compile all functions into Analyze
def index(request):
    return render(request, 'index.html')

def Analyze(reuqest):
    # TextFromUser = requests.GET.get('text', 'default')
    # remove_punctuation = requests.GET.get('remove_punctuation', 'off')
    TextFromUser = requests.get('text', 'default')
    remove_punctuation = requests.get('remove_punctuation', 'off')
    print(remove_punctuation)
    print(TextFromUser)
    return HttpResponse("Remove punctuation")