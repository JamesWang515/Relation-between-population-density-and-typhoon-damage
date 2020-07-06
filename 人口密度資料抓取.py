import requests

url = "https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP048/106"
res = requests.get(url)
filename = "F:\\population_density.json"
with open(filename,'wb') as f:
    f.write(res.content)
