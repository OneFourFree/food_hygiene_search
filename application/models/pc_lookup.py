import requests

def postcode_lookup(pc):
    response = requests.get('http://api.postcodes.io/postcodes/' + pc)

    data = response.json()

    output = dict()
    output['long'] = data['result']['longitude']
    output['lat'] = data['result']['latitude']
    return output

