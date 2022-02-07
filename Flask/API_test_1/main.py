import requests

url_Bretagne = "http://127.0.0.1:5000/REGION/Bretagne" 

resp = requests.get(url=url_Bretagne)
print(resp.text)