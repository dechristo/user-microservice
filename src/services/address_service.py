import requests
from settings import Settings


class AddressService:

    @staticmethod
    def get_address_by_zip_code(zip_code):
        address = requests.get(Settings.ADDRESS_API.format(zip_code))
        return address.json() if address else None
