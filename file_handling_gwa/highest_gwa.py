class HighestGwa:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename

    def read_file(self) -> list[str]:
        with open(self.filename, "r") as file:
            return [line.rstrip("\n") for line in file.readlines()]

    def get_highest(self, data: list):
        new_data = [info.split(",") for info in data]
        highest_gwa = max(new_data, key=lambda x: x[1])
        print(f"Highest Gwa: {highest_gwa[0]}\nGwa: {highest_gwa[1]}")

if __name__ == "__main__":
    gwa = HighestGwa()
    data = gwa.read_file()
    gwa.get_highest(data)