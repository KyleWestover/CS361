from urllib.request import urlopen

import certifi
import json
import os

def main():
    symbol = ' '
    num_of_calls = 0

    while True:
        called = num_of_calls
        if os.path.getsize('symbol.txt') > 0:
            with open('symbol.txt') as f:
                text = f.read()
                if text != symbol:
                    num_of_calls += 1
                    symbol = text

        if called != num_of_calls:
            print(symbol)
            url = f"https://financialmodelingprep.com/api/v3/profile/{text}?apikey=12ec7ab3910a83907a3a37115874e406"
            data = get_jsonparsed_data(url)

            with open('description.txt', 'w+') as f:
                f.write(data[0]['description'])


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)


if __name__ == '__main__':
    main()
