from requests import get

def fetch(url):
    response = get(url)
    return response

url = "https://www.baidu.com"
if fetch(url).status_code == 200:
    print("Yeah!")
else:
    print("Oops...")

for i in range(10):
    print("count {}".format(i))