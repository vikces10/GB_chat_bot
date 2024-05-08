import requests

def fox():
    url = 'http://randomfox.ca/floof/'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        image = data.get('image')
        return image

def coin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)

    # Check explicitly for a successful status code
    if response.status_code == 200:
        data = response.json()
        # Access the desired data fields
        usd_price = data.get('bpi', {}).get('USD', {}).get('rate', 'N/A')
 # Construct a response string
        return f"BTC = {usd_price} USD"
    else:
        return "Failed to retrieve data"


def get_ip():
    url = 'https://api.ipify.org?format=json'
    response = requests.get(url)

    # Check explicitly for status code 200 (successful request)
    if response.status_code == 200:
        data = response.json()
        # Retrieve the value using the correct key 'ip'
        ip_address = data.get('ip')
        return ip_address
    else:
        return "Failed to retrieve IP address"



if __name__ == '__main__':
    print(fox())
    print(get_ip())
    print(coin())
