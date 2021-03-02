#logo problimatos sto API tou OPAP pernei ana mia mera kai anagkastika to programma argei
import requests
import json
from datetime import datetime
today = datetime.today()
def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num
for day in range(1,today.day):
    list = []
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + str(datetime(today.year, today.month, day).date()) + "/" + str(datetime(today.year, today.month, day).date()) + "/draw-id"
    r = requests.get(url)
    for k in eval(r.text):
        url2 = "https://api.opap.gr/draws/v3.0/1100/" + str(k)
        r2 = requests.get(url2)
        list += r2.json()["winningNumbers"]["list"]
    mf = most_frequent(list)
    print ("Ο ποιό συχνός αρηθμός της ημέρας " +  str(datetime(today.year, today.month, day).date()) + " είναι ο " + str(mf))
