from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .multiprocess import get_event_ticketmaster, get_venue_ticketmaster, get_attraction_ticketmaster, get_classification_search_result
from .strategy import get_suggestion_list

# Create your views here.

class Search_Event(View):

    def get(self, request):
        # Get suggestions
        suggestion_response = get_suggestion_list()
        return render(request, 'main.html', {'suggestion_response':suggestion_response})

    def post(self, request):
        search_event_word = request.POST.get("search_event_word")
        search_response = get_event_ticketmaster(search_event_word)
        if "error_message" in search_response:
            return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
        else:
            return render(request, 'searchtable.html', {"response_event_list":search_response})

# Concert function       
def get_concert_page(request):
    print(request.GET)
    classification_id = request.GET.get('id')
    print("classification_id ======= ",classification_id, type(classification_id))
    search_response = get_classification_search_result(classification_id)
    if "error_message" in search_response:
        return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
    else:
        return render(request, 'concert_display.html', {"response_event_list":search_response})
    # return render(request, 'concert_display.html')

def get_venue_page(request):
    print(request.GET)
    search_event_word = request.GET.get("venue_id")
    search_response = get_venue_ticketmaster(search_event_word)
    if "error_message" in search_response:
        return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
    else:
        return render(request, 'searchtable.html', {"response_event_list":search_response})
    
def get_attraction_page(request):
    print(request.GET)
    search_event_word = request.GET.get("attraction_id")
    search_response = get_attraction_ticketmaster(search_event_word)
    if "error_message" in search_response:
        return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
    else:
        return render(request, 'searchtable.html', {"response_event_list":search_response})