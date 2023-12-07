import requests
import hashlib

# wine data
wine_url = "https://archive.ics.uci.edu/static/public/109/wine.zip"
response_1 = requests.get(wine_url)
with open('wine.zip', mode='wb') as f:
    f.write(response_1.content)

filename = 'wine.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

wine_sha256 = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'
if wine_sha256 != sha256hash:
    print("Computed hash does not match expected hash for original wine data")
else:
    print("Computed hash matches expected hash for original wine data")
