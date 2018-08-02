import os
from src.utils.json_reader import JsonReader

class Settings:

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    KEY = JsonReader.read(PROJECT_ROOT + "/.key.json").get("key")
    ADDRESS_API = "https://api.postmon.com.br/v1/cep/{0}"
    db_settings = JsonReader.read(PROJECT_ROOT + "/db.json")
    DB_SETTINGS = {
        "hostname": db_settings.get("hostname"),
        "db": db_settings.get("db"),
        "username" : db_settings.get("username"),
        "password" : db_settings.get("password")
    }