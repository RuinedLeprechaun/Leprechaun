import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','maps.settings')
import django
django.setup()
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from home.models import Markers


# Start the driver
path = "C:\\Users\\User\\PycharmProjects\\hspavailability\\chromedriver.exe"
driver = webdriver.Chrome(path)

oblist = Markers.objects.filter(Phone="0000000000")[1940:7000]
nf = 0
f=0
for ob in oblist:
    data = ob.name
    if "road" in ob.address:
        data = data + ", " + ob.address["road"]
    if "suburb" in ob.address:
        data = data + ", " + ob.address["suburb"]
    if "city" in ob.address:
        data = data + ", " + ob.address["city"]
    if "state_district" in ob.address:
        data = data + ", " + ob.address["state_district"]
    if "state" in ob.address:
        data = data + ", " + ob.address["state"]
    if "postcode" in ob.address:
        data = data + ", " + ob.address["postcode"]

    data.replace(" ","+")
    data.replace(",","%2C")
    url="https://www.google.com/search?q="+data+"+phone+number"
    driver.get(url)
    box = ""
    timeout=0
    while not box:
        if timeout>1:break
        try:
            box = driver.find_element_by_css_selector(".LrzXr.zdqRlf.kno-fv")
            number = box.find_element(By.CSS_SELECTOR, "span")
            value = number.get_attribute('innerHTML')
        except:
            sleep(1)
            timeout+=1
    if timeout>1:
        print(str(nf+f)+" Not Found")
        nf+=1
        continue
    # number = box.find_element(By.CLASS, "LrzXr zdqRlf kno-fv")
    ob.Phone = value
    f+=1
    print((nf+f),ob.Phone)
    ob.save()
    # Open URL
print("Not Found = "+ str(nf))
print("Found = "+ str(f))
