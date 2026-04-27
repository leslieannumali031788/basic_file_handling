class HighestGwa:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename

    def read_file(self) -> list[str]:
        with open(self.filename, "r") as file:
            return [line.rstrip("\n") for line in file.readlines()]

    def get_highest(self, data: list):
        pass