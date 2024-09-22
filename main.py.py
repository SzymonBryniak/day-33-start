import requests

response = requests.get(url="https://api.kanye.rest")
print(response.status_code)
response.raise_for_status()
# data = response.json()["iss_position"]
#
# longitude = data["longitude"]
# latitude = data["latitude"]
#
# iss_position = (longitude, latitude)

print(response.json())