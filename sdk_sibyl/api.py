import json
import requests


class API:
    SERVER_URL = None
    TOKEN = None

    def doPOST(self, payload, url):
        response = requests.request(
            "POST",
            "{}{}".format(self.SERVER_URL, url),
            data=payload
        )
        return json.loads(response.text)

    def doGET(self, url):
        response = requests.request(
            "POST",
            "{}{}".format(self.SERVER_URL, url),
        )

        return json.loads(response.text)
