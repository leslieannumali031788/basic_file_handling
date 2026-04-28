class DataDistributor:
    def __init__(self, filename: str = "integers.txt"):
        self.filename = filename
        self.even_file = "double.txt"
        self.odd_file = "triple.txt"

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:

    def write_file(self, filename: str, content: int):
        pass

    def process_file(self):
        pass