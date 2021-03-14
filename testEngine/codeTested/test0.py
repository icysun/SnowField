from requests import get

def fetch(url):
    response = get(url)
    return response

url = "https://www.baidu.com"
if fetch(url).status_code == 200:
    print("Yeah!")
else:
    print("Oops...")