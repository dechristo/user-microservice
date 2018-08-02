import json

class JsonReader:

    @staticmethod
    def read(path):
        db_settings = {}
        with open(path) as json_file:
            data = json.load(json_file)
            for attribute in data:
               db_settings[attribute] = data[attribute]
        return db_settings