#!/usr/bin/env python3

from RESTfulClient import RESTfulClient

client = RESTfulClient()

for location in client.getAvailableTrendLocations():
	print('{}: {}'.format(location['name'], location['woeid']))
	for trendingTopic in client.getTopTrends(location['woeid'])[0]['trends']:
		print(trendingTopic['name'])
	print('\n')
