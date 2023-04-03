from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .multiprocess import get_event_ticketmaster, get_venue_ticketmaster, get_attraction_ticketmaster, get_classification_search_result
from .strategy import get_suggestion_list
import geocoder
from geopy.geocoders import Nominatim

# Fetching latitude and longitude of the user 
geo_data = geocoder.ip('me')
latitude = geo_data.lat
longitude = geo_data.lng
print("from geolocation ==========", latitude, longitude)
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse(str(latitude)+","+str(longitude))
address = location.raw['address']
print(address)
state = address.get("state",'')
# Location fetch ends

class Search_Event(View):

    # Get event suggestions from TicketMaster
    def get(self, request):
        suggestion_response = get_suggestion_list(state)  
        print("state sent =======", state)
        return render(request, 'base.html', {'suggestion_response':suggestion_response, 'state':state})

    # Search events based on search word
    def post(self, request):
        search_event_word = request.POST.get("search_word")
        search_city = request.POST.get("search_city")
        print("search word from form ========", search_event_word, search_city)
        search_response = get_event_ticketmaster(search_event_word, search_city)
        if "error_message" in search_response:
            return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
        else:
            return render(request, 'searchtable.html', {"response_event_list":search_response})

# Display all events based on category selected by user       
def get_concert_page(request):
    classification_id = request.GET.get('id')
    print("classification_id ======= ",classification_id, type(classification_id))
    search_response = get_classification_search_result(classification_id)
    if "error_message" in search_response:
        return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
    else:
        return render(request, 'concert_display.html', {"response_event_list":search_response})

# Display all events based on venue selected by user 
def get_venue_page(request):
    print(request.GET)
    search_event_word = request.GET.get("venue_id")
    search_response = get_venue_ticketmaster(search_event_word)
    if "error_message" in search_response:
        return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
    else:
        return render(request, 'searchtable.html', {"response_event_list":search_response})

# Display all events based on attrcation selected by user    
def get_attraction_page(request):
    print(request.GET)
    search_event_word = request.GET.get("attraction_id")
    search_response = get_attraction_ticketmaster(search_event_word)
    if "error_message" in search_response:
        return render(request, 'searchresult.html',{"error_message":"No record found !!!!"})   
    else:
        return render(request, 'searchtable.html', {"response_event_list":search_response})