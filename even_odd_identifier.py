class EvenOddIdentifier:
    def __init__(self, filename: str = "./numbers.txt"):
        self.filename = filename

    def read_file(self) -> list[int]:
        numbers = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    numbers.append(int(line.strip()))
        except FileNotFoundError:
            print("File not found")
        except ValueError:
            print("Ensure that the file only consists of integers.")
        return numbers

    def write_file(self, filename: str, content: int):
        with open(filename, "a") as file:
            file.write(f"{content}\n")

    def categorize(self):
        data = self.read_file()
        for number in data:
            if number % 2 == 0:
                self.write_file("even.txt", number)
            else:
                self.write_file("odd.txt", number)
if __name__ == "__main__":
    extractor = EvenOddIdentifier()
    extractor.categorize()