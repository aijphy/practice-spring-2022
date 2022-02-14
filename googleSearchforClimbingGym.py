import requests,lxml
# soup to parse data from xml format:
from bs4 import BeautifulSoup

print('setting up request')
#host
url = "https://google.com/search"
payload={}
headers = {}
#query:
params={'q':'climbing gym'}

print('getting response, please hold...')
#request a get (could also put, post, delete for apis which I have authorization
response = requests.get( url, headers=headers, params=params)
soup=BeautifulSoup(response.text,'lxml')

print('results:')
cnt=0
#find each xml a division (could use class with ., and I'm guessing id as well)
for result in soup.select('a'):
      cnt=cnt+1
      #get just the href portion:
      link = result['href']
      print(link)

print('# of Results: ',cnt)

