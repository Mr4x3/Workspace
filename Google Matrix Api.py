#!/usr/bin/python3
import json, urllib.request, requests
source="212 radford st, winston salem, nc 27106, USA"
destination="1834 Wake Forest Rd, Winston-Salem, NC 27109, United States"
#destination="San Francisco"
url = """https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&key=AIzaSyATklQLymFGmo3PWpQghzqPEXRffalESdw&mode=driving""".format(source,destination)
#k=urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?origins=212%20radford%20st,%20winston%20salem,%20nc%2027106,%20USA&destinations=1834%20Wake%20Forest%20Rd,%20Winston-Salem,%20NC%2027109,%20United%20States&key=AIzaSyATklQLymFGmo3PWpQghzqPEXRffalESdw")
#data = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins=212%20radford%20st,%20winston%20salem,%20nc%2027106,%20USA&destinations=1834%20Wake%20Forest%20Rd,%20Winston-Salem,%20NC%2027109,%20United%20States&key=AIzaSyATklQLymFGmo3PWpQghzqPEXRffalESdw").json()
data = requests.get(url).json()
#result= json.load(urllib.request.urlopen(k).read().decode('utf8'))
#print(data)
driving_time = data['rows'][0]['elements'][0]['duration']['text']
print(driving_time)
