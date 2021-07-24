import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','maps.settings')
import django
django.setup()
import requests, json
from home.models import Markers
from time import sleep

oblist = Markers.objects.all()
for ob in oblist:
    if ob.address == "":

        sleep(1)
        url = 'https://eu1.locationiq.com/v1/reverse.php?key='+os.environ.get("LocIQ_key")+'&lat=' + str( ob.lat) + '&lon=' + str(ob.lng) + '&format=json'
        det = requests.get(url)
        if det.status_code == 200:
            data = json.loads(det.content.decode())
            ob.display_address = data["display_name"]
            ob.address = data["address"]
            print(ob.display_address)
            ob.save()
        else:
            print(ob.id)