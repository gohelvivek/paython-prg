import requests
response = requests.get("https://unsplash.com/s/photos/url")
file = open("image2.jpg", "wb")
file.write(response.content)
file.close()
