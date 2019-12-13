import requests

# build url
path_url = 'http://api.postcodes.io/postcodes/'
arguments = 'ox495nu'


post_codes = requests.get(path_url + arguments)

dict_response = post_codes.json()

# Getting out data

print(dict_response['result'].keys())
print(dict_response['result']['postcode'])
print(dict_response['result']['longitude'])
print(dict_response['result']['latitude'])
print(dict_response['result']['nuts'])
print(dict_response['result']['admin_ward'])

def postcode_lat():
    ask_postcode = input('What is the postcode you want to find the latitude of?')
    path_url = 'http://api.postcodes.io/postcodes/'
    result = requests.get(path_url + ask_postcode.strip())
    post_code_dictionary = result.json()
    return post_code_dictionary['result']['latitude']

def postcode_long():
    ask_postcode = input('What is the postcode you want to find the longitude of?')
    path_url = 'http://api.postcodes.io/postcodes/'
    result = requests.get(path_url + ask_postcode.strip())
    post_code_dictionary = result.json()
    return post_code_dictionary['result']['longitude']

def search_postcode():
    ask_postcode = input('What is the postcode you would like to search for?')
    path_url = 'http://api.postcodes.io/postcodes/'
    result = requests.get(path_url + ask_postcode.strip())
    post_code_dictionary = result.json()

ask_file = input('Please name the file you would like to insert your postcode data into')
file_name = ask_file + '.txt'
try:
    with open(file_name, 'w+') as file_created:
        file_created.write(f"Postcode: {post_code_dictionary['result']['postcode']}."
                            f" Longitude: {post_code_dictionary['result']['longitude']}."
                            f" Latitude: {post_code_dictionary['result']['latitude']}."
                            f" Nuts: {post_code_dictionary['result']['nuts']}."
                            f" Admin Ward: {post_code_dictionary['result']['admin_ward']}.")
except TypeError as error:
        print('Please ensure you have all the correct information')
finally:
        print('Completed')
