import requests

# build url
path_url = 'http://api.postcodes.io/postocdes/'
arguments = 'e146gt'


post_codes = requests.get(path_url + arguments)
print(post_codes)