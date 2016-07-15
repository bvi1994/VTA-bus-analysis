# cleanStops.py - Removes unncessary views in the JSON file exported by
# from https://data.vta.org/Transit-Operations/Stops-January-2015 to use for
# analysis

import json, requests, sys

cleanData = open('bus-stop-clean.json', 'w')

with open('bus-stops-initial.json') as initial:
	initialData = json.data(initial)
	for stop in initial:
		del stop["VTA_Bench"]



