from unittest import TestCase
from environs import Env

from sdk_sibyl import Auth

env = Env()
env.read_env()


class SibylAuthTestCase(TestCase):

    def test_get_token(self):
        auth = Auth()
        auth.get_token(
            server=env('SERVER_URL'),
            username=env('USERNAME'),
            password=env('PASSWORD')
        )

        self.assertIsInstance(auth.TOKEN, str)

    def test_refresh_token(self):
        auth = Auth()
        auth.get_token(
            server=env('SERVER_URL'),
            username=env('USERNAME'),
            password=env('PASSWORD')
        )

        token = auth.TOKEN
        auth.TOKEN = None

        auth.refresh_token(token)

        self.assertIsInstance(auth.TOKEN, str)


class SibylUserTestCase(TestCase):

    def test_register(self):
        # todo: allow register user, using the server root user
        pass

    def test_get(self):
        # todo: allow get user info
        pass


class SibylDocumentTestCase(TestCase):

    def test_upload_document(self):
        pass

    def test_get_documents(self):
        pass

    def test_approve_document(self):
        pass

    def test_reject_document(self):
        pass
