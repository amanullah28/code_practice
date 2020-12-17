import requests
# url = "http://www.google.com"
# res = requests.get(url)
# print(f"your request to {url} came back w/ status code {res.status_code}")


url = "https://icanhazdadjoke.com/"
res = requests.get(url, headers = {"Accept": "application/json"})
# print(res.text)
print(res.json())