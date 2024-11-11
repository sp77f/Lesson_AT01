import requests

def get_cat_url():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return Nones

res = get_cat_url()
url = res[0]['url']
print (res)
print(url)