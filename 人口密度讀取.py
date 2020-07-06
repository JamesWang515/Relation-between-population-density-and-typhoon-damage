import requests, json, os
import pandas as pd

filename = f"D:\\population_density.json"
with open(filename, 'r', encoding='utf-8') as f:
    fdata = json.loads(f.read())
    
datas = fdata['responseData']

for dt in datas:
    dt['city'] = dt['site_id'][0:3]

for data in datas:
    try:
        data['people_total'] = int(data['people_total'])
        data['area'] = float(data['area'])
    except:
        data['people_total'] = _
        data['area'] = _

df = pd.DataFrame(datas)
gb = df.groupby(['city'])
ndf = gb[['people_total', 'area']].sum()
try:
    ndf["population_density"] = ndf['people_total'] / ndf['area']
except:
    ndf["population_density"] = _

ndf.to_excel(os.path.join("D://popnlation_density_analysis.xls"))
