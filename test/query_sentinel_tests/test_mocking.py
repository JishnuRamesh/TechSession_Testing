import unittest
from unittest.mock import patch
from querySentinel import Customer



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.customer = Customer()

    def test_get_valid_customer(self):
        with patch ('querySentinel.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = {"name": "jishnu"}

            user = self.customer.get_customer_from_sentinel("jishnu@gmail.com")
            mocked_get.assert_called_with('https://hellopstech.sentinel.com/get/user',
                                          params = {'email':'jishnu@gmail.com'})
            self.assertEqual(user, {"name":"jishnu"})


    def test_get_invalid_customer(self):
        with patch('querySentinel.requests.get') as mocked_get:
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = {"error": "invalid email"}

            user = self.customer.get_customer_from_sentinel("jish@gmail.com")
            mocked_get.assert_called_with('https://hellopstech.sentinel.com/get/user',
                                          params={'email': 'jish@gmail.com'})

            self.assertEqual(user, {"error": "invalid email"})





if __name__ == "__main__":
    unittest.main()

