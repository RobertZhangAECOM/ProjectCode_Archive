import traveltimepy as ttpy
import os
import json
from datetime import datetime

os.environ["TRAVELTIME_ID"] = '8e300d62'
os.environ["TRAVELTIME_KEY"] = '397d6c452ceb0add10ec1bb57bcfddcd'

departure_search = {
    'id': "public transport from Trafalgar Square",
    'departure_time':  datetime.utcnow().isoformat(),
    'travel_time': 900,
    'coords': {'lat': 51.507609, 'lng': -0.128315},
    'transportation': {'type': "public_transport"},
    'properties': ['is_only_walking']
}

arrival_search = {
    'id': "public transport to Trafalgar Square",
    'arrival_time':  datetime.utcnow().isoformat(),
    'travel_time': 900,
    'coords': {'lat': 51.507609, 'lng': -0.128315},
    'transportation': {'type': "public_transport"},
    'range': {'enabled': True, 'width': 3600}
}

out = ttpy.time_map(departure_searches=departure_search, arrival_searches=arrival_search)

print(json.dumps(out, indent=4, sort_keys=True))
