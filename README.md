# subway_schedule_board
code to run a Raspberry Pi or Arduino based board to show departures at a specific subway station in NYC


SAMPLE CODE FROM GOOGLE TRANSIT (https://developers.google.com/transit/gtfs-realtime/examples/python-sample)

```python
from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.request.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
    # ^ this needs headers to work with MTA data, not sure how to do that
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)
```