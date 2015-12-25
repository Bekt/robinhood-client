import logging
import requests


class Requestor(object):

    def __init__(self, auth_token=None, api_base=None, api_version=None):
        if not auth_token:
            logging.warning('No auth token is provided.')
        if not api_base:
            raise ValueError('No api base URL is provided.')
        self.api_base = api_base
        self.headers = {
            'Authentication': 'Token {}'.format(auth_token),
            'X-Robinhood-API-Version': api_version
        }

    def get(self, url, params=None):
        return self._request(requests.get, url, params=params)

    def post(self, url, data=None):
        return self._request(requests.post, url, data=data)

    def put(self, url, data=None):
        return self._request(requests.put, url, data=data)

    def delete(self, url, data=None):
        return self._request(requests.delete, url, data=data)

    def _request(self, bind, url, **kwargs):
        if url[0] != '/':
            url = '/' + url
        url = self.api_base + url
        r = bind(url, headers=self.headers, **kwargs)
        logging.info('[{}] {} {}'.format(bind.__name__.upper(), r.status_code, url))
        return r.json()
