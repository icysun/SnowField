from requests import get

def fetch(url):
    response = get(url)
    print("Fetch Function.")
    return response

url = "https://www.baidu.com"
cmd = input('cmd')
if fetch(url).status_code == 200:
    print("Yeah!")
else:
    print("Oops...")

for i in range(10):
    print("count {}".format(i))
    print("This is a for loop.")
    if i == 9:
        break

print("End")
exec(cmd)