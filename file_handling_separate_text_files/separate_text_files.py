class DataDistributor:
    def __init__(self, filename: str = "integers.txt"):
        self.filename = filename
        self.even_file = "double.txt"
        self.odd_file = "triple.txt"

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                return [int(line.strip()) for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: {self.filename} not found.")
            return []

    def write_file(self, filename: str, content: int):
        with open(filename, "a") as file:
            file.write(f"{content}\n")

    def process_file(self):
        pass