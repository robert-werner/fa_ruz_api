import requests


class RuzEndpoint:

    def __init__(self, host='https://ruz.fa.ru/api/{}', endpoint=None):
        self.host = host
        self.endpoint = endpoint

    def _request_(self, endpoint=None, **params):
        if endpoint is None:
            endpoint = self.endpoint
        try:
            params = "&".join("%s=%s" % (k, v) for k, v in params.items())
            req = requests.get(self.host.format(endpoint), params=params)
            return req.json()
        except Exception as e:
            raise e
