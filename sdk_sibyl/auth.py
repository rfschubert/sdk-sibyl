from .api import API


class Auth(API):

    def get_token(self, server: str, username: str, password: str):
        self.SERVER_URL = server
        response = self.doPOST(
            payload={
                'username': username,
                'password': password
            },
            url='/api/token'
        )
        self.TOKEN = response['token']
        return response

    def refresh_token(self, token: str):
        response = self.doPOST(
            payload={
                'token': token
            },
            url='/api/token/refresh'
        )
        self.TOKEN = response['token']
        return response
