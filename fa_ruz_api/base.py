import requests


class RuzEndpoint:
    """
    Base class for RUZ endpoint.
    """

    def __init__(self, host='https://ruz.fa.ru/api/{}', endpoint=None):
        self.host = host
        self.endpoint = endpoint

    def _request_(self, endpoint=None, **params):
        """
        Internal requestor of RUZ endpoint.
        The endpoint can be changed on-the-fly by passing the _endpoint_ argument.
        Should not be used directly.
        """
        if endpoint is None:
            endpoint = self.endpoint
        try:
            params = "&".join("%s=%s" % (k, v) for k, v in params.items()) # this prevents requests from additional urlencoding params
            req = requests.get(self.host.format(endpoint), params=params)
            return req.json()
        except Exception as e:
            raise e
