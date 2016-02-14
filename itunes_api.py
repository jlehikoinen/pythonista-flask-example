"""
iTunes Search API:
https://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html
"""

import json
from operator import itemgetter

# PyPi
import requests

###

COUNTRY_CODE = 'fi'

###

def search_album(query, entity, limit):

  main_array = []

  base_url = 'https://itunes.apple.com/' + COUNTRY_CODE + '/search?term='
  url = base_url + query + '&entity=' + entity + '&limit=' + str(limit)

  try:
    response = requests.get(url)
    data_dict = response.json()
  except Exception, e:
    print str(e)

  # Quick and dirty iteration
  for item in data_dict["results"]:
    if (item["artistName"].lower()) == query.lower():
      if item.get("artistName", None):
        artist_name = item["artistName"]
      if item.get("collectionName", None): 
        album_name = item["collectionName"]
      if item.get("collectionPrice", None):
        album_price = item["collectionPrice"]
      else:
        album_price = "n/a"
      if item.get("artworkUrl60", None):
        album_cover = item["artworkUrl60"]
      if item.get("releaseDate", None):
        release_date = item["releaseDate"]

      sub_array = [artist_name, 
                   album_name, 
                   album_price, 
                   album_cover, 
                   release_date]
      main_array.append(sub_array)

  # Sort by releaseDate, latest first
  main_array = sorted(main_array, key=itemgetter(4), reverse=True)

  return main_array


def	main():

  data = search_album('Anthrax', 'album', 100)
  print data

if __name__ == '__main__':
  main()