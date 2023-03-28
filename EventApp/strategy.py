import requests, json

def get_classifications():
    url = "https://app.ticketmaster.com/discovery/v2/classifications?apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&locale=*"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_body = response.json()
    classification_list = response_body["_embedded"]["classifications"]
    classifications = []
    for classification in classification_list:
        key = "segment" if "segment" in classification.keys() else "type"
        class_id = classification[key]["id"] 
        class_name = classification[key]["name"]
        print(class_id, class_name)
        classifications.append({"class_id":class_id,"class_name":class_name})
    return classifications

def get_event_detail_by_searchword(search_word):
    pass

def get_suggestion_list():
    url = "https://app.ticketmaster.com/discovery/v2/suggest?sort=relevance,desc&apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&locale=*"

    response = requests.request("GET", url)
    response_body = response.json()

    response_venue_list = response_body['_embedded']['venues']
    venue_list = []
    for venue in response_venue_list:
        venue_id = venue['id']
        venue_name = venue['name']
        venue_image = venue['images'][0]['url'] if 'images' in venue.keys() else "https://media.npr.org/assets/img/2021/11/06/gettyimages-1351654275-7d1654f8a83da60c48172bc53aab2fa7d3e50c1b-s1100-c50.jpg"
        venue_upcoming_event = venue['upcomingEvents']['_total']
        venue_list.append(dict(venue_name = venue_name, venue_id = venue_id, venue_image=venue_image, venue_upcoming_event=venue_upcoming_event))

    response_attraction_list = response_body['_embedded']['attractions']
    attraction_list = []
    for attraction in response_attraction_list:
        attr_id = attraction['id']
        attr_name = attraction['name']
        attr_image = attraction['images'][1]['url']
        attr_upcoming_event = attraction['upcomingEvents']['_total']
        attraction_list.append(dict(attr_id=attr_id, attr_name=attr_name, attr_image=attr_image, attr_upcoming_event=attr_upcoming_event))
    print(f"length of event list = {len(venue_list)} attraction list = {len(attraction_list)}")
    return {'venue_list':venue_list, 'attraction_list':attraction_list}
