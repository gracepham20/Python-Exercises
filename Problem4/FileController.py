import json
from storefrontconfig import StorefrontConfig


class FileController:
    @staticmethod
    def read_file(file_name):
        with open(file_name) as file:
            data = json.load(file)
            return StorefrontConfig(data)

    @staticmethod
    def write_file(obj, file_name):
        with open(file_name, "w") as file:
            file.write(json.dumps(obj.data))
