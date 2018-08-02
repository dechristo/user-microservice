import requests

class AddressService:

    @staticmethod
    def get_address_by_zip_code(zip_code):
        address = requests.get("https://api.postmon.com.br/v1/cep/{0}".format(zip_code))
        return address.json() if address else None
