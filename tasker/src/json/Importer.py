import json


class Importer:
    imported_data = []

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj

        with open("taski.json") as file:
            self.imported_data = json.load(file)
            file.close()


    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj

        return self.imported_data
