import requests
from bs4 import BeautifulSoup

req = requests.get('http://jadwalsholat.pkpu.or.id/?id=308')
soup = BeautifulSoup(req.text, 'html.parser')

datt = soup.find('td', {'align': 'center'}).find('b').text
place = soup.find('td', {'align': 'center'}).find('small').find('b').text
scrap = soup.find_all('tr', 'table_highlight')
scrap = scrap[0]
data = {}

i = 0
for j in scrap:
    if i > 0:
        if i == 1:
            data['subuh'] = j.get_text()
        elif i == 2:
            data['dzuhur'] = j.get_text()
        elif i == 3:
            data['ashar'] = j.get_text()
        elif i == 4:
            data['maghrib'] = j.get_text()
        elif i == 5:
            data['isya'] = j.get_text()
    else:
        data['date'] = j.get_text() + ' ' + datt + ' di ' + place
    i += 1

print(f"jadwal sholat pada tanggal {data['date']}, yaitu:")
print(f"subuh: {data['subuh']}")
print(f"dzuhur: {data['dzuhur']}")
print(f"ashar: {data['ashar']}")
print(f"maghrib: {data['maghrib']}")
print(f"isya: {data['isya']}")
