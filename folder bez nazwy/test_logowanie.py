import logowanie
import unittest
import requests
import json


class Testlogowanie(unittest.TestCase):

    def test_logowanie(self):
        log_data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        log_token = {
            "token": "QpwL5tke4Pnpja7X4"
        }

        response = requests.post(logowanie.gl_url() + "/api/login", data=log_data)
        token = json.loads(response.text)

        self.assertEqual(token, log_token)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
