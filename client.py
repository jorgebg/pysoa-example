from pysoa.client import Client

from settings import SOA_CLIENT_SETTINGS


if __name__ == '__main__':
    client = Client({'example': SOA_CLIENT_SETTINGS})
    action_response = client.call_action('example', 'square', {'number': 42})
    print(action_response)
