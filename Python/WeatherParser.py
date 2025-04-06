import requests
from bs4 import BeautifulSoup

url = "https://www.foreca.com/100658225/Helsinki-Finland"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        title = soup.find('div', {'class': 'wrap cloudLight'}).next.get_text()
        price = soup.find('span', {'class': 'temp'}).get_text()

        print("City:", title)
        print("Temperature C:", price)
    except AttributeError:
        print("Error")
else:
    print("Load page error")

