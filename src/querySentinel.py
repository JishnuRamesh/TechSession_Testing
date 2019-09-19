
import requests


class Customer:

    def get_customer_from_sentinel(self, email):
        if email is not None:
            params = {"email" : email}
            response = requests.get("https://hellopstech.sentinel.com/get/user", params=params)

            if response.ok:
                return response.text
            else:
                raise {"error": "invalid email"}


if __name__ == "__main__":
    c = Customer()
    c.get_customer_from_sentinel("jis")