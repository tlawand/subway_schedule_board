import requests
from pathlib import Path
from google.transit import gtfs_realtime_pb2
import urllib

ACE_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace"
ONE_TO_SEVEN_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"
BDFM_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm"

API_KEY = "ENavFdXno14bk22Nm45OF7RxuL8PpecM8ehvitSb" #MOVE TO .ENV FILE

headers={
        "x-api-key":API_KEY
        }

feed = gtfs_realtime_pb2.FeedMessage()

ace_resp = requests.get(
    ACE_URL, 
    headers={
        "x-api-key":API_KEY
        }
        )
feed.ParseFromString(ace_resp.content)
for entity in feed.entity:
    if entity.HasField("trip_update"):
        print(entity.trip_update)


"""
SAMPLE CODE FROM GOOGLE TRANSIT (https://developers.google.com/transit/gtfs-realtime/examples/python-sample)


from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.request.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
    # ^ this needs headers to work with MTA data, not sure how to do that
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)
"""