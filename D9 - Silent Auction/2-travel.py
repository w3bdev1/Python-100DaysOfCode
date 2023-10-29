
travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_travel_entry(country_name, number_of_visits, list_of_cities):
    travel_log.append({
        "country": country_name,
        "visits": number_of_visits,
        "cities": list_of_cities
    })

add_travel_entry("Russia", 2, ["Moscow", "St. Petersburg"])

print(travel_log[-1])