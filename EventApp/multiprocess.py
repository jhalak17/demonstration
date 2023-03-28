import requests, json

def get_event_ticketmaster(searchword):

    url = "https://app.ticketmaster.com/discovery/v2/events?apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&locale=*&sort=date,asc&keyword="+searchword
    response = requests.request("GET", url)
    response_body = response.json()
    if "page" in response_body.keys():
        if response_body["page"]["totalElements"] == 0:
            return {"error_message":"No record found !!!!"}
    event_list = response_body["_embedded"]["events"]
    event_response_list = []
    for event in event_list:
        try:
            ticket_company = "Ticket Master"
            event_id = event["id"]
            event_name = event["name"]
            event_image = event["images"][1]["url"]
            event_date = event["dates"]["start"]["localDate"]
            event_timezone = event["dates"]["timezone"] if "timezone" in event["dates"].keys() else "-"
            if "priceRanges" in event.keys():
                price_range = event["priceRanges"]
                min_price = price_range[0]["min"] 
                currency = price_range[0]["currency"] 
            else:
                min_price = "-"
                currency = "-"
            event_venue = event["_embedded"]["venues"] if "venues" in event["_embedded"].keys() else None
            venue_name = event_venue[0]["name"] if event_venue else "-"
            event_attraction = event["_embedded"]["attractions"] if "attractions" in event["_embedded"].keys() else None
            performer_name = event_attraction[0]["name"] if event_attraction else "-"
            event_response_list.append(dict(ticket_company=ticket_company, event_id=event_id, event_name=event_name, event_image=event_image, event_date=event_date, event_timezone=event_timezone, min_price=min_price, currency=currency, venue_name=venue_name, performer_name=performer_name))
        except:
            print("*********** exception occured ************")
            continue

    return event_response_list

def get_venue_ticketmaster(searchword):

    url = "https://app.ticketmaster.com/discovery/v2/events?apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&locale=*&sort=date,asc&venueId="+searchword
    response = requests.request("GET", url)
    response_body = response.json()
    if "page" in response_body.keys():
        if response_body["page"]["totalElements"] == 0:
            return {"error_message":"No record found !!!!"}
    event_list = response_body["_embedded"]["events"]
    event_response_list = []
    for event in event_list:
        try:
            ticket_company = "Ticket Master"
            event_id = event["id"]
            event_name = event["name"]
            event_image = event["images"][1]["url"]
            event_date = event["dates"]["start"]["localDate"]
            event_timezone = event["dates"]["timezone"] if "timezone" in event["dates"].keys() else "-"
            if "priceRanges" in event.keys():
                price_range = event["priceRanges"]
                min_price = price_range[0]["min"] 
                currency = price_range[0]["currency"] 
            else:
                min_price = "-"
                currency = "-"
            event_venue = event["_embedded"]["venues"] if "venues" in event["_embedded"].keys() else None
            venue_name = event_venue[0]["name"] if event_venue else "-"
            event_attraction = event["_embedded"]["attractions"] if "attractions" in event["_embedded"].keys() else None
            performer_name = event_attraction[0]["name"] if event_attraction else "-"
            event_response_list.append(dict(ticket_company=ticket_company, event_id=event_id, event_name=event_name, event_image=event_image, event_date=event_date, event_timezone=event_timezone, min_price=min_price, currency=currency, venue_name=venue_name, performer_name=performer_name))
        except:
            print("*********** exception occured ************")
            continue

    return event_response_list

def get_attraction_ticketmaster(searchword):

    url = "https://app.ticketmaster.com/discovery/v2/events?apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&locale=*&sort=date,asc&attractionId="+searchword
    response = requests.request("GET", url)
    response_body = response.json()
    if "page" in response_body.keys():
        if response_body["page"]["totalElements"] == 0:
            return {"error_message":"No record found !!!!"}
    event_list = response_body["_embedded"]["events"]
    event_response_list = []
    for event in event_list:
        try:
            ticket_company = "Ticket Master"
            event_id = event["id"]
            event_name = event["name"]
            event_image = event["images"][1]["url"]
            event_date = event["dates"]["start"]["localDate"]
            event_timezone = event["dates"]["timezone"] if "timezone" in event["dates"].keys() else "-"
            if "priceRanges" in event.keys():
                price_range = event["priceRanges"]
                min_price = price_range[0]["min"] 
                currency = price_range[0]["currency"] 
            else:
                min_price = "-"
                currency = "-"
            event_venue = event["_embedded"]["venues"] if "venues" in event["_embedded"].keys() else None
            venue_name = event_venue[0]["name"] if event_venue else "-"
            event_attraction = event["_embedded"]["attractions"] if "attractions" in event["_embedded"].keys() else None
            performer_name = event_attraction[0]["name"] if event_attraction else "-"
            event_response_list.append(dict(ticket_company=ticket_company, event_id=event_id, event_name=event_name, event_image=event_image, event_date=event_date, event_timezone=event_timezone, min_price=min_price, currency=currency, venue_name=venue_name, performer_name=performer_name))
        except:
            print("*********** exception occured ************")
            continue

    return event_response_list